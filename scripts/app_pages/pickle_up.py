# The pickle-up pages' text and settings (build.py turns them into /ja|en/apps/pickle-up/...).
# Store links: None until the app is out; the badge then shows without a link and "coming soon" beside it.

SLUG = 'pickle-up'
NAME = 'pickle-up'
STORES = {
    # e.g. 'https://apps.apple.com/app/id0000000000'
    'appStore': None,
    # 'https://play.google.com/store/apps/details?id=com.it.quests.pickleup'
    'googlePlay': None,
}
UPDATED = {'ja': '2026年11月11日', 'en': 'November 11, 2026'}

# Screens (images/apps/pickle-up/screens/<name>.webp), each 1206 x 2622 (iPhone, @3x), shown at 300 px wide.
SCREEN_SIZE = (1206, 2622)

JA = {
    'lang': 'ja',
    'title': 'pickle-up | ピックルボールの試合を撮って、自分の打球を振り返る',
    'description': 'コートの後ろにスマホを置いて試合を撮るだけ。ラリーと得点を自動で区切り、あなたの打球がどこへ、どれくらいの高さで飛んだかをコートの図で振り返れるアプリです。',
    'nav': {'features': '機能', 'how': '使い方', 'faq': 'よくある質問', 'support': 'サポート', 'download': 'ダウンロード', 'menu': 'メニュー'},
    'langSwitch': '言語を切り替える',
    'soon': '近日公開',
    'storeAlt': {'appStore': 'App Store からダウンロード', 'googlePlay': 'Google Play で手に入れよう'},
    'hero': {
        'eyebrow': 'ピックルボールの試合分析アプリ',
        'title': ['撮るだけで、', '自分の打球が', '見えてくる。'],
        'lead': 'コートの後ろにスマホを置いて、試合を撮るだけ。ラリーと得点を自動で区切り、あなたの打球がどこへ、どれくらいの高さで飛んだかを、コートの図で振り返れます。',
        'screenAlt': '分析タブ。自分の打球の軌道を、立体のコートに重ねて表示している',
    },
    'features': {
        'eyebrow': '機能',
        'title': '試合を撮ったら、|あとは|アプリに|おまかせ',
        'items': [
            {
                'screen': 'record',
                'title': '置いて|撮るだけ。|区切りも|得点も|自動で',
                'body': 'ラリーの始まりと終わり、得点、試合か練習かを自動で判定します。スコアの読み上げにも対応しているので、プレーに集中できます。',
                'points': ['ラリーを自動で区切る', '得点を数えて読み上げる', '試合か練習かを自動で判定'],
                'alt': '録画タブ。撮影をはじめるボタンと、スコアの読み上げ・得点方式の設定',
            },
            {
                'screen': 'analysis-flat',
                'title': 'あなたの|打球を、|コートの|図に',
                'body': '動画の中で自分を1回タップするだけ。打った位置から、相手のコートのどこに落ちたかまでを線で描きます。週や月でまとめれば、狙いのくせが見えてきます。',
                'points': ['打った位置と着地点', 'イン・アウト・ボレーで絞り込み', '週・月・試合・ラリーごとに'],
                'alt': '分析タブ。自分の打球を、上から見たコートに線で重ねて表示している',
            },
            {
                'screen': 'analysis-3d',
                'title': '高さは|立体で。|指で|回して|確かめる',
                'body': '打球の軌道を立体で描き、ネットから何cm上を通ったかも推定します。ディンクが浮いていないか、ドライブが低く通っているかを、数字で確かめられます。',
                'points': ['軌道の高さを立体で表示', 'ネットからの高さ（中央値）', '回転・拡大で好きな角度に'],
                'alt': '分析タブの立体表示。打球の軌道と、ネットからの高さの中央値',
            },
            {
                'screen': 'home',
                'title': '練習の|積み重ねが、|ひと目で',
                'body': '毎日の練習時間を、週や月のグラフで見られます。手で記録した練習も、撮影した試合もまとめて集計します。',
                'points': ['週・月の練習時間のグラフ', '練習した日をカレンダーに', '練習の記録とリマインダー'],
                'alt': 'ホーム。週の練習時間の棒グラフと、練習した日数',
            },
        ],
    },
    'privacy': {
        'eyebrow': 'プライバシー',
        'title': '動画は、|あなたの|スマホの|中だけに',
        'lead': '撮った動画の解析は、すべてスマホの中で行います。動画や解析結果を、私たちのサーバーに送ることはありません。',
        'items': [
            ('ri-smartphone-line', 'スマホの中で解析', '骨格やボールの検出も、打球の計算も、通信せずに端末だけで行います。'),
            ('ri-lock-line', '動画は外に出ない', '動画はアプリ専用の場所に保存します。共有するのは、あなたが選んだときだけです。'),
            ('ri-user-unfollow-line', '登録なしで使える', 'アカウントを作らずに、すぐに使いはじめられます。'),
        ],
        'link': 'プライバシーポリシーを読む',
    },
    'how': {
        'eyebrow': '使い方',
        'title': '3ステップで、|次の|試合から',
        'steps': [
            ('コートの後ろに置く', 'ベースラインの後ろの、なるべく高い位置にスマホを置きます。コートの四隅と、手前でサーブを待つ人まで入れば準備完了です。'),
            ('試合を撮る', '「撮影をはじめる」を押して、いつもどおりプレーします。'),
            ('打球を振り返る', '分析タブで、試合ごと・ラリーごとに自分の打球を確かめます。'),
        ],
    },
    'faq': {
        'eyebrow': 'よくある質問',
        'title': 'よくある質問',
        'items': [
            ('どんな撮り方が必要ですか？', 'コートの後ろから、コートの四隅と手前のサーバーまで入るように撮ってください。アプリの「撮影のしかた」で、置き方の図を見られます。'),
            ('撮った動画はどこに保存されますか？', 'スマホの中の、アプリ専用の場所に保存します。私たちのサーバーには送りません。'),
            ('分析はどれくらい正確ですか？', 'スマホ1台の映像から推定するため、奥のコートの着地点や球の高さには誤差があります。判定に十分な確かさがない打球は図に描かず、「判定不能」として数えます。'),
            ('対応している機種は？', 'iPhone 版と Android 版を準備しています。公開したら、このページでお知らせします。'),
        ],
        'more': 'サポートページを見る',
    },
    'cta': {'title': '次の|試合を、|撮ってみませんか。', 'lead': 'スマホを置いて撮るだけで、自分の打球が見えてきます。'},
    'footer': {
        'tagline': 'ピックルボールの試合を撮って、自分の打球を振り返るアプリ',
        'app': 'アプリ',
        'company': '開発元',
        'links': {'features': '機能', 'support': 'サポート', 'privacy': 'プライバシーポリシー'},
        'companyLinks': {'home': 'Quests について', 'apps': 'Quests のアプリ', 'contact': 'お問い合わせ'},
        'by': 'pickle-up は Quests Bay Pte. Ltd. が開発・運営しています。',
        'trademarks': 'Apple および Apple ロゴは、米国その他の国で登録された Apple Inc. の商標です。App Store は Apple Inc. のサービスマークです。Google Play および Google Play ロゴは Google LLC の商標です。',
    },
    'support': {
        'title': 'サポート | pickle-up',
        'description': 'pickle-up の使い方、よくある質問、お問い合わせ先。',
        'eyebrow': 'サポート',
        'h1': 'pickle-up のサポート',
        'lead': '使い方で困ったときは、まず下のよくある質問をご覧ください。解決しないときは、お問い合わせフォームからご連絡ください。',
        'groups': [
            ('撮影', [
                ('スマホはどこに置けばよいですか？', 'ベースラインの後ろの、なるべく高い位置に置いてください。コートの四隅と、手前のラインの後ろでサーブを待つ人まで入るように、少し広めに映します。三脚やフェンスに付けるホルダーが便利です。'),
                ('前（ネット側）から撮れますか？', '打球がスマホに当たるおそれがあるため、後ろか横から撮ってください。分析はコートの後ろから撮った動画を前提にしています。'),
                ('試合か練習かは選ぶ必要がありますか？', '選ぶ必要はありません。撮った動画から自動で判定します。違っていたら、動画の画面で直せます。'),
            ]),
            ('分析', [
                ('自分の打球を出すには？', '試合の動画を開き、「自分」から、全員が映った場面で自分の四角をタップします。ラリーごとに打球を取り出し、分析タブに表示します。'),
                ('「判定不能」とは何ですか？', '着地点やイン・アウトを判断できるほど確かでない打球です。図には描かず、本数だけを数えます。'),
                ('ネットからの高さはどう測っていますか？', '映像から打球の軌道を立体で推定し、ネットの真上を通った位置で、球の下端からネットの上端までの高さを出しています。ネットにかかった球は、ネットに当たった位置の高さをマイナスで表します。'),
                ('コートの位置がずれています', '動画の画面の「コートの位置」から、四隅の位置を直せます。直した位置で分析し直します。'),
            ]),
            ('データ', [
                ('動画はサーバーに送られますか？', '送りません。動画も解析結果も、スマホの中のアプリ専用の場所に保存します。'),
                ('データを消すには？', '動画ごとに動画の画面から削除できます。すべて消すときは、マイページの「すべてのデータを削除」を使ってください。写真アプリに保存した動画は残ります。'),
                ('機種変更したときは？', '今の版では、データは端末の中だけにあり、新しい端末には引き継がれません。残したい動画は、写真アプリに保存してください。'),
            ]),
        ],
        'contactTitle': 'お問い合わせ',
        'contactBody': 'お問い合わせフォームからご連絡ください。お使いの機種、OS のバージョン、アプリのバージョン（マイページの「バージョン」）を書いていただくと、早くお答えできます。',
        'contactLink': 'お問い合わせフォームへ',
    },
    'privacyPage': {
        'title': 'プライバシーポリシー | pickle-up',
        'description': 'pickle-up における情報の取り扱いについて。',
        'eyebrow': 'pickle-up',
        'h1': 'プライバシーポリシー',
        'updated': '最終更新日',
        'lead': 'Quests Bay Pte. Ltd.（以下「当社」）は、スマートフォン向けアプリ「pickle-up」（以下「本アプリ」）で扱う情報について、以下のとおり定めます。当社全体の個人情報の取り扱いは、<a href="/ja/privacy/">当社のプライバシーポリシー</a>をご覧ください。',
        'sections': [
            ('summary', '1. 要点', '''<ul>
<li>本アプリで撮影した動画と、その解析結果は、お使いのスマートフォンの中だけに保存します。</li>
<li>当社は、これらの動画や解析結果を受け取りません。本アプリは、当社のサーバーとの通信を行いません。</li>
<li>本アプリには、広告や行動分析のための外部のツールを組み込んでいません。</li>
</ul>'''),
            ('data', '2. 本アプリが扱う情報', '''<p>本アプリは、次の情報を、お使いのスマートフォンの中の本アプリ専用の領域に保存します。</p>
<ul>
<li>撮影した動画と、その音声</li>
<li>動画の解析結果（人の姿勢の推定、ボールの位置、ラリーの区切り、得点、打球の位置や高さなど）</li>
<li>練習の記録、メモ、最初に入力していただいたプロフィール、アプリの設定</li>
</ul>
<p>解析はすべて端末の中で行い、通信は行いません。解析では、選手を見分けるために、映っている人の位置や服の色を使いますが、顔を認識したり、個人を特定したりはしません。</p>'''),
            ('permissions', '3. 端末の機能へのアクセス', '''<div class="table-wrap"><table>
<tr><th>カメラ</th><td>試合や練習を撮影するため</td></tr>
<tr><th>マイク</th><td>動画に音声を記録するため</td></tr>
<tr><th>写真</th><td>アプリの外で撮った動画を取り込むため、またお客様が選んだ動画を写真アプリに保存するため</td></tr>
<tr><th>通知</th><td>お客様が設定した練習のリマインダーを、端末の中から通知するため</td></tr>
</table></div>
<p>いずれも、お客様が許可した場合にだけ使います。許可は、端末の設定アプリからいつでも変更できます。</p>'''),
            ('people', '4. 映っている方について', '''<p>動画には、一緒にプレーする方や周りの方が映ることがあります。撮影する前に、映る方の了承を得てください。動画を共有するときも同様です。</p>'''),
            ('sharing', '5. 共有と第三者への提供', '''<p>動画の共有や写真アプリへの保存は、お客様が操作したときにだけ、お客様が選んだ先に対して行います。当社が、本アプリの情報を第三者に提供することはありません。</p>
<p>本アプリのダウンロードや更新の際に、Apple Inc. または Google LLC が取得する情報は、それぞれのプライバシーポリシーに従って扱われます。</p>'''),
            ('delete', '6. 情報の削除', '''<p>動画は、動画の画面からいつでも削除できます。マイページの「すべてのデータを削除」で、本アプリが保存したすべての情報を削除できます。本アプリを端末から削除した場合も、本アプリ専用の領域の情報は削除されます。ただし、写真アプリに保存した動画は残ります。</p>'''),
            ('children', '7. お子さまの利用', '''<p>本アプリは、お子さまから当社が情報を受け取る仕組みを持ちません。保護者の方の判断のもとでご利用ください。</p>'''),
            ('changes', '8. 本ポリシーの変更', '''<p>ログインや AI によるアドバイスなど、情報の扱いが変わる機能を追加するときは、その前に本ポリシーを改定し、本アプリとこのページでお知らせします。</p>'''),
            ('contact', '9. お問い合わせ', '''<div class="contact"><p>Quests Bay Pte. Ltd.<br>68 Circular Road, #02-01, Singapore 049422（シンガポール）<br><a href="/ja/#contact">お問い合わせフォーム</a></p></div>'''),
        ],
    },
}

