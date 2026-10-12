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

## 追加対応: Google Map の表示言語を UI 言語に連動
- [x] `locales/{en,ja}.json` に `contact.side.mapSrc`（埋め込みURLに `hl=en` / `hl=ja`）を追加
- [x] iframe に `data-i18n-attr-src="contact.side.mapSrc"` を付与（初期 `src` は各ページの言語で記述し、JS無効時も正しい言語）
- [x] `i18n.js`: 属性値が同じなら `setAttribute` しない（初期化時に iframe を二重読み込みしないため）。キャッシュバスター `?v=6`
- 検証（headless Chrome）: `/en/` → `hl=en`、`/ja/` → `hl=ja`、iframe の読み込みはどちらも1回。`/ja/` でページ内から English に切り替えると、リロードなしで `hl=en` に変わる。実描画で英語地図／日本語地図（「クラーク・キー」「マーライオン」等）になることを確認。

## 追加対応: 表示設定（site-config.js）の導入と Marshall 拠点の表示切替
- [x] `assets/js/site-config.js`（設定値）と `assets/js/config.js`（反映ロジック）を新設。`<head>` で同期読み込み
- [x] `data-show-if` / `data-hide-if` 属性で、要素ごとにJSを書かずに表示を切り替えられるようにした
- [x] Offices の Quests Ltd.（Marshall）行に `data-show-if="showMarshallOffice"`。既定値は `true`（現状維持）
- [x] README に「表示設定」節を追加
- 方針: CSSで隠す方式（非表示でもHTMLソースには残る）。地図の拡大は既存の `flex-1` に任せ、追加CSSなし。スマホの1列表示では地図の高さは変えない
- 検証（headless Chrome、`site-config.js` の応答を差し替えて実測）:
  - `true`: Marshall行が表示され、地図の高さは変更前と同じ（1440px: en 564px / ja 536px、390px: 362px）
  - `false`: Marshall行が `display:none`。1440px で地図が en 564→656px（行72px＋gap20px）、ja 536→645px（行89px＋gap20px）に広がり、カードの下端はフォームの下端と一致。390px では地図は362pxのまま、カードだけ短くなる。ページ内で言語を切り替えても非表示のまま
  - `site-config.js` が404: Marshall行は非表示になり、JSエラーなし
  - en/ja HTML の差分は既存の4か所のまま

## 英語コピーの改善（簡潔さ・訴求力）
- [x] `<title>` とナビは変更しない（ナビは大手IT企業を参考に別途提案）
- [x] Hero: 1行目 "Pioneering the Future" / 2行目 "with Big-Tech Expertise and Startup Speed"（"Big-Tech Expertise"〜"Startup Speed" に1本のグラデーション、"with" と "and" は白）/ サブはユーザー指定の文言 / Scroll → "Explore"
- [x] About: サブ、Why Quests、What We Bring（クラウド認定・特許を持つエンジニアがいることを訴求）
- [x] Services: サブ、4サービスのタイトル・説明・詳細・箇条書き
- [x] Case Studies: サブ、フィルタ "All"、"Tech Stack"、6事例を「結果から書く」型に
- [x] Contact: 見出し、サブ、フォームのラベル・プレースホルダ、送信ボタン "Continue to Email"
- [x] Privacy: "Opt out of marketing"（文法の修正のみ）/ Footer: タグライン、コピーライトのピリオド
- [x] HTML内のフォールバック文言（英語）も en.json に合わせる（JSON読み込み前に旧文言が一瞬見えるのを防ぐ）
- [x] 日本語（ja.json）は変更しない
- [x] 検証: 各画面幅でHeroが見切れないこと、en/ja の表示、JSONの妥当性

## レビュー（英語コピー）
- `locales/en.json` の全セクションを改訂（`<title>`・ナビ・`ja.json` は変更なし）。About にクラウド認定・特許を持つエンジニアがいることを追記。
- Hero: `hero.titleHighlight` を `data-i18n-html` に変更し、`Big-Tech Expertise <span class="text-white">and</span> Startup Speed` で1本のグラデーション＋白い "and" を実現。
- Hero の折り返し: 2行目が長くなり、`sm:whitespace-nowrap` のせいで 640〜1279px で画面外にはみ出した。`.hero-line2` に変更し、英語は `text-wrap: balance` で折り返し、日本語は従来どおり ≥640px で nowrap（`html[lang="ja"]` で切替、ページ内の言語切替にも追従）。1024〜1279px は3行になり "Explore" に接するため、見出しを `lg:text-6xl` → `xl:text-6xl`（lg は 5xl）に変更。
- HTML内の英語フォールバック文言を en.json と一致させた（en/ja 各161か所、差分チェックで一致を確認）。
- 検証（headless Chrome）: 英語 360/390/640/768/1024/1280/1440px で横はみ出しなし、Hero は "with Big-Tech Expertise / and Startup Speed" の2行（モバイルは3行）、サブと "Explore" の重なりなし。日本語の Hero は変更前と同じ行数・位置。Services/Cases/Contact の表示崩れなし、JSエラーなし。

