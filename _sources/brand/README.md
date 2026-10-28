# Quests ブランド素材

Quests のロゴに関するファイルは、**すべてこのフォルダにあります**（ここが正本です）。
サイトで使うファイルだけ、`scripts/build_icons.py` がこのフォルダから公開場所へコピーします（下の表の「サイトでの配置」）。
このフォルダは `_` で始まるため、GitHub Pages のサイトでは公開されません（リポジトリ上では閲覧できます）。

---

## ロゴの意味

Quests のロゴマークは、頭文字「Q」をもとにした、円とひとつの角からなる形です。

| 形の要素 | 意味 |
|---|---|
| **全体の形 ＝ Q** | Quests の頭文字。そして「Quest（探求の旅）」 |
| **円** | 的であり、確かで完成された技術。**Big Tech Expertise** |
| **右下のひとつの角** | 矢じり。一点に向かう鋭さと速さ。**Startup Speed**。左上から右下へという、文章や時間が流れる方向（未来・前進）を指す |
| **中心の穴** | 実現したい理想。あえて塗りつぶさない「余白」で、お客様と一緒に描いていく未来を表す。中心にあるのは、お客様のビジネス |
| **4 : 2 : 1 の比率** | 外側の円・中心の穴・角の丸みの大きさが、2倍ずつの関係（2の累乗）でできた構造。デジタル（ビット）の論理に基づく、ぶれのない設計 |
| **継ぎ目のない一つの面** | 戦略から実装・運用まで、一つのチームで一貫して手がけること |

円と角の組み合わせは、会社のメッセージ「**Big Tech Expertise at Startup Speed**（ビッグテックの技術力 × スタートアップの速さ）」と対応しています。

**ブランドステートメント**

> 円は、ビッグテックで培った確かな技術。ひとつの鋭い角は、スタートアップの速さで一点に向かう意志。中心の余白は、お客様と共に描く理想です。Quests の「Q」は、その理想へ向かう旅の始まりを表しています。

> The circle stands for proven, Big Tech expertise. The single sharp corner is our drive to move with startup speed toward one point. The open center is the ideal we shape together with each client. Our "Q" marks the start of that quest.

---

## ファイル一覧

**資料・SNS 用**

| ファイル | 内容 | 主な用途 |
|---|---|---|
| `logo.svg` | 紺のマーク・背景透明（ベクター） | PowerPoint（Microsoft 365）、Keynote、Figma、印刷物。**最優先で使うファイル** |
| `logo-white.svg` | 白のマーク・背景透明（ベクター） | 暗い背景のスライド・資料 |
| `logo-navy-2048.png` | 紺のマーク・背景透明・2048×2048px | SVG を扱えないソフト（古い PowerPoint、Word、メールの署名など） |
| `logo-white-2048.png` | 白のマーク・背景透明・2048×2048px | 同上（暗い背景用） |
| `linkedin-logo-400.png` | 紺の背景に白のマーク・400×400px | **LinkedIn の会社ロゴ**（推奨サイズちょうど）。その他 SNS のアイコン |
| `linkedin-cover-1512x256.png`（`@2x` は 3024×512px） | Hero と同じ背景に、Hero と同じ2行の見出し「Pioneering the Future / with Big Tech Expertise at Startup Speed」・1512×256px | **LinkedIn の会社ページのカバー画像**（現在の推奨サイズ） |
| `linkedin-banner-ceo-1584x396.png`（`@2x` は 3168×792px） | 同じ背景に「Quests」と「Big Tech Expertise at Startup Speed」・1584×396px | **CEO の LinkedIn 個人ページの背景画像** |
| `/images/og/quests-1200x627.png`（サイト側に置く） | 同じ背景に「Quests」と「Big Tech Expertise at Startup Speed」・1200×627px | **リンクを共有したときの画像**（OGP 画像。LinkedIn・Slack・X など） |
| `linkedin-cover-1128x191.png` | Hero の背景を横に切っただけの文字なし版・1128×191px（旧推奨サイズ。`scripts/build_icons.py` が作る） | 文字なしのカバーにしたいとき |

**サイト用**（このフォルダが正本。サイトにはコピーを配置）

| ファイル | 内容 | サイトでの配置 |
|---|---|---|
| `favicon.svg` | ファビコン（ブラウザのダークモードでは白に切り替わる） | `/images/brand/favicon.svg` |
| `favicon.ico` | 旧ブラウザ用ファビコン（16/32/48px） | `/favicon.ico` |
| `apple-touch-icon.png` | iPhone のホーム画面用・180×180px | `/apple-touch-icon.png` |
| `icon-192.png` / `icon-512.png` | Android のホーム画面用（`/site.webmanifest` から参照） | `/images/brand/` |