EN = {
    'lang': 'en',
    'title': 'pickle-up | Film your pickleball games and see every shot you hit',
    'description': 'Set your phone behind the court and film the game. pickle-up splits the rallies, keeps the score, and shows where and how high every shot you hit went, on a picture of the court.',
    'nav': {'features': 'Features', 'how': 'How it works', 'faq': 'FAQ', 'support': 'Support', 'download': 'Download', 'menu': 'Menu'},
    'langSwitch': 'Change language',
    'soon': 'Coming soon',
    'storeAlt': {'appStore': 'Download on the App Store', 'googlePlay': 'Get it on Google Play'},
    'hero': {
        'eyebrow': 'Pickleball match analysis',
        'title': ['Film the game.', 'See every shot', 'you hit.'],
        'lead': 'Set your phone behind the court and play. pickle-up splits the rallies and keeps the score, then shows where and how high each of your shots went, on a picture of the court.',
        'screenAlt': 'The Insights tab, with your shots drawn on the court in 3D',
    },
    'features': {
        'eyebrow': 'Features',
        'title': 'Film the match. The app does the rest.',
        'items': [
            {
                'screen': 'record',
                'title': 'Set it up and play. Rallies and score, automatic.',
                'body': 'pickle-up finds where each rally starts and ends, keeps the score, and tells a match from practice. It can call the score out loud, so you can keep your eyes on the ball.',
                'points': ['Splits the rallies for you', 'Keeps and calls the score', 'Tells matches from practice'],
                'alt': 'The Record tab, with the start button and the score calling and scoring settings',
            },
            {
                'screen': 'analysis-flat',
                'title': 'Your shots, on the court',
                'body': 'Tap yourself once in the video. Each shot you hit is drawn from where you hit it to where it landed on the other side. Look over a week or a month and your patterns show.',
                'points': ['Where you hit and where it landed', 'Filter by in, out and volleys', 'By week, month, match or rally'],
                'alt': 'The Insights tab, with your shots drawn on the court from above',
            },
            {
                'screen': 'analysis-3d',
                'title': 'See the height in 3D. Turn it with a finger.',
                'body': 'Shots are drawn in 3D, with an estimate of how far above the net each one passed. Check whether your dinks float or your drives stay low, in centimetres.',
                'points': ['Shot height in 3D', 'Height from the net (median)', 'Turn and zoom to any angle'],
                'alt': 'The Insights tab in 3D, with the shots and the median height from the net',
            },
            {
                'screen': 'home',
                'title': 'Your practice, at a glance',
                'body': 'See the time you practised each day, by week or by month. Practice you log by hand and matches you film are counted together.',
                'points': ['Practice time by week and month', 'The days you played, on a calendar', 'Practice log and reminders'],
                'alt': 'The Home tab, with a bar chart of the week’s practice time',
            },
        ],
    },
    'privacy': {
        'eyebrow': 'Privacy',
        'title': 'Your videos stay on your phone',
        'lead': 'Every video is analysed on your phone. Neither your videos nor the results are ever sent to our servers.',
        'items': [
            ('ri-smartphone-line', 'Analysed on your phone', 'Finding players and the ball, and working out every shot, happens on the device, offline.'),
            ('ri-lock-line', 'Videos never leave it', 'Videos are kept in the app’s own storage. They are shared only when you choose to.'),
            ('ri-user-unfollow-line', 'No sign-up', 'Start right away, no account needed.'),
        ],
        'link': 'Read the privacy policy',
    },
    'how': {
        'eyebrow': 'How it works',
        'title': 'Three steps, starting with your next match',
        'steps': [
            ('Set it behind the court', 'Put your phone behind the baseline, as high as you can. Once all four corners and the server waiting behind the near line are in view, you are ready.'),
            ('Film the match', 'Tap Start recording and play as usual.'),
            ('Look back at your shots', 'Open the Insights tab to go through your shots, match by match and rally by rally.'),
        ],
    },
    'faq': {
        'eyebrow': 'FAQ',
        'title': 'Frequently asked questions',
        'items': [
            ('How should I film?', 'From behind the court, with all four corners and the server on the near side in view. The app’s filming guide shows where to put your phone.'),
            ('Where are my videos kept?', 'In the app’s own storage on your phone. We never upload them.'),
            ('How accurate is the analysis?', 'Everything is estimated from a single phone’s video, so landings on the far side and ball heights have some error. Shots that cannot be judged with enough certainty are not drawn; they are counted as unclear.'),
            ('Which phones does it run on?', 'Versions for iPhone and Android are on the way. We will announce them on this page.'),
        ],
        'more': 'Visit the support page',
    },
    'cta': {'title': 'Film your next match.', 'lead': 'Set your phone down, play, and see every shot you hit.'},
    'footer': {
        'tagline': 'Film your pickleball games and see every shot you hit.',
        'app': 'App',
        'company': 'Made by',
        'links': {'features': 'Features', 'support': 'Support', 'privacy': 'Privacy policy'},
        'companyLinks': {'home': 'About Quests', 'apps': 'Apps by Quests', 'contact': 'Contact'},
        'by': 'pickle-up is built and run by Quests Bay Pte. Ltd.',
        'trademarks': 'Apple and the Apple logo are trademarks of Apple Inc., registered in the U.S. and other countries. App Store is a service mark of Apple Inc. Google Play and the Google Play logo are trademarks of Google LLC.',
    },
    'support': {
        'title': 'Support | pickle-up',
        'description': 'How to use pickle-up, answers to common questions, and how to reach us.',
        'eyebrow': 'Support',
        'h1': 'pickle-up support',
        'lead': 'If something is not working as you expect, start with the questions below. If they do not help, send us a message through the contact form.',
        'groups': [
            ('Filming', [
                ('Where should I put my phone?', 'Behind the baseline, as high as you can. Frame it a little wide, so all four corners and the player waiting to serve behind the near line are in view. A tripod or a fence mount helps.'),
                ('Can I film from the front, by the net?', 'Please film from behind or from the side: a shot could hit your phone. The analysis expects video taken from behind the court.'),
                ('Do I need to say whether it is a match or practice?', 'No. The app works it out from the video. If it gets it wrong, you can change it on the video’s screen.'),
            ]),
            ('Analysis', [
                ('How do I see my own shots?', 'Open the match’s video, choose You, and tap your box in a frame where everyone is in view. Your shots are found rally by rally and shown in the Insights tab.'),
                ('What does “unclear” mean?', 'A shot whose landing, or whether it was in or out, cannot be judged with enough certainty. It is counted but not drawn.'),
                ('How is the height from the net measured?', 'The shot’s flight is estimated in 3D from the video. Where it passes over the net, we measure from the bottom of the ball to the top of the net. For a ball that hits the net, the height where it met the net is shown as a negative number.'),
                ('The court is in the wrong place', 'Open Court position on the video’s screen and move the corners. The video is analysed again with the corrected court.'),
            ]),
            ('Your data', [
                ('Are my videos uploaded?', 'No. Videos and results are kept in the app’s own storage on your phone.'),
                ('How do I delete my data?', 'Delete a video from its screen. To delete everything, use Delete all data in the Me tab. Videos you saved to the Photos app stay there.'),
                ('What happens when I change phones?', 'In this version your data lives only on the phone and does not move to a new one. Save the videos you want to keep to the Photos app.'),
            ]),
        ],
        'contactTitle': 'Contact us',
        'contactBody': 'Send us a message through the contact form. Telling us your phone model, its OS version and the app’s version (Version, in the Me tab) helps us answer sooner.',
        'contactLink': 'Go to the contact form',
    },
    'privacyPage': {
        'title': 'Privacy policy | pickle-up',
        'description': 'How pickle-up handles your information.',
        'eyebrow': 'pickle-up',
        'h1': 'Privacy policy',
        'updated': 'Last updated',
        'lead': 'This policy explains how Quests Bay Pte. Ltd. (“we”) handles information in the pickle-up app for smartphones (“the app”). For how we handle personal data in general, see <a href="/en/privacy/">our privacy policy</a>.',
        'sections': [
            ('summary', '1. In short', '''<ul>
<li>The videos you film with the app, and the results of analysing them, are stored only on your phone.</li>
<li>We do not receive these videos or results. The app does not communicate with our servers.</li>
<li>The app contains no third-party tools for advertising or for analysing how you use it.</li>
</ul>'''),
            ('data', '2. Information the app handles', '''<p>The app keeps the following in its own storage on your phone:</p>
<ul>
<li>The videos you film, with their sound</li>
<li>The results of analysing them (estimated body positions, ball positions, rallies, scores, and the positions and heights of shots)</li>
<li>Your practice log, notes, the profile you entered when you started, and the app’s settings</li>
</ul>
<p>All analysis runs on the device, without any network connection. To tell players apart, it uses where the people in the video stand and the colours of their clothes. It does not recognise faces or identify anyone.</p>'''),
            ('permissions', '3. Access to your phone’s features', '''<div class="table-wrap"><table>
<tr><th>Camera</th><td>To film matches and practice</td></tr>
<tr><th>Microphone</th><td>To record sound with your videos</td></tr>
<tr><th>Photos</th><td>To bring in videos filmed outside the app, and to save videos you choose to the Photos app</td></tr>
<tr><th>Notifications</th><td>To show the practice reminders you set, from the device itself</td></tr>
</table></div>
<p>Each is used only if you allow it. You can change this at any time in your phone’s Settings.</p>'''),
            ('people', '4. People in your videos', '''<p>Your videos may show the people you play with and others nearby. Please get their agreement before you film them, and before you share a video.</p>'''),
            ('sharing', '5. Sharing and third parties', '''<p>Videos are shared or saved to the Photos app only when you do so, and only to where you choose. We never give information from the app to third parties.</p>
<p>Information that Apple Inc. or Google LLC collect when you download or update the app is handled under their own privacy policies.</p>'''),
            ('delete', '6. Deleting your information', '''<p>You can delete a video from its screen at any time. Delete all data in the Me tab removes everything the app has stored. Deleting the app from your phone also removes what it stored. Videos you saved to the Photos app stay there.</p>'''),
            ('children', '7. Children', '''<p>The app has no way for us to receive information from children. Children should use it with a parent’s or guardian’s consent.</p>'''),
            ('changes', '8. Changes to this policy', '''<p>Before we add features that change how information is handled, such as signing in or advice from AI, we will update this policy and announce it in the app and on this page.</p>'''),
            ('contact', '9. Contact', '''<div class="contact"><p>Quests Bay Pte. Ltd.<br>68 Circular Road, #02-01, Singapore 049422<br><a href="/en/#contact">Contact form</a></p></div>'''),
        ],
    },
}

APP_CARD = {
    'ja': {'title': 'pickle-up', 'body': 'ピックルボールの試合を撮って、自分の打球を振り返るアプリ。ラリーと得点を自動で区切り、打球の行き先と高さをコートの図で見せます。', 'cta': '詳しく見る'},
    'en': {'title': 'pickle-up', 'body': 'Film your pickleball games and see every shot you hit. Rallies and score are kept for you, and each shot is drawn on the court with its height.', 'cta': 'Learn more'},
}