## 追加対応: ナビ（案A）
- [x] PC: Services · Case Studies · About ｜ 言語切替 ｜ [Contact us]（白いボタン、`.nav-cta`）
- [x] 英語ラベル: "About Us" → "About"、"Contact Us" → "Contact us"（日本語ラベルは変更なし、並び順のみ変更）
- [x] スマホのメニューとフッターのクイックリンクも同じ順にし、スマホのメニューの Contact は全幅の青いボタンにした
- 検証（headless Chrome）: en/ja × 1440/1024px で並びと右端の揃い、スクロール前後の見た目、ボタンで #contact へスクロールすることを確認。390px でメニューの並び、Contact ボタンでメニューが閉じてスクロールすること、フッターの並びを確認。JSエラーなし。

## 追加修正: Contact を元に戻す / 英語 Hero を2行に
- [x] Contact はボタンをやめ、元のテキストリンク "Contact Us"（日本語「お問い合わせ」）に戻した。並びは Services · Case Studies · About · Contact Us ｜ 言語切替。スマホのメニュー・フッターも元のスタイルに戻した
- [x] 英語の Hero（1024px以上）: 見出しの範囲をコンテナの幅いっぱいにし、2行目を折り返さないようにした。文字サイズは lg 44px / xl 以上 56px（コンテナ幅が段階的に変わるため、画面幅ではなく段階で指定）。1023px以下と日本語は従来どおり
- 検証: en 1920/1536/1440/1280/1279/1024px で2行・はみ出しなし（1024px の右端は 943px、1440px は 1273px で、いずれもコンテナ内）。768px 以下は従来どおり折り返し。ja は変更前と同じ。ja ページから英語に切り替えても2行になる
- [x] Hero 2行目のつなぎを "and" → "at" に変更（"with Big-Tech Expertise at Startup Speed"）。1440px・1024px で2行のまま、はみ出しなし
- [x] 英語 Hero のサブを、PC幅（1024px以上）で2行にした（`max-width: 56rem` + `text-wrap: balance`、`html[lang="en"]` のみ）。1920/1440/1280/1024px で2行、768px 以下と日本語は従来どおり

## 日本語コピーの刷新（英語版の改訂に合わせる）と改行処理の見直し
- [x] Hero: 案B（「未来を切りひらく」/「ビッグテックの技術力 × スタートアップの速さ」、2つのキーワードにグラデーション、× は白）、サブ、スクロール表示
- [x] Hero のレイアウト: 日本語も PC 幅で2行に収まるようにする（英語と同じ考え方で、言語ごとに文字サイズを指定）。モバイル用の `<br class="sm:hidden">` を撤去（2行目の先頭に空行ができるため）
- [x] About: サブ・本文1はユーザー指定の文言、見出し1「Questsを選ぶ理由」、本文2は提案どおり
- [x] Services: サブ、タイトル、短い説明（開発はユーザー指定の文言）、詳細、箇条書き
- [x] 導入事例: サブ、フィルタ（AI活用 / データ分析 / システム刷新）、「解決策」、6事例を数字から書く型に
- [x] お問い合わせ: サブ、フォーム見出し、全角コロンのプレースホルダ（ご相談内容の例は既存のまま）、同意、送信ボタン
- [x] フッター: タグライン、「メニュー」
- [x] 改行: 文節改行（BudouX + keep-all）は見出しとリード文（`data-phrase`）だけにし、本文・箇条書きは通常の組み方（禁則あり）に戻す
- [x] 検証: PC/スマホで描画確認（本文の右端、箇条書きの折り返し、Hero の行数、はみ出し）、英語版に影響がないこと

