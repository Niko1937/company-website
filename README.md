# Quests Ltd. — Company Website

IT企業 **Quests Ltd.** のコーポレートサイト（ランディングページ）。
SPA構成で、軽量かつ多言語（英語・日本語）に対応しています。

- 本番URL: https://quests.it.com/
- デプロイ先: GitHub Pages（カスタムドメイン `quests.it.com`、`CNAME` で設定）

---

## ホームページの仕様

### 技術スタック

| 項目 | 採用技術 |
|------|---------|
| マークアップ | HTML5（静的、SPA） |
| スタイル | Tailwind CSS（CDN経由、3.4.16） |
| アイコン | Remixicon（CDN） |
| フォント | Inter（Google Fonts） |
| フォーム送信 | サーバー送信なし。入力内容を入れたメール作成画面（メールアプリ／Gmail／Outlook）を開く |
| ホスティング | GitHub Pages |
| ビルドステップ | なし（静的ファイル配信のみ） |

### ファイル構成

```
.
├── index.html              ルート: ブラウザ言語に応じて /en/ または /ja/ へリダイレクト
├── en/index.html           英語版エントリポイント（canonical）
├── ja/index.html           日本語版エントリポイント（canonical）
├── en/privacy/, ja/privacy/  プライバシーポリシー（独立した静的ページ。後述「プライバシーポリシー・利用規約」）
├── en/terms/, ja/terms/      利用規約（同上）
├── locales/
│   ├── v2/
│   │   ├── en.json         英語の全テキスト（翻訳のソース・オブ・トゥルース。編集するのはこちら）
│   │   └── ja.json         日本語の全テキスト
│   ├── en.json             固定の旧版（キャッシュに残った古いページ用。編集しない。後述）
│   └── ja.json             同上
├── assets/
│   └── js/
│       ├── i18n.js         言語切替ロジック（依存ライブラリなし）
│       ├── site-config.js  表示設定の値（後述「表示設定」）
│       ├── config.js       表示設定を画面に反映するロジック
│       ├── solutions.js    Solutions のデモ動画の表示・再生（後述「Solutions のデモ動画」）
│       ├── section-links.js  ページ内リンク（#services など）の移動と URL の更新（後述「セクションへのリンク」）
│       └── cases.js        Case Studies の絞り込みと、詳細の重ね表示（`#cases-<id>`）
├── videos/solutions/       （任意）Solutions のカードで流す短いループ映像。使うときに作成する
├── images/                 静的画像（後述「画像の管理」）
│   ├── brand/              サイトで使うファビコン・アプリアイコン（正本は _sources/brand/ からのコピー）
│   ├── hero/               Hero 背景
│   ├── about/              About の写真
│   ├── services/           サービスカードの写真（ファイル名 = services.items のキー）
│   └── cases/              導入事例カードの写真（ファイル名 = cases.items のキー）
├── _sources/photos/        写真の元画像（生成時の解像度・高画質JPEG）と生成プロンプト。`_` 始まりのため GitHub Pages では非公開
├── _sources/brand/         ロゴに関する全ファイルの正本（資料・SNS 用、サイト用）とロゴの意味（同フォルダの README.md）。GitHub Pages では非公開
├── scripts/
│   ├── optimize_images.py  写真を Web 用（JPEG/WebP・2サイズ）に変換するスクリプト
│   ├── build_icons.py      ロゴの PNG / ICO を作り、サイト用のファイルを公開場所へコピーするスクリプト
│   ├── legal_pages/        プライバシーポリシー・利用規約のページを作るスクリプトと文面（content_en.py / content_ja.py）
│   └── check_lang_links.py すべてのサイト内リンクが表示言語を保つか（/ja/ のページから /en/ に飛ばないか）を確認する
├── favicon.ico             旧ブラウザ用ファビコン（16/32/48px）
├── apple-touch-icon.png    iPhone のホーム画面用アイコン（180px）
├── site.webmanifest        Android のホーム画面用の設定
├── CNAME                   GitHub Pagesのカスタムドメイン設定
├── _config.yml             GitHub Pages で公開しないファイルの設定（CLAUDE.md・README.md・scripts/・tasks/）
├── README.md               このファイル
└── services/               別サービスの情報置き場（後述、LP関連の情報を入れないこと）
```

### 多言語対応（i18n）

**戦略:** サブディレクトリ方式 + JSONベース + JS動的差し替え。

- **`/en/`** が英語、**`/ja/`** が日本語の正規URL（canonical）。
- HTML テンプレートは `/en/index.html` と `/ja/index.html` で共通（同一構造）。
- 翻訳テキストは `/locales/v2/en.json` と `/locales/v2/ja.json` に集約。
- `/assets/js/i18n.js` がページ読み込み時に該当JSONを fetch し、`data-i18n` 属性が付いたDOM要素を書き換える。

#### 翻訳キーの追加方法

1. `/locales/v2/en.json` と `/locales/v2/ja.json` の両方に、同じキー構造で値を追加する。
2. HTML側で対象要素に `data-i18n="path.to.key"` を付与する。
   - 単一テキスト: `data-i18n="hero.title"`
   - リスト（`<li>` の自動生成）: `data-i18n-list="services.items.consulting.bullets"`
   - 属性値（例: placeholder）: `data-i18n-attr-placeholder="contact.form.namePlaceholder"`
3. JSコードから動的に翻訳文字列を取得したい場合は `window.i18n.t('path.to.key')` を使用する。

#### デプロイ直後のキャッシュ対策（翻訳JSONのバージョン管理）

GitHub Pages は HTML に最大10分のキャッシュを付けるため、利用者のブラウザでは「古い HTML・`i18n.js`」がしばらく動き続けることがある。古い `i18n.js` が新しい書き方の翻訳JSON（`{company}` のような置き換え用の記号など）を読むと、記号がそのまま表示されてしまう。これを防ぐため、翻訳JSONは `i18n.js` のバージョンごとのフォルダに置いている。

- `i18n.js` は `/locales/v<I18N_VERSION>/<言語>.json` を読む（現在は `v2`）。**文言の編集は常に最新のフォルダで行う。**
- 古いフォルダと `/locales/en.json`・`ja.json`（v1 以前の `i18n.js` が読む場所）は**固定の旧版**として残し、編集しない。置き換え用の記号を含まない内容なので、古いページは更新前の文言（例: 会社名「Quests」）で表示され、`{…}` は表示されない。
- 翻訳JSONで、古い `i18n.js` では表示できない新しい書き方を使い始めるときは、次をそろえて行う。
  1. `/assets/js/i18n.js` の `I18N_VERSION` を1つ上げる。
  2. 翻訳JSONを新しいフォルダ（例: `/locales/v3/`）にコピーして、そちらを編集する。`meta.requiresI18n` を同じ番号にする。
  3. 直前のフォルダ（例: `v2`）は、新しい書き方を含まない状態で固定する。
  4. `/en/index.html` と `/ja/index.html` の `i18n.js?v=` を上げる。

念のための二重の対策として、`i18n.js` は自分より新しい翻訳JSONを読んだ場合にページを1回だけ自動で再読み込みし、置き換えられない `{…}` が残る文言は画面に入れない。

#### ルート（`/`）アクセス時の言語振り分けロジック

`/index.html` のスクリプトが以下の優先順で判定し、`/en/` または `/ja/` にリダイレクトする。

| 優先順位 | 判定材料 | 動作 |
|---------|---------|------|
| ① | `localStorage.preferredLang` | ユーザーが過去にスイッチャーで選んだ言語を最優先 |
| ② | `navigator.language` | 値が `ja` で始まれば日本語、それ以外は次の判定へ |
| ③ | デフォルト | 英語（`/en/`）にフォールバック |

ユーザーが言語スイッチャーで明示的に切り替えると、その選択は `localStorage` に保存され、次回以降のルートアクセスで再利用される。

#### SEO対応

各言語ページの `<head>` に以下を設定済み:

```html
<link rel="canonical" href="/en/">                <!-- 英語ページなら /en/, 日本語ページなら /ja/ -->
<link rel="alternate" hreflang="en" href="/en/">
<link rel="alternate" hreflang="ja" href="/ja/">
<link rel="alternate" hreflang="x-default" href="/en/">
```

`<html lang>` 属性も i18n.js が言語に合わせて動的に更新する。

**リンクを共有したときの表示（OGP タグ）**

LinkedIn・Slack・X などにリンクを貼ったときのタイトル・説明・画像は、`en/index.html`・`ja/index.html`・ルートの `index.html` の `<head>` にある `og:*`・`description`・`twitter:card` で決まる（[LinkedIn の仕様](https://www.linkedin.com/help/linkedin/answer/46687)：画像は 1200×627px 以上、1.91:1、5MB まで、`https://` から始まる URL）。

