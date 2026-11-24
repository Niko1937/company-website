# The Pickle Up pages' text and settings (build.py turns them into /ja|en/apps/pickle-up/...).
# The privacy policy and the support FAQ are in pickle_up_legal.py.
# Store links: None until the app is out; the badge then shows without a link and "coming soon" beside it.
import pickle_up_legal as legal

SLUG = 'pickle-up'
NAME = 'Pickle Up'
STORES = {
    # e.g. 'https://apps.apple.com/app/id0000000000'
    'appStore': None,
    # 'https://play.google.com/store/apps/details?id=com.it.quests.pickleup'
    'googlePlay': None,
}
UPDATED = legal.UPDATED

# Screens (images/apps/pickle-up/screens/<name>-<lang>.webp), each 900 x 2000, shown at 300 px wide. Taken from
# the app's sample match (made-up data, nobody real in it) and its Practice tab, in each language.
SCREEN_SIZE = (900, 2000)

# The contact form at the end of the support page (#contact): the kinds of question, in the order shown.
CONTACT_TOPICS = ('bug', 'howto', 'plan', 'account', 'idea', 'other')

JA = {
    'lang': 'ja',
    'title': 'Pickle Up | 撮るだけで次の試合が変わるピックルボールのアプリ',
    'description': 'コートの後ろにスマホを置いて試合をすると、スコアを数えて読み上げ、あなたが打った球を1本ずつコートに描きます。ドロップは入っているのにボレーはネット、といった傾向が数字で分かり、AI コーチが次に練習することを教えます。',
    'nav': {'features': '機能', 'how': '使い方', 'privacy': 'プライバシー', 'faq': 'よくある質問', 'support': 'サポート', 'download': 'ダウンロード', 'menu': 'メニュー', 'menuOpen': 'メニューを開く', 'menuClose': 'メニューを閉じる'},
    'langSwitch': '言語を切り替える',
    'soon': '近日公開',
    'storeAlt': {'appStore': 'App Store からダウンロード', 'googlePlay': 'Google Play で手に入れよう'},
    'carousel': {'prev': '前の画面', 'next': '次の画面', 'slide': '{n}枚目'},
    'hero': {
        'title': ['撮るだけで', '次の試合が変わる'],
        'lead': '失点したショットが分かれば、意識と練習が変わる。撮影動画から自分の得意や苦手を見つけ、次の練習に役立てることができます。',
        'screen': '3d-all',
        'screenAlt': 'サンプルの試合の画面。45本の打球を立体のコートに描き、イン率82%、ネットからの高さの中央値 +19cm を表示している',
        # Beside the phone (decorative: the same numbers as its screen).
        'stats': [('イン率', '82%'), ('ネットの上の高さ（中央値）', '+19 cm')],
    },
    'features': {
        'title': 'Pickle Up でできること',
        'items': [
            {
                'title': 'スコアはアプリが数えて、|声でコールする',
                'body': 'ラリーが終わるたびに「1-0-2」のようにスコアをコールします。サーブの順番もアプリが覚えているので、プレーを止めて数え直すことはありません。終わった試合はスコアと一緒に記録に残ります。',
                'note': 'サイドアウト制とラリーポイント制に対応しています。コールは英語で、日本語にも切り替えられます。',
                'slides': [
                    ('score', 'どちらが自分で、勝ったか負けたかがひと目で分かります。得点の流れも、いつも自分の点が左です。', '試合の画面。自分11点・相手8点で勝ちの表示と、自分の点を左にした得点の流れ'),
                ],
            },
            {
                'title': 'ネットにかけた球も、|アウトした球も、|コートに残る',
                'body': '動画の中で自分を1回タップすると、あなたが打った球を1本ずつコートに描きます。入った球は着地点に丸、アウトとネットは赤い×です。ショットの種類で絞り込むと、ドロップは入っているのにボレーはネットにかけている、といった差が数字で分かります。',
                'slides': [
                    ('flat-all', '上から見た45本。奥のベースラインの外と、ネットの上にある×がミスした球です。', '45本の打球を上から見たコートに描いた画面。アウトとネットのミスが赤い×で表示されている'),
                    ('3d-drop', 'ドロップだけに絞ると、7本中6本がイン。全部キッチンに届いていて、ドロップのスコアは95点です。', 'ドロップだけを表示した立体の画面。イン率86%、キッチンに届いた割合100%、スコア95点'),
                    ('3d-volley', 'ボレーだけにすると、8本中3本がネットに。イン率は63%、スコアは78点まで下がります。', 'ボレーだけを表示した立体の画面。ネットにかかった3本が赤い×で表示され、イン率63%、スコア78点'),
                    ('3d-all', '立体で見ると、球の高さが分かります。この試合でネットの上を通った高さは、中央値で +19cm でした。指で回して角度を変えられます。', '45本の打球を立体のコートに描いた画面。イン率82%、ネットからの高さの中央値 +19cm'),
                ],
            },
            {
                'title': '次に何を練習するか、|AI コーチが|数字から答える',
                'body': 'AI コーチは試合の数字と打球の傾向を読んで、良かったところと次に直すことを返します。ボレーが8本中3本ネットにかかっていると分かったら、練習タブで「ボレーの早打ち」のようなドリルを探せます。ドリルは25種類。USA Pickleball のスキルレベルを目安に、あなたのレベルに合うものから並べています。',
                'slides': [
                    ('coach', 'AI コーチのアドバイスの例。ドロップは安定、ボレーはネットが多い、という試合の数字から書いています。', 'AI コーチのアドバイスの例。ボレーのミスと、おすすめのドリル'),
                    ('drill', 'アドバイスに出てきたドリル。コートの図と手順つきで、2人で8分ほどです。', 'ドリル「ボレーの早打ち（ハンドバトル）」の画面。コートの図とレベル3.0〜4.0の表示'),
                    ('practice', '練習タブ。ディンク、ドロップ、ボレーなど、ショットごとにドリルを探せます。', '練習タブ。レベルに合わせたおすすめと、ショットごとの練習メニュー'),
                ],
            },
        ],
    },
    'how': {
        'title': '使い方',
        'steps': [
            ('コートの後ろにスマホを置く', 'ベースラインの後ろの、なるべく高いところに置きます。コートの四隅と、手前でサーブを待つ人が画面に入れば大丈夫です。三脚やフェンス用のホルダーがあると楽です。'),
            ('いつもどおり試合をする', '「撮影をはじめる」を押したら、あとはプレーするだけです。スコアは自動で数えて、ラリーごとにコールします。'),
            ('試合のあとに振り返る', '試合の画面で自分を1回タップすると、打球の図ができます。分析タブでは、週や月ごとのまとめも見られます。'),
        ],
    },
    'privacy': {
        'title': '動画は、|あなたのスマホから|出ません',
        'items': [
            ('ri-lock-line', '動画は外に出ない', '動画はあなたの端末にしか保存されません。サーバー側で処理するのは、動画から判定された骨格や打球の動きの情報のみです。'),
            ('ri-user-unfollow-line', 'ログインなしで使える', 'アカウント登録は不要です。機種変更などでデータを引き継ぎたい場合は、アカウントを作成して同期できます。'),
            ('ri-eye-off-line', '広告も追跡もなし', '行動を追跡するツールは組み込んでおらず、広告用途などであなたの情報が外に漏れることもありません。'),
        ],
        'link': 'プライバシーポリシーを読む',
    },
    'faq': {
        'title': 'よくある質問',
        'items': [
            ('どこから撮ればいいですか？', 'コートの後ろからです。コートの四隅と、手前でサーブを待つ人が入るように置いてください。アプリの「撮影のしかた」に、置き方の見本があります。'),
            ('撮った動画はどこに保存されますか？', 'スマホの中の、アプリ専用の場所です。動画をサーバーに送ることはありません。'),
            ('分析はどれくらい正確ですか？', 'スマホ1台の映像から推定しているので、奥のコートの着地点や球の高さには誤差があります。判定に自信がない球は図に描かず、「判定不能」として数えます。'),
            ('無料で使えますか？', '録画、スコアの自動カウントと読み上げ、練習メニューは無料です。打球の分析は最初の動画1本を無料で見られます。プレミアムにすると何本でも見られます。'),
            ('対応している機種は？', 'iPhone 版と Android 版を準備しています。公開したら、このページでお知らせします。'),
        ],
        'more': 'サポートページを見る',
    },
    'cta': {'title': '次の試合から、|分析してみましょう。', 'lead': '先に中身を見たいときは、アプリの中のサンプルの試合をどうぞ。撮らなくても開けます。'},
    'footer': {
        'tagline': 'ピックルボールの試合を撮って、スコアと打った球を記録するアプリ',
        'app': 'アプリ',
        'company': '開発元',
        'links': {'support': 'サポート', 'contact': 'お問い合わせ', 'privacy': 'プライバシーポリシー'},
        'companyLinks': {'home': 'Quests について', 'apps': 'Quests のアプリ'},
        'by': 'Pickle Up は Quests Bay Pte. Ltd. が開発・運営しています。',
        'trademarks': 'Apple および Apple ロゴは、米国その他の国で登録された Apple Inc. の商標です。App Store は Apple Inc. のサービスマークです。Google Play および Google Play ロゴは Google LLC の商標です。',
    },
    'support': {
        'title': 'サポート | Pickle Up',
        'description': 'Pickle Up の使い方、よくある質問、お問い合わせ。',
        'eyebrow': 'サポート',
        'h1': 'Pickle Up のサポート',
        'lead': legal.SUPPORT_LEAD['ja'],
        'groups': legal.SUPPORT_GROUPS['ja'],
        'contact': {
            'title': 'お問い合わせ',
            'lead': '不具合のご報告、使い方のご質問、ご意見やご要望をお送りください。送信を押すと、内容を入れたメールの作成画面が開きます。',
            'required': '必須',
            'name': 'お名前',
            'namePlaceholder': '山田 太郎',
            'email': 'メールアドレス',
            'emailPlaceholder': 'you@example.com',
            'topic': 'お問い合わせの種類',
            'topicPlaceholder': '選んでください',
            'topics': {'bug': '不具合のご報告', 'howto': '使い方について', 'plan': 'プラン・購入について', 'account': 'アカウント・データについて', 'idea': 'ご意見・ご要望', 'other': 'その他'},
            'device': 'お使いの端末',
            'devicePlaceholder': '例：iPhone 15・iOS 18.1',
            'appVersion': 'アプリのバージョン',
            'appVersionPlaceholder': '例：1.0.0',
            'appVersionHint': 'アプリの「設定 › ヘルプとこのアプリについて」で確かめられます。アプリのお問い合わせボタンから開くと、自動で入ります。',
            'message': 'お問い合わせ内容',
            'messagePlaceholder': '起きたこと、そのときの操作、いつからか、などを書いてください。',
            'privacyNote': 'いただいた内容は、<a href="../privacy/">プライバシーポリシー</a>に従って扱います。',
            'submit': 'メールで送る',
            'errors': {'name': 'お名前を入力してください。', 'email': 'メールアドレスを入力してください。', 'emailFormat': 'メールアドレスの形式を確かめてください（例：name@example.com）。', 'topic': 'お問い合わせの種類を選んでください。', 'message': 'お問い合わせ内容を入力してください。'},
            'mailSubject': '[Pickle Up] お問い合わせ',
            'mailerTitle': 'メールの送り方を選ぶ',
            'mailerDescription': '使うメールを選んでください。入力した内容が入った作成画面が開きます。',
            'mailerDefault': 'いつものメールアプリ',
            'mailerOutlookWeb': 'Outlook（ウェブ版）',
            'close': '閉じる',
        },
    },
    'privacyPage': {
        'title': 'プライバシーポリシー | Pickle Up',
        'description': 'Pickle Up における情報の取り扱いについて。',
        'eyebrow': 'Pickle Up',
        'h1': 'プライバシーポリシー',
        'updated': '最終更新日',
        'lead': legal.PRIVACY_LEAD['ja'],
        'sections': legal.PRIVACY_SECTIONS['ja'],
    },
}