`/favicon.ico` と `/apple-touch-icon.png` は、ブラウザがサイトのルートを直接探しに来るため、ルートに置いています。


---

## LinkedIn のバナーとリンク共有用の画像

`linkedin/banner.html` が元です（サイトと同じ Inter・同じグラデーション、背景は `_sources/photos/hero/background.jpg`）。文言や位置を変えたら、Chrome で PNG に書き出し直します（`#company` が会社ページ、`#ceo` が個人ページ）。

```sh
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --hide-scrollbars --virtual-time-budget=5000 --window-size=1512,256 --force-device-scale-factor=1 \
  --screenshot=_sources/brand/linkedin-cover-1512x256.png "file://$PWD/_sources/brand/linkedin/banner.html#company"
"$CHROME" --headless=new --hide-scrollbars --virtual-time-budget=5000 --window-size=1584,396 --force-device-scale-factor=1 \
  --screenshot=_sources/brand/linkedin-banner-ceo-1584x396.png "file://$PWD/_sources/brand/linkedin/banner.html#ceo"
```

リンク共有用の画像（OGP）は `#og` を 1200×627 で書き出し、サイトの `images/og/` に置きます。

```sh
"$CHROME" --headless=new --hide-scrollbars --virtual-time-budget=5000 --window-size=1200,627 --force-device-scale-factor=1 \
  --screenshot=images/og/quests-1200x627.png "file://$PWD/_sources/brand/linkedin/banner.html#og"
```

`@2x` 版は `--force-device-scale-factor=2` にして、ファイル名に `@2x` を付けます。どちらのサイズも LinkedIn にそのまま上げられます（比率が同じ。`@2x` は高解像度の画面でくっきり見える）。

**文字を置いてよい範囲**（LinkedIn のロゴ・顔写真と、スマホで切れる部分を避ける）

| | サイズ | 文字を置く範囲 | 避ける理由 |
|---|---|---|---|
| 会社ページ | 1512×256 | x 340〜1362、y 28〜200 | 左下に会社ロゴが重なる（x 45〜286、y 134〜下端）。スマホでは左右が約 8% 切れるとの説あり |
| 個人ページ | 1584×396 | x 420〜1164、y 60〜300 | PC では左下に顔写真（左 25%・下 45%）。スマホでは左右が最大 20% 切れ、顔写真が下の中央に来るとの説あり |

- サイズは LinkedIn ヘルプ（[会社ページ](https://www.linkedin.com/help/linkedin/answer/a563309)・[個人ページ](https://www.linkedin.com/help/linkedin/answer/a568217)）による。重なる位置は、LinkedIn 以外のガイドの計測値（ManyPixels ほか）を重ね合わせたもので、公式の数値ではない。上げた後は実際のスマホアプリでも確認する。
- サイトの URL は画像に入れない（クリックできないため）。個人ページの「連絡先情報 → ウェブサイト」に登録する。

---

## 仕様

**形状**（100単位の格子、マークは 10〜90 の範囲）

- 外側の円: 半径 40（中心 50, 50）
- 右下の角: 円の右下 1/4 を四角にし、角の丸みは半径 10
- 中心の穴: 半径 20

16px・32px に縮めても各寸法が整数ピクセルになるため、小さいサイズでも輪郭がくっきり出ます。

**色**

| 色 | 値 | 用途 |
|---|---|---|
| ネイビー | `#232F3E` | マークの基本色 |
| ホワイト | `#FFFFFF` | 暗い背景の上 |
| チャコール | `#1F1F1F` | サイトのヘッダー・Hero・フッターの背景 |

**使い方のルール**

- マークのまわりには、少なくとも**中心の穴の半径（マークの幅の 1/4）**の余白を空ける。
- 最小サイズは 16px（ファビコンの大きさ）。
- 単色で使う。グラデーション・影・縁取り・変形（縦横比の変更、回転）はしない。
- **社名「Quests」の文字の横にマークを並べない。** マークの Q と社名の Q が続いて「QQuests」のように見え、読みづらくなるため。マークは単独で（アイコン・ファビコン・資料の隅などに）使う。

---

## ファイルの作り直し

ロゴの形を変える場合は、このフォルダの `logo.svg`・`logo-white.svg`・`favicon.svg` を更新し、リポジトリのルートで次を実行します（Pillow が必要: `pip install pillow`）。

```bash
python3 scripts/build_icons.py
```

このフォルダの PNG / ICO がすべて作り直され、サイト用のファイルが公開場所へコピーされます。スクリプト内の寸法（`GEOMETRY`）も SVG と合わせてください。
**サイト側のコピーを直接編集しないこと**（次回の実行で上書きされます）。
