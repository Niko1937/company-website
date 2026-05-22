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
│       └── i18n.js         言語切替ロジック（依存ライブラリなし）
├── images/                 静的画像（ロゴ等）
├── CNAME                   GitHub Pagesのカスタムドメイン設定
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
