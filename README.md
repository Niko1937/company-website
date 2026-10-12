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
| グラフ | ECharts（CDN） |
| フォント | Inter（Google Fonts） |
| フォーム送信 | Formspree |
| ホスティング | GitHub Pages |
| ビルドステップ | なし（静的ファイル配信のみ） |

### ファイル構成

```
.
├── index.html              ルート: ブラウザ言語に応じて /en/ または /ja/ へリダイレクト
├── en/index.html           英語版エントリポイント（canonical）
├── ja/index.html           日本語版エントリポイント（canonical）
├── locales/
│   ├── en.json             英語の全テキスト（翻訳のソース・オブ・トゥルース）
│   └── ja.json             日本語の全テキスト
├── assets/
│   └── js/
│       ├── i18n.js         言語切替ロジック（依存ライブラリなし）
│       ├── site-config.js  表示設定の値（後述「表示設定」）
│       └── config.js       表示設定を画面に反映するロジック
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
│   └── build_icons.py      ロゴの PNG / ICO を作り、サイト用のファイルを公開場所へコピーするスクリプト
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
- 翻訳テキストは `/locales/en.json` と `/locales/ja.json` に集約。
- `/assets/js/i18n.js` がページ読み込み時に該当JSONを fetch し、`data-i18n` 属性が付いたDOM要素を書き換える。

#### 翻訳キーの追加方法

1. `/locales/en.json` と `/locales/ja.json` の両方に、同じキー構造で値を追加する。
2. HTML側で対象要素に `data-i18n="path.to.key"` を付与する。
   - 単一テキスト: `data-i18n="hero.title"`
   - リスト（`<li>` の自動生成）: `data-i18n-list="services.items.consulting.bullets"`
   - 属性値（例: placeholder）: `data-i18n-attr-placeholder="contact.form.namePlaceholder"`
3. JSコードから動的に翻訳文字列を取得したい場合は `window.i18n.t('path.to.key')` を使用する。

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

### 表示設定（site-config.js）

ページの表示内容の一部を、`/assets/js/site-config.js` の値で切り替えられる。値を変更して `main` に push すれば反映される（ビルド不要）。

```js
window.SITE_CONFIG = {
  showMarshallOffice: true,
  companyName: "Quests",
};
```

| キー | 内容 | 既定値 |
|------|------|--------|
| `showMarshallOffice` | Contact の Offices に Quests Ltd.（Marshall）を表示するか。`false` にすると非表示になり、PCの2列表示では空いた分だけ地図が縦に広がる | `true` |
| `companyName` | LP に表示する法人名。`"Quests"` または `"Quests Bay"`。英語版・日本語版のすべてのセクション（ページタイトル、ヘッダー、About、フォーム、利用規約、フッター等）に反映される。**Offices の正式名称（Quests Bay Pte. Ltd. / Quests Ltd.）は変わらない** | `"Quests"` |

#### 仕組みと項目の追加方法

- `/assets/js/config.js` が `<head>` 内で同期実行され、条件に合わない要素を `display:none` にするスタイルを描画前に差し込む（ちらつきなし）。
- HTML側は対象要素に属性を付けるだけでよい（`/en/` と `/ja/` の両方に付けること）。
  - `data-show-if="key"`: 値が `true` のときだけ表示（`false` や未定義、設定ファイルの読み込み失敗時は非表示）
  - `data-hide-if="key"`: 値が `true` のときは非表示
- 項目を追加するときは、`site-config.js` にキーを足し、上の表にも追記する。
- JSから値を読む場合は `window.siteConfig.get('key')` を使う。
- 法人名を文言に入れるときは、翻訳JSONに法人名を直接書かず `{company}` と書く（例: `"About {company}"`）。`/assets/js/i18n.js` が読み込み時に `companyName` の値へ置き換える。Offices の正式名称のように、設定に関係なく固定したい名前は直接書く。
- **注意:** 非表示はCSSで隠すだけなので、要素はHTMLソースに残る（開発者ツール等で見える）。また `site-config.js` 自体も公開ファイルなので、秘密情報は書かないこと。

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
3. 代替テキストは `data-i18n-attr-alt` で翻訳JSONの `imageAlt` キーを参照する（`/locales/en.json` と `/locales/ja.json` の両方に追加）。

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
- **テキストのみの更新**: `/locales/en.json` と `/locales/ja.json` を編集するだけで反映される。
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
   - 「View details / 詳細を見る」などのトグルボタンが正しく開閉すること
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
