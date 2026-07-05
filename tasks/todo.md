# 日本語コピー & 組版の自然化

## 方針
- 金額表記: **ドル建てのまま維持**（数値は変更せず、周辺表現のみ自然化）
- 対象: `ja/index.html`, `en/index.html`（style/head は同一構造）, `assets/js/i18n.js`, `locales/ja.json`

## Item 1: 日本語フォント + 行間
- [ ] Google Fonts に Noto Sans JP を追加読み込み
- [ ] `body` の font-family を `'Inter', 'Noto Sans JP', 'Hiragino Sans', ...` に
- [ ] `html[lang="ja"]` に line-height（本文1.8前後）を追加
- [ ] 見出し/サブタイトルに `font-feature-settings: 'palt'` + わずかな letter-spacing

## Item 2: 改行処理の是正
- [ ] `i18n.js` の `protectPunctuation`（読点前後のワードジョイナー）を削除
- [ ] `locales/ja.json` 内のハードコード `<br>` を撤去
- [ ] 見出し/サブタイトルに `text-wrap: balance` を適用

## Item 3: 文章リライト
- [ ] hero（タイトル/サブタイトル）
- [ ] about（mission/expertise、一気通貫の重複解消）
- [ ] services 各項目
- [ ] cases 各項目（レポート表現など）
- [ ] contact / privacy（並列崩れ修正）/ terms / footer
- [ ] 英数字前後スペースの統一

## Item 4: 金額表記
- [x] ユーザー判断 → ドル建て維持（対応不要）

## レビュー
- Item 1: `ja/`・`en/` 両HTMLに Noto Sans JP 読み込み、和文フォントスタック、`html[lang="ja"]` の palt/letter-spacing、`p`の行間1.85+`text-wrap:pretty`、見出しの`text-wrap:balance`を追加。
- Item 2: `i18n.js` の `protectPunctuation`（読点ワードジョイナー）を関数ごと削除し呼び出しを素の値に。JSON内の `<br>` 5箇所（hero/about×3/services）を撤去。キャッシュバスターを `?v=5` へ。
- Item 3: `ja.json` 全キーを見直し。「一気通貫」重複を解消（→ワンストップ/一貫して）、「伴走」を1回に集約、英数字前後スペースを「入れない」で統一、privacy.sharing の並列崩れを修正、フォームのプレースホルダを例示形式に。金額はドル建て維持。
- 検証: JSON妥当・`<br>`0件・U+2060残存なし・ローカル配信で反映確認済み。
- 実機確認（headless Chrome）: デスクトップ/モバイルで描画確認済み。フォント適用・コピー更新・BudouX折り返しOK。

## 追加修正: モバイルのヒーロー見出し見切れ（approach a）
- 事象: モバイル幅で2行目「テクノロジーで、未来をひらく」が右端で見切れ。
- 原因: `word-break: keep-all`（`html[lang="ja"]`）+ `sm:whitespace-nowrap` で、狭幅時に折り返し機会がなく溢れる。`<wbr>`（明示的break機会）も **Chromiumがkeep-all下で抑制** し効かなかった。
- 対応: prefix span と highlight span の間に `<br class="sm:hidden">` を挿入（`ja/index.html`）。モバイルは読点直後で強制改行→3行、`sm`以上(≥640px)は `display:none` で従来の2行を維持。
- `en/index.html` は元々問題の対象外のため wbr を除去して原状復帰（英語は空白で自然折り返し）。
- 検証: モバイル390pxで3行・見切れ解消、デスクトップ1440pxで2行維持を実描画で確認。
- 既知の未対応: **英語モバイルのヒーローも同種の見切れ（既存）**。今回は日本語スコープのため未修整。必要なら同手法で対応可能。