## レビュー（日本語コピー・改行）
- `locales/ja.json` を英語版の改訂に合わせて全面更新。ユーザー指定の文言（About のサブと本文1、開発の短い説明）を反映し、ご相談内容の例は既存のまま。「——」は0件、プレースホルダの「例：」は全角に統一。キーの構成は en.json と一致。
- 改行: `i18n.js` で BudouX を適用する範囲を `h1–h4` と `[data-phrase]`（Hero のサブ、各セクションのリード文、お問い合わせのサブ、フッターのタグライン）に限定。CSS の `word-break: keep-all` も同じ範囲に限定し、本文と箇条書きは通常の組み方（`line-break: strict` の禁則つき）に戻した。キャッシュバスターは `?v=7`。
- Hero: 日本語は2行目が長いため、PC幅のレイアウト（見出しの範囲を広げる、2行目は折り返さない、サブは最大 56rem で2行）を日英共通にし、文字サイズだけ言語別に指定（ja: lg 40px / xl 52px、en: lg 44px / xl 56px）。`.hero-copy` の幅指定が Tailwind の `lg:w-3/5` に負けていたため、セレクタに `html` を付けて優先度を上げた。モバイル用の `<br class="sm:hidden">` は撤去し、en/ja の HTML の差分はページ固有の3か所だけになった。
- 検証（headless Chrome）: ja 360〜1920px の9つの幅で横はみ出しなし。Hero は 1024px以上で2行、768px以下は3行。サブは 1024px以上で2行。本文の右端がそろい、箇条書きはすべて1行に収まることを PC/スマホで確認。英語版の Hero・サブは変更前と同じ値。ページ内の言語切り替え（ja→en、en→ja）でも同じ結果。JSエラーなし。

## 追加修正: 日本語の文言（ユーザーの修正＋提案の反映）
- [x] ja: Hero サブ・強みの「等」→「など」、About サブ「シニアメンバーがプロジェクトに参画し、成果にこだわって支援します」、強みの本文を改稿（BIG4などのコンサルティングファーム出身、認定資格・特許、戦略から実装まで、変革まで伴走）、箇条書きの表記を統一（デジタル戦略策定 / 業務プロセス改善 / 組織変革支援 / 技術選定 / ITアーキテクチャ診断 の順。クラウドネイティブな実装、レガシーシステム刷新、クラウドインフラ管理、ナレッジトランスファー）、お問い合わせ「担当者からすぐにご返信いたします」
- [x] en: "What We Bring" を日本語に合わせて改稿（Big Four 出身のコンサルタント、変革まで伴走）、戦略・コンサルティングの箇条書きを日本語と同じ並びに
- [x] Services のカード: 1024〜1279px は2列に（`lg:grid-cols-4` → `xl:grid-cols-4`）。4列で折り返していた英語の箇条書き2つを短縮（Cloud infrastructure / Documentation & standards）
- 検証: ja/en × 390〜1536px の7つの幅で、箇条書きがすべて1行・横はみ出しなし・JSエラーなし。About と Services を PC 幅で描画確認
- [x] ja「私たちの強み」から「主要クラウドの認定資格や特許を持つエンジニアも所属しています。」を削除（ユーザー指示）
- [x] en "What We Bring" から "Our team includes cloud-certified engineers and patent holders." を削除（JSON と HTML のフォールバック）

## LP写真の再生成と差し替え
- [x] 生成スクリプト・候補画像はリポジトリ外（scratchpad）に置く。キーは `../Questia/.env` から実行時にメモリへ読み込むだけで、表示・保存しない
- [x] `.gitignore` に `.env` / `.env.*` を追加
- [x] 12枠 × 4パターン（方向性A×2 + B×2）を gpt-image-1.5（high, 1536x1024）で生成
- [x] 比較ギャラリーでユーザーが選択
- [x] 採用画像を JPEG 化して `images/photos/` に配置、en/ja の img src と Hero 背景を差し替え、README 更新
- [x] 検証: 全画像の読み込み、readdy.ai 参照0件、キー文字列がステージ内容に含まれないこと

## レビュー（LP写真）
- 画像生成 API（共有ゲートウェイ）は `/images/edits` を許可していなかったため、修正はすべて構図を細かく指定した新規生成で対応。6回のやり取りで計112枚を生成し、ユーザーが12枚を選定。
- 採用: hero-R3 / about-V3 / consulting-R4 / system-A2 / operations-S2 / training-R1 / material-B2 / chatbot-B2 / predictive-S2 / dashboard-A1 / voice-U1 / legacy-S4。
- `images/photos/<枠名>.jpg` に配置（カード・About は 1200×800、Hero は 1536×1024、JPEG 品質78、合計約2.4MB）。en/ja の HTML の readdy.ai の URL 12か所を置き換え（外部参照0件）。
- 検証（headless Chrome）: ja/en × 1440px・en × 390px で全11枚の img と Hero 背景が読み込まれ、readdy.ai への通信は0件、JSエラーなし。カードでの切り抜き（上寄せ）で、人物の顔や店内ナビのスマホが切れていないことを確認。
- 秘密情報: 生成スクリプト・候補画像はリポジトリ外。キー文字列はリポジトリ・一時フォルダとも0件。