EN = {
    'lang': 'en',
    'title': 'Pickle Up | Just film your pickleball games, and play better the next one',
    'description': 'Prop your phone behind the court and play. Pickle Up keeps and calls the score, draws each of your shots on the court, shows where they go wrong (your drops land, your volleys find the net), and its AI coach tells you what to practise.',
    'nav': {'features': 'Features', 'how': 'How it works', 'privacy': 'Privacy', 'faq': 'FAQ', 'support': 'Support', 'download': 'Download', 'menu': 'Menu', 'menuOpen': 'Open menu', 'menuClose': 'Close menu'},
    'langSwitch': 'Change language',
    'soon': 'Coming soon',
    'storeAlt': {'appStore': 'Download on the App Store', 'googlePlay': 'Get it on Google Play'},
    'carousel': {'prev': 'Previous screen', 'next': 'Next screen', 'slide': 'Screen {n}'},
    'hero': {
        'title': ['Just film it.', 'Play better next game.'],
        'lead': 'See the shots that lose you points, and your game changes. Your video shows your strengths and weak spots to practise.',
        'screen': '3d-all',
        'screenAlt': 'The sample match: 45 shots drawn on a 3D court, with an 82% in rate and a median height over the net of +19 cm',
        'stats': [('In rate', '82%'), ('Height over the net (median)', '+19 cm')],
    },
    'features': {
        'title': 'What it does',
        'items': [
            {
                'title': 'It keeps score and calls it out',
                'body': 'After every rally it calls the score, like “1-0-2”. It keeps track of who serves, so nobody has to stop and recount. When the game ends, the score goes into your history.',
                'note': 'Side-out and rally scoring. Calls are in English, and you can switch them to Japanese.',
                'slides': [
                    ('score', 'See at a glance which side is yours and whether you won. The score’s progress keeps yours on the left too.', 'The match screen: won 11–8, with how the score went, yours on the left'),
                ],
            },
            {
                'title': 'Every shot on the court, misses included',
                'body': 'Tap yourself once in the video and Pickle Up draws each shot you hit. Shots that land get a circle; outs and nets get a red ×. Filter by shot and the differences show up in numbers. Maybe your drops land and your volleys keep finding the net.',
                'slides': [
                    ('flat-all', 'All 45 shots from above. The ×s past the far baseline and on the net are the misses.', '45 shots drawn on the court from above, with outs and nets marked with red ×s'),
                    ('3d-drop', 'Drops only: 6 of 7 went in, and every one reached the kitchen. Drop score: 95.', 'Drops only, in 3D: 86% in, 100% reached the kitchen, score 95'),
                    ('3d-volley', 'Volleys only: 3 of 8 went into the net. The in rate drops to 63% and the score to 78.', 'Volleys only, in 3D: three shots into the net marked with red ×s, 63% in, score 78'),
                    ('3d-all', 'In 3D you can see how high each ball went. In this match, the median height over the net was +19 cm. Drag to turn the court.', '45 shots drawn on a 3D court, with an 82% in rate and a median height over the net of +19 cm'),
                ],
            },
            {
                'title': 'An AI coach that reads your numbers and tells you what to practise',
                'body': 'The AI coach reads your match numbers and shot patterns, then tells you what went well and what to fix. If 3 of your 8 volleys went into the net, the Practice tab has drills like Volley hands battle. There are 25 drills, sorted by USA Pickleball skill level, with the ones for your level first.',
                'slides': [
                    ('coach', 'An example of the AI coach’s advice: steady drops, too many volleys in the net. It is written from the match numbers.', 'An example of AI coach advice about volley errors, with a suggested drill'),
                    ('drill', 'The drill from the advice, with a court diagram and steps. Two players, about 8 minutes.', 'The Volley hands battle drill, with a court diagram and level 3.0–4.0'),
                    ('practice', 'The Practice tab. Find drills by shot: dinks, drops, volleys and more.', 'The Practice tab, with drills suggested for your level and drills by shot'),
                ],
            },
        ],
    },
    'how': {
        'title': 'How it works',
        'steps': [
            ('Put your phone behind the court', 'Behind the baseline, as high as you can. You need all four corners in view, plus the server waiting on your side. A tripod or a fence mount makes it easy.'),
            ('Play as usual', 'Tap Start recording and play. The score is kept and called after every rally.'),
            ('Look back after the match', 'Tap yourself once on the match screen to get your shot map. The Insights tab adds up your weeks and months.'),
        ],
    },
    'privacy': {
        'title': 'Your videos stay on your phone',
        'items': [
            ('ri-lock-line', 'Videos never leave it', 'Videos are saved only on your phone. Our servers only handle the body and ball movement worked out from the video.'),
            ('ri-user-unfollow-line', 'No sign-up', 'No account needed. To move your data to a new phone, create an account and sync.'),
            ('ri-eye-off-line', 'No ads, no tracking', 'There are no tracking tools in the app, and your information never leaves it for advertising or anything like it.'),
        ],
        'link': 'Read the privacy policy',
    },
    'faq': {
        'title': 'Questions',
        'items': [
            ('Where do I put my phone?', 'Behind the court, with all four corners and the server on your side in view. The app’s filming guide shows an example.'),
            ('Where are my videos kept?', 'In the app’s own storage on your phone. Videos are never sent to our servers.'),
            ('How accurate is the analysis?', 'It is estimated from one phone’s video, so landings on the far side and ball heights are off by a little. Shots it cannot judge with confidence are not drawn; they are counted as unclear.'),
            ('Is it free?', 'Recording, automatic scoring and calls, and the drills are free. Shot analysis is free for your first video. With Premium there is no limit.'),
            ('Which phones does it run on?', 'iPhone and Android versions are on the way. We will post here when they are out.'),
        ],
        'more': 'Visit the support page',
    },
    'cta': {'title': 'Try it at your next game.', 'lead': 'Want to look first? The app has a sample match you can open without filming anything.'},
    'footer': {
        'tagline': 'Film your pickleball games. Keep the score and every shot you hit.',
        'app': 'App',
        'company': 'Made by',
        'links': {'support': 'Support', 'contact': 'Contact', 'privacy': 'Privacy policy'},
        'companyLinks': {'home': 'About Quests', 'apps': 'Apps by Quests'},
        'by': 'Pickle Up is built and run by Quests Bay Pte. Ltd.',
        'trademarks': 'Apple and the Apple logo are trademarks of Apple Inc., registered in the U.S. and other countries. App Store is a service mark of Apple Inc. Google Play and the Google Play logo are trademarks of Google LLC.',
    },
    'support': {
        'title': 'Support | Pickle Up',
        'description': 'How to use Pickle Up, answers to common questions, and how to reach us.',
        'eyebrow': 'Support',
        'h1': 'Pickle Up support',
        'lead': legal.SUPPORT_LEAD['en'],
        'groups': legal.SUPPORT_GROUPS['en'],
        'contact': {
            'title': 'Contact us',
            'lead': 'Report a problem, ask how something works, or send us your ideas. Sending opens your email app with your message filled in.',
            'required': 'Required',
            'name': 'Name',
            'namePlaceholder': 'Alex Smith',
            'email': 'Email',
            'emailPlaceholder': 'you@example.com',
            'topic': 'What is it about?',
            'topicPlaceholder': 'Choose one',
            'topics': {'bug': 'Something isn’t working', 'howto': 'How to use the app', 'plan': 'Plans and purchases', 'account': 'Account and data', 'idea': 'Ideas and requests', 'other': 'Something else'},
            'device': 'Your phone',
            'devicePlaceholder': 'e.g. iPhone 15, iOS 18.1',
            'appVersion': 'App version',
            'appVersionPlaceholder': 'e.g. 1.0.0',
            'appVersionHint': 'Find it in the app under Settings › Help and about. Opened from the app’s Contact button, it is filled in for you.',
            'message': 'Message',
            'messagePlaceholder': 'What happened, what you were doing, and since when.',
            'privacyNote': 'We handle your message under our <a href="../privacy/">privacy policy</a>.',
            'submit': 'Continue to email',
            'errors': {'name': 'Please enter your name.', 'email': 'Please enter your email address.', 'emailFormat': 'Please check the email address (e.g. name@example.com).', 'topic': 'Please choose what it is about.', 'message': 'Please write your message.'},
            'mailSubject': '[Pickle Up] Contact',
            'mailerTitle': 'Choose your email app',
            'mailerDescription': 'Select your email service. A compose window opens with your message filled in.',
            'mailerDefault': 'Default mail app',
            'mailerOutlookWeb': 'Outlook (web)',
            'close': 'Close',
        },
    },
    'privacyPage': {
        'title': 'Privacy policy | Pickle Up',
        'description': 'How Pickle Up handles your information.',
        'eyebrow': 'Pickle Up',
        'h1': 'Privacy policy',
        'updated': 'Last updated',
        'lead': legal.PRIVACY_LEAD['en'],
        'sections': legal.PRIVACY_SECTIONS['en'],
    },
}

# The card on the /apps/ list.
APP_CARD = {
    'ja': {'title': 'Pickle Up', 'body': 'ピックルボールの試合を撮るだけで、スコアを自動で数え、あなたの打球をコートの図で振り返り、AI コーチが次に直すポイントを教えるアプリ。', 'cta': '詳しく見る'},
    'en': {'title': 'Pickle Up', 'body': 'Film your pickleball games: the score is kept and called for you, every shot you hit is drawn on the court, and an AI coach tells you what to work on next.', 'cta': 'Learn more'},
}