- 共有する側のクローラーは JavaScript を実行しないため、翻訳JSONではなく HTML に直接書いている。文言を変えるときは3ファイルとも直す（ルートは英語ページと同じ内容で、`og:url` だけ `https://quests.it.com/`）。
- `<title>` も同じ文言で、翻訳JSONの `meta.title` と合わせている（JavaScript が動いた後は `meta.title` が使われる）。
- 社名（`site-config.js` の `companyName`）を変えたときは、これらの「Quests」も手で直す。
- 画像は `/images/og/quests-1200x627.png`（元は `_sources/brand/linkedin/banner.html#og`。作り直し方は `_sources/brand/README.md`）。
- LinkedIn はプレビューをしばらく保存する。変更を反映した後は、[Post Inspector](https://www.linkedin.com/post-inspector/) で URL を調べ直すと新しい内容になる。既に投稿・登録したリンクは古いままなので、貼り直す。

### 表示設定（site-config.js）

ページの表示内容の一部を、`/assets/js/site-config.js` の値で切り替えられる。値を変更して `main` に push すれば反映される（ビルド不要）。

```js
window.SITE_CONFIG = {
  showMarshallOffice: true,
  companyName: "Quests",
  solutions: [ /* 後述「Solutions のデモ動画」 */ ],
};
```

| キー | 内容 | 既定値 |
|------|------|--------|
| `showMarshallOffice` | Contact の Offices に Quests Ltd.（Marshall）を表示するか。`false` にすると非表示になり、PCの2列表示では空いた分だけ地図が縦に広がる | `true` |
| `companyName` | LP に表示する法人名。`"Quests"` または `"Quests Bay"`。英語版・日本語版のすべてのセクション（ページタイトル、ヘッダー、About、フォーム、利用規約、フッター等）に反映される。**Offices の正式名称（Quests Bay Pte. Ltd. / Quests Ltd.）は変わらない** | `"Quests"` |
| `solutions` | Solutions セクションに載せるデモ動画の一覧（後述「Solutions のデモ動画」）。表示する動画が 0 本ならセクションごと表示されない | `[]` |

#### 仕組みと項目の追加方法

- `/assets/js/config.js` が `<head>` 内で同期実行され、条件に合わない要素を `display:none` にするスタイルを描画前に差し込む（ちらつきなし）。
- HTML側は対象要素に属性を付けるだけでよい（`/en/` と `/ja/` の両方に付けること）。
  - `data-show-if="key"`: 値が `true` のときだけ表示（`false` や未定義、設定ファイルの読み込み失敗時は非表示）
  - `data-hide-if="key"`: 値が `true` のときは非表示
- 項目を追加するときは、`site-config.js` にキーを足し、上の表にも追記する。
- JSから値を読む場合は `window.siteConfig.get('key')` を使う。
- 法人名を文言に入れるときは、翻訳JSONに法人名を直接書かず `{company}` と書く（例: `"About {company}"`）。`/assets/js/i18n.js` が読み込み時に `companyName` の値へ置き換える。Offices の正式名称のように、設定に関係なく固定したい名前は直接書く。
- **注意:** 非表示はCSSで隠すだけなので、要素はHTMLソースに残る（開発者ツール等で見える）。また `site-config.js` 自体も公開ファイルなので、秘密情報は書かないこと。

### Solutions のデモ動画

Solutions セクション（Services と Cases の間。ページの中に浮かぶ、角の丸い暗いパネル）に、自社ソリューションのデモ動画を「法人向け」「個人向け」の2段で並べる。動画は `site-config.js` の `solutions` に書くだけで追加・変更・非表示にできる（HTML や翻訳JSONの編集は不要）。

```js
solutions: [
  {
    id: "ai-chatbot",            // 動画ごとのリンク名（#solutions-ai-chatbot）。英小文字・数字・ハイフン。重複不可
    category: "business",        // "business"（法人向け）または "consumer"（個人向け）
    show: true,                  // false にすると表示しない
    video: { en: "AbCdEfGhIjK", ja: "LmNoPqRsTuV" },  // YouTube の動画 ID（11文字）
    title: { en: "AI Chatbot", ja: "AIチャットボット" },
    description: { en: "Answers customer questions 24/7.", ja: "お客様の質問に24時間回答します。" },  // 任意。\n で改行
    preview: "/videos/solutions/ai-chatbot.mp4",      // 任意
  },
],
```

| 項目 | 内容 |
|------|------|
| `video` / `title` / `description` | 英語・日本語で別の値を設定できる。**片方の言語が空なら、もう片方の言語の値を表示する**（例: 日本語版の動画しかなければ、英語ページでも日本語版を流す）。両言語で同じなら `title: "Quests AI"` のように文字列1つでもよい |
| YouTube の動画 ID | 動画の URL の `v=` の後ろ、または `youtu.be/` の後ろの11文字（`https://www.youtube.com/watch?v=AbCdEfGhIjK` なら `AbCdEfGhIjK`）。限定公開の動画も使える |
| `preview` | カードで流す数秒の無音ループ映像。`/videos/solutions/` に置いた MP4（または WebM）を指定する。数MB以内にすること（GitHub Pages は1ファイル100MBまで）。画面に入ったときだけ再生し、「視差効果を減らす」設定の利用者には再生しない。未指定ならサムネイルのみ |

**表示のルール**

- 動画が 0 本の段（法人向け・個人向け）は見出しごと隠れる。両方 0 本ならセクションと、ヘッダー・スマホメニュー・フッターの「Solutions」、Hero の「ソリューションを見る」ボタンも隠れる。
- 段の見出し（法人向け／個人向け）は中央に表示する。両方の段があるときだけ、見出しと間の区切り線を出す。片方の段しかないときは、段の見出しも再生画面の見出し上の小さな「法人向け」も出さない（ほかの種類もあるように見えないようにするため）。
- 1段のカードがすべて画面に収まるときは、カードも中央に並べる。
- 1段のカードが画面に収まらないとき（PC では3本以上、スマホでは2本以上）は、次のカードの一部が右端からのぞき、列の下の ← → ボタンとスワイプで送れる。矢印の左には見えている範囲（例: `1–3 / 6`）を出す。収まるときは矢印も件数も出さない。
- 再生画面でも、同じ段の前後の動画に `2 / 6 (←)(→)` と ← → キーで送れる（送り操作の見た目は Case Studies の詳細画面と共通の部品 `.pager`）。
- カードには YouTube のサムネイルを表示する（`i.ytimg.com` から読み込み）。プレーヤーはクリックされてから読み込むため、ページは重くならない。再生は `youtube-nocookie.com` の埋め込みで、画面に重なるウィンドウ（Esc・背景クリックで閉じる）で行う。
- 書き方に誤りがある項目（ID の形式、カテゴリ、動画 ID、タイトルなし、重複など）は表示されず、ブラウザのコンソールに `[solutions] Skipped solutions[番号]: check ...` と理由が出る。追加後に表示されないときはコンソールを確認する。
- タイトル・説明は文字としてそのまま表示される（HTML は使えない）。
- 段見出し・セクション見出し・ボタン名は翻訳JSONの `solutions.*` で管理する。

**注意**

- `site-config.js` は公開ファイルなので、`show: false` の動画も ID は誰でも見られる。**公開前の動画は書かないこと。** また、限定公開の動画も URL を知っていれば誰でも見られるため、社外秘の画面は映さない。
- YouTube は、収益化していない動画にも広告を表示することがある。広告を確実に避けたい場合は、Vimeo などへの移行を検討する（`solutions.js` の埋め込み URL の変更が必要）。
- 変更は push 後、利用者のブラウザでは最大約10分古いまま見えることがある（GitHub Pages のキャッシュ）。

### プライバシーポリシー・利用規約

トップページを軽く保つため、法務の文書は独立したページにしている（`/en/privacy/` `/ja/privacy/` `/en/terms/` `/ja/terms/`）。フッターとお問い合わせフォームの下の一文からリンクしている。

- 文面は `scripts/legal_pages/content_en.py`（英語）と `content_ja.py`（日本語）にある。直したら、リポジトリのルートで次を実行して4ページを作り直し、生成された HTML もコミットする。
  ```bash
  python3 scripts/legal_pages/build.py .
  ```
- 改定したときは、両方のファイルの `updated`（最終更新日）も更新する。
- ヘッダーとフッターはトップページと同じ見た目・動き（大手 IT 企業の法務ページと同じ構成）。ただし Tailwind は使わず、同じ見た目を CSS で再現した軽いページ。メニューやフッターの文言は `locales/v2/*.json`、社名は `site-config.js` の `companyName` から作るため、これらを変えたときも上のコマンドで作り直す。
- 迷惑メール対策のため、サイトにはメールアドレスを表示しない。法務ページの問い合わせ窓口は、トップページのお問い合わせフォーム（`/ja/#contact`）へのリンクにしている。
- 文面は大手 IT・コンサル企業の構成を参考にした雛形。公開前に、代表者名・個人情報保護責任者（DPO）の任命状況・準拠法などを含め、専門家の確認を受けること。

### 表示言語の維持

ページを移動しても表示中の言語は変わらない。サイト内リンクは言語付きのパスか相対パスで書き、各ページは開いた言語をブラウザに保存する（`preferredLang`）。ページやリンクを追加・変更したら、次を実行して OK になることを確認する。

```bash
python3 scripts/check_lang_links.py
```

### セクションへのリンク

各セクションには ID があり、URL で直接開ける。メニューを押したときも、アドレスバーの URL がこの形になる（ブラウザの履歴は増やさないので、「戻る」1回で前のサイトに戻る）。

| URL の例 | 開いたときの表示 |
|------|------|
| `https://quests.it.com/ja/#services` | Services（同様に `#about` `#solutions` `#cases` `#contact`） |
| `https://quests.it.com/ja/#privacy-policy` | 以前のページ内リンク。`/ja/privacy/` へ自動で移動する（`#terms-of-service` は `/ja/terms/`） |
| `https://quests.it.com/ja/#solutions-<id>` | Solutions を表示し、`id` の動画の再生ウィンドウを開いた状態にする。その動画が非表示・削除済みなら Solutions を表示 |
| `https://quests.it.com/ja/#cases-<id>` | Case Studies を表示し、その事例の詳細を開いた状態にする。`id` は事例カードの `data-case`（例: `material` `chatbot` `predictive` `dashboard` `voice` `legacy`）。存在しない ID なら Case Studies を表示 |
| `https://quests.it.com/#solutions` | ブラウザの言語に合わせて `/en/` または `/ja/` に移り、`#solutions` は引き継ぐ |

- 外部から開いたときは、スクロールの動きなしに最初からそのセクションを表示する。翻訳の反映や画像の読み込みで位置がずれた場合も、利用者がまだ操作していなければ位置を合わせ直す。
- 動画ごとのリンクを外部から開いた場合、ブラウザの方針で自動再生が止められ、再生ボタンを押す状態で表示されることがある。
- 固定ヘッダーに見出しが隠れないよう、移動位置は CSS の `scroll-margin-top` で調整している（Solutions は角の丸い暗いパネルの上の余白がヘッダーのすぐ下に来る位置）。
- 言語を切り替えても `#...` は保たれる。

### 画像の管理

**配置ルール**

- ディレクトリ名は HTML のセクションID（`hero` / `about` / `services` / `cases`）、ロゴは `brand/`。
- サービス・事例の写真のファイル名は、翻訳JSONのキーと同じにする（例: `cases.items.voice` → `images/cases/voice.*`）。項目を追加・削除するときは、画像も同じ名前で追加・削除する。
- 各写真は4ファイル1組: `<名前>.jpg` / `<名前>.webp`（幅1200px）と `<名前>-600.jpg` / `<名前>-600.webp`（幅600px）。Hero 背景は `background.jpg` / `background.webp`（幅1536px）のみ。

**写真を追加・差し替える手順**

1. 元画像（3:2 推奨、幅1200px以上）を `_sources/photos/` に同じ名前で保存し、そこから Web 用ファイルを作る（Pillow が必要: `pip install pillow`）:

   ```bash
   python3 scripts/optimize_images.py _sources/photos/cases/<キー>.jpg images/cases/<キー>
   # Hero 背景のみ: python3 scripts/optimize_images.py _sources/photos/hero/background.jpg images/hero/background --widths 1536
   ```

2. HTML（`/en/` と `/ja/` の両方）に、既存のカードと同じ形の `<picture>` を書く。WebP 対応ブラウザには WebP、それ以外には JPEG が、画面幅と解像度に合わせて 600px / 1200px から自動で選ばれる。
3. 代替テキストは `data-i18n-attr-alt` で翻訳JSONの `imageAlt` キーを参照する（`/locales/v2/en.json` と `/locales/v2/ja.json` の両方に追加）。

### ロゴとアイコン

ロゴマークは「円 + 右下の角 + 中心の穴」でできた Q の形。100単位の格子で、外側の円の半径 40・角の丸み 10・穴の半径 20（4 : 2 : 1）。16px・32px でも各寸法が整数ピクセルになるため、小さいサイズでも輪郭がくっきり出る。

ロゴに関するファイルは、**すべて `_sources/brand/` にある**（正本）。サイトの公開場所には、サイトで実際に使う次の5ファイルだけをコピーして置く。

| サイトでの配置 | 用途 |
|---------|------|
| `/images/brand/favicon.svg` | ファビコン（ブラウザのダークモードでは白に切り替わる） |
| `/favicon.ico` | SVG ファビコン非対応のブラウザ用（16/32/48px） |
| `/apple-touch-icon.png` | iPhone のホーム画面用（紺の背景に白のマーク） |
| `/images/brand/icon-192.png` / `icon-512.png` | Android のホーム画面用（`site.webmanifest` から参照） |

資料・LinkedIn などで使うロゴ一式と、ロゴの意味・使い方のルールは `_sources/brand/README.md` を参照。

ロゴを変更したら、`_sources/brand/` の SVG を更新したうえで `python3 scripts/build_icons.py`（Pillow が必要）を実行する。PNG / ICO が作り直され、サイト用のファイルが公開場所へコピーされる。スクリプト内の寸法（`GEOMETRY`）も SVG と合わせること。サイト側のコピーは直接編集しない。

### コンテンツ更新時の注意

- **HTML構造（タグの追加・削除等）を変更する場合**: `/en/index.html` と `/ja/index.html` の両方を更新する必要がある（同一構造を保つため）。
- **テキストのみの更新**: `/locales/v2/en.json` と `/locales/v2/ja.json` を編集するだけで反映される。
- 一方の言語にだけキーを追加すると、もう一方の言語ではフォールバックとしてHTML側のデフォルト値（英語）が表示される。両方のJSONに必ず追加すること。

---

## 開発

### 必要環境

- Python 3（`python3 -m http.server` を使う場合）
  - 代替: Node.js の `npx serve`、`live-server` など任意のローカルサーバでも可

### ローカルサーバの起動と動作確認

`file://` プロトコルで直接HTMLを開くと、絶対パス（`/assets/...` `/locales/...`）が解決できず、`fetch` も CORS でブロックされて動作しません。**必ずHTTPサーバ経由で確認してください。**

1. プロジェクトルートで HTTP サーバを起動:

   ```bash
   python3 -m http.server 8000
   ```

2. ブラウザで以下のURLにアクセスして動作確認:

   | URL | 確認内容 |
   |-----|---------|
   | http://localhost:8000/ | ブラウザ言語に応じて `/en/` または `/ja/` にリダイレクトされること |
   | http://localhost:8000/en/ | 英語ページが正常に表示されること |
   | http://localhost:8000/ja/ | 日本語ページが正常に表示されること |

3. 確認ポイント:
   - ヘッダー右側の「English | 日本語」スイッチャーで言語切替ができ、URLも切り替わること
   - 現在の言語ボタンがプライマリーカラーでハイライトされること
   - サービスのカードに要点（箇条書き）が表示され、導入事例の「詳細を見る」で詳細ウィンドウが開くこと
   - Contact フォームの送信エラー / 成功メッセージが言語に応じて表示されること

4. 言語振り分けのテスト:

   ブラウザの DevTools コンソールで以下を実行すると、初回訪問状態を再現できます。

   ```javascript
   localStorage.removeItem('preferredLang');
   ```

   その上で http://localhost:8000/ にアクセスし、ブラウザの言語設定（Chrome: 設定 → 言語）に応じた振り分け動作を確認する。

### デプロイ

- `main` ブランチへのpushで GitHub Pages が自動デプロイ。
- ビルド処理はなし。リポジトリ内のファイルがそのまま `https://quests.it.com/` 配下で配信される。
- 反映には数分かかる場合あり。

---

## 重要: `services/` ディレクトリの扱い

**`services/` 配下は、本ランディングページ（LP）以外の別サービスの情報を置く場所です。**

- LPに関するファイル（HTML、画像、翻訳JSON、JS、CSS等）は `services/` 配下に置かない。
- LPに関する設定や仕様の追記が必要な場合は、本READMEまたはプロジェクトルートの該当ディレクトリ（`/locales/`, `/assets/` 等）で対応する。
- AIエージェント（Claude Code等）に作業を依頼する際も、`services/` 配下は明示的な指示がない限り編集対象外として扱う旨が `CLAUDE.md` に記載されている。