## 追加対応: 画像の配置整理と配信の最適化
- [x] `images/` をセクション別に整理（brand / hero / about / services / cases）。ファイル名は翻訳JSONのキーと一致。ロゴは `brand/logo.svg`（ファビコンのパスを3ファイルで更新）
- [x] `scripts/optimize_images.py`（Pillow）で JPEG + WebP、600px / 1200px を生成。元の PNG から直接変換
- [x] `<picture>` + `srcset` / `sizes`、`width` / `height`、`loading="lazy"`（About 以外）、`decoding="async"`
- [x] Hero 背景を CSS の `image-set()`（WebP 優先、JPEG フォールバック）に変更し、インラインスタイルを撤去
- [x] 代替テキストを `imageAlt` キーで多言語化（`data-i18n-attr-alt`）
- [x] README に「画像の管理」節を追加
- 検証（headless Chrome）: ja 1440px（1x）/ en 1440px（2x）/ en 390px（3x）で全11枚が表示、等倍ではサービスに 600px の WebP、Retina では 1200px が選ばれる。Hero は WebP を読み込み。alt が言語に追従、ファビコン 200、旧 `images/photos/` への参照0件、JSエラーなし、レイアウトは変更前と同じ
- [x] 元画像を `_sources/photos/`（`_` 始まりで Pages 非公開）に、生成時の解像度 1536×1024 のまま品質95の JPEG で保存（12枚・約5.8MB）。生成プロンプトを `prompts.md` に記録（秘密情報なし）。README の手順も元画像起点に更新

## ロゴの刷新（C5 Drop）
- [x] 6案 → B/C のバリエーション → B1/C5 のバリエーションを提示し、ユーザーが C5（外径の半径40・角10・穴20 = 4:2:1）を選定。黄金比版（穴15.3/24.7・角9.4）とも比較し、C5 を維持
- [x] `images/brand/logo.svg` / `logo-white.svg` を新ロゴに置き換え（viewBox を 10..90 に切り詰め）、ダークモード対応の `favicon.svg` を追加
- [x] `scripts/build_icons.py`（Pillow で描画）で `favicon.ico`（16/32/48）・`apple-touch-icon.png`（180）・`icon-192/512.png` を生成。`site.webmanifest` を追加し、3つの HTML の head を更新
- 検証: 全アイコンが 200 で配信、マニフェストは JSON として正しい。プレビューで 16px・32px の輪郭、iOS の角丸・Android の円形マスク内に収まること、ダークモードのタブでの白版を確認
- [x] ヘッダー・フッターにマークを付けたが、マークと「Quests」の Q が似ていて社名が読みづらいため、ユーザーの判断で取り下げ（元の文字だけの表示に戻した）。ロゴはファビコン・アプリアイコンでのみ使用

## 文章から「AIっぽさ」を除く
- [x] エムダッシュを全廃（英語の文章7か所、日本語タイトル、地図の title 属性）
- [x] en: About サブ、強みの最終文（truly / don't stop at）、サービスのリード（journey＋コロン）、開発の短い説明・詳細、事例のリード、Hero サブの断片、"Big-Tech" → "Big Tech" に統一
- [x] ja: 事例のリード（「〜へ。」の重複）、運用の短い説明（3語の並び）、強みの最終文（からこそ／伴走）、開発の詳細と Questsの設立の一文（ユーザー指定の文言）、著作権表示のピリオド
- 検証: HTML の英語フォールバックと en.json の不一致0件。Hero の見出し・サブは en/ja とも 1024px 以上で2行、はみ出しなし
- [x] en のフォームの入力例を日本語版に合わせた（John Doe / you@example.com / Quests Ltd.）

## ブランド素材一式
- [x] `_sources/brand/` に、ロゴ SVG（紺・白）、背景透明の 2048px PNG（紺・白）、LinkedIn 用ロゴ 400×400、LinkedIn カバー 1128×191（Hero 背景の中央の帯）を配置
- [x] ロゴの意味・ファイル一覧・仕様（寸法・色）・使い方のルール（余白、最小サイズ、社名の横に並べない）を `_sources/brand/README.md` に記載
- [x] `scripts/build_icons.py` から一式を作り直せるようにした
- Hero 背景は検討の結果、現状（hero-R3）を維持
- [x] ロゴ関連の全ファイルを `_sources/brand/` に集約（正本）。サイトで使わない `images/brand/logo.svg` / `logo-white.svg` を削除し、サイトで使う5ファイルだけを `build_icons.py` がコピーして公開する形に変更。READMEも更新
