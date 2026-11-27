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
    'nav': {'features': '機能', 'how': '使い方', 'pricing': '料金', 'privacy': 'プライバシー', 'faq': 'よくある質問', 'support': 'サポート', 'download': 'ダウンロード', 'menu': 'メニュー', 'menuOpen': 'メニューを開く', 'menuClose': 'メニューを閉じる'},
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
        'stats': [('イン率（ドロップ）', '86%'), ('ネットの上の高さ（中央値）', '+19 cm'), ('ミスの内訳', ('ネット', 5), ('アウト', 3))],
    },
    'features': {
        'title': '機能',
        'items': [
            {
                'title': 'スコアはアプリが数えて|自動音声でコール',
                'body': 'ラリーが終わるたびに、アプリがスコアを音声でコール。数え間違いを気にせず、プレーに集中できます。',
                # Heard on the page: the call the first screen shows (10-7, match point), in the app's own English voice.
                'audio': {'src': 'score-call-en.mp3', 'label': 'スコア読み上げの例を聞く'},
                'slides': [
                    ('recording', '試合を録画している画面。コート全体と4人が映った映像の上に 10-7 のスコアが出ていて、右上の読み上げはオン'),
                    ('recording-settings', '録画中に開いた試合の設定。得点方式・何点先取・デュース・ゲーム数を、録画を続けたまま変えられる'),
                ],
            },
            {
                'title': '打った球を|コート上に描いて分析',
                'body': '打球の軌道と着地点を、1本ずつコートに描きます。ショットの種類ごとに、得意な球と失点につながる球が数字で分かります。',
                'slides': [
                    ('flat-all', '45本の打球を上から見たコートに描いた画面。アウトとネットのミスがオレンジの×で表示されている'),
                    ('3d-all', '45本の打球を立体のコートに描いた画面。イン率82%、ネットからの高さの中央値 +19cm'),
                    ('3d-drop', 'ドロップだけを表示した立体の画面。イン率86%、キッチンに届いた割合100%'),
                    ('3d-volley', 'ボレーだけを表示した立体の画面。ネットにかかった3本がオレンジの×で表示され、イン率63%'),
                ],
            },
            {
                'title': '次に何を練習すべきか、|AI コーチが|データからアドバイス',
                'body': '試合の数字から、良かったところと次に直すことを AI コーチが提案。あなたのレベルに合うドリルもすぐに見つかります。',
                'slides': [
                    ('coach', 'AI コーチのアドバイスの例。ボレーのミスと、おすすめのドリル'),
                    ('drill', 'ドリル「ボレーの早打ち（ハンドバトル）」の画面。コートの図とレベル3.0〜4.0の表示'),
                    ('practice', '練習タブ。レベルに合わせたおすすめと、ショットごとの練習メニュー'),
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
    'pricing': {
        'title': '料金',
        # The same rows in the same order on both cards, so each line compares like with like.
        'plans': [
            {'name': '無料プラン', 'price': '¥0', 'period': '', 'sub': 'ずっと無料',
             'items': [('打球の分析', '月60分'), ('AI コーチのアドバイス', '月2回'),
                       ('スコアの自動カウントと読み上げ', '無制限'), ('練習用ドリル', '無制限')]},
            {'name': 'プレミアムプラン', 'price': '¥2,980', 'period': '/月', 'sub': '年額 ¥24,800（月あたり約 ¥2,067）', 'badge': '7日間無料トライアル',
             'trial': '年額プランは7日間無料でお試しできます。\n期間中に解約すれば、料金はかかりません。',
             'items': [('打球の分析', '無制限'), ('AI コーチのアドバイス', '月50回'),
                       ('スコアの自動カウントと読み上げ', '無制限'), ('練習用ドリル', '無制限')]},
        ],
        'note': '価格は日本の App Store・Google Play での税込みの価格です。',
    },
    'privacy': {
        'title': 'プライバシー',
        'items': [
            ('ri-lock-line', '動画は外に出ない', '動画はあなたの端末にしか保存されません。サーバー側で処理するのは、動画から判定された骨格や打球の動きの情報のみです。'),
            ('ri-user-unfollow-line', 'ログインなしで使える', 'アカウント登録は不要です。機種変更などでデータを引き継ぎたい場合は、アカウントを作成して同期できます。'),
            ('ri-eye-off-line', '広告も追跡もなし', '行動を追跡するツールは組み込んでおらず、広告用途などであなたの情報が外に漏れることもありません。'),
        ],
        'link': 'プライバシーポリシーを読む',
    },
    'faq': {
        'title': 'よくある質問',
        'items': [legal.SHARED_FAQ['ja'][k] for k in ('where', 'videos', 'accuracy', 'free', 'devices')],
        'more': 'サポートページを見る',
    },
    'cta': {'title': '撮るだけで|次の試合が変わる'},
    'footer': {
        'app': 'アプリ',
        'company': '開発元',
        'links': {'support': 'サポート', 'contact': 'お問い合わせ', 'privacy': 'プライバシーポリシー'},
        'companyLinks': {'home': 'Quests について', 'apps': 'Quests のアプリ'},
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
    'nav': {'features': 'Features', 'how': 'How it works', 'pricing': 'Pricing', 'privacy': 'Privacy', 'faq': 'FAQ', 'support': 'Support', 'download': 'Download', 'menu': 'Menu', 'menuOpen': 'Open menu', 'menuClose': 'Close menu'},
    'langSwitch': 'Change language',
    'soon': 'Coming soon',
    'storeAlt': {'appStore': 'Download on the App Store', 'googlePlay': 'Get it on Google Play'},
    'carousel': {'prev': 'Previous screen', 'next': 'Next screen', 'slide': 'Screen {n}'},
    'hero': {
        'title': ['Just film it.', 'Play better next game.'],
        'lead': 'See the shots that lose you points, and your game changes. Your video shows your strengths and weak spots to practise.',
        'screen': '3d-all',
        'screenAlt': 'The sample match: 45 shots drawn on a 3D court, with an 82% in rate and a median height over the net of +19 cm',
        'stats': [('In rate (drops)', '86%'), ('Height over the net (median)', '+19 cm'), ('Misses', ('Net', 5), ('Out', 3))],
    },
    'features': {
        'title': 'Features',
        'items': [
            {
                'title': 'It keeps score and calls it out',
                'body': 'After every rally, the app calls the score out loud. No miscounts. Just play.',
                'audio': {'src': 'score-call-en.mp3', 'label': 'Hear a score call'},
                'slides': [
                    ('recording', 'Recording a match: the whole court and all four players in view, the score 10–7 shown, with the score call switched on'),
                    ('recording-settings', 'Match settings opened while recording: scoring, points to win, win by 2 and games, changed without stopping'),
                ],
            },
            {
                'title': 'Every shot you hit, analysed on the court',
                'body': 'See the path and landing spot of every shot. Filter by shot to find the ones you win with, and the ones that cost you points.',
                'slides': [
                    ('flat-all', '45 shots drawn on the court from above, with outs and nets marked with orange ×s'),
                    ('3d-all', '45 shots drawn on a 3D court, with an 82% in rate and a median height over the net of +19 cm'),
                    ('3d-drop', 'Drops only, in 3D: 86% in, 100% reached the kitchen'),
                    ('3d-volley', 'Volleys only, in 3D: three shots into the net marked with orange ×s, 63% in'),
                ],
            },
            {
                'title': 'An AI coach that reads your numbers and tells you what to practise',
                'body': 'From your match numbers, the AI coach points out what went well and what to fix, and finds drills for your level.',
                'slides': [
                    ('coach', 'An example of AI coach advice about volley errors, with a suggested drill'),
                    ('drill', 'The Volley hands battle drill, with a court diagram and level 3.0–4.0'),
                    ('practice', 'The Practice tab, with drills suggested for your level and drills by shot'),
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
    'pricing': {
        'title': 'Pricing',
        'plans': [
            {'name': 'Free plan', 'price': '$0', 'period': '', 'sub': 'Free forever',
             'items': [('Shot analysis', '60 min a month'), ('AI coach advice', '2 a month'),
                       ('Score kept and called out', 'Unlimited'), ('Practice drills', 'Unlimited')]},
            {'name': 'Premium plan', 'price': '$19.99', 'period': '/month', 'sub': 'Or $164.99 a year (about $13.75 a month)', 'badge': '7-day free trial',
             'trial': 'Try the yearly plan free for 7 days.\nCancel before it ends and you pay nothing.',
             'items': [('Shot analysis', 'Unlimited'), ('AI coach advice', '50 a month'),
                       ('Score kept and called out', 'Unlimited'), ('Practice drills', 'Unlimited')]},
        ],
        'note': 'Prices are in US dollars and vary by country; your app store shows yours.',
    },
    'privacy': {
        'title': 'Privacy',
        'items': [
            ('ri-lock-line', 'Videos never leave it', 'Videos are saved only on your phone. Our servers only handle the body and ball movement worked out from the video.'),
            ('ri-user-unfollow-line', 'No sign-up', 'No account needed. To move your data to a new phone, create an account and sync.'),
            ('ri-eye-off-line', 'No ads, no tracking', 'There are no tracking tools in the app, and your information never leaves it for advertising or anything like it.'),
        ],
        'link': 'Read the privacy policy',
    },
    'faq': {
        'title': 'Questions',
        'items': [legal.SHARED_FAQ['en'][k] for k in ('where', 'videos', 'accuracy', 'free', 'devices')],
        'more': 'Visit the support page',
    },
    'cta': {'title': 'Just film it. Play better next game.'},
    'footer': {
        'app': 'App',
        'company': 'Made by',
        'links': {'support': 'Support', 'contact': 'Contact', 'privacy': 'Privacy policy'},
        'companyLinks': {'home': 'About Quests', 'apps': 'Apps by Quests'},
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
