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
    'title': 'Pickle Up | ピックルボールの試合を撮るだけで、スコアも打球も AI コーチも',
    'description': 'コートの後ろにスマホを置いて試合を撮るだけ。スコアを自動で数えて読み上げ、あなたの打球をコートの図で振り返り、AI コーチが次に直すポイントを教えるピックルボールのアプリです。',
    'nav': {'features': '機能', 'how': '使い方', 'faq': 'よくある質問', 'support': 'サポート', 'download': 'ダウンロード', 'menu': 'メニュー'},
    'langSwitch': '言語を切り替える',
    'soon': '近日公開',
    'storeAlt': {'appStore': 'App Store からダウンロード', 'googlePlay': 'Google Play で手に入れよう'},
    'hero': {
        'eyebrow': 'ピックルボールの AI コーチ',
        'title': ['撮るだけで、', 'スコアも打球も', '見えてくる。'],
        'lead': 'コートの後ろにスマホを置いて、いつもどおりプレーするだけ。スコアを自動で数えて読み上げ、あなたの打球を立体のコートで振り返り、AI コーチが次に直すポイントを教えます。',
        'screen': 'shots-3d',
        'screenAlt': '試合の画面。自分の打球の軌道を、立体のコートに重ねて表示している',
    },
    'features': {
        'eyebrow': '機能',
        'title': '試合を撮ったら、|あとは|アプリに|おまかせ',
        'items': [
            {
                'screen': 'score',
                'title': '撮るだけで、|スコアを|自動で|カウント',
                'body': 'スマホを置いて、いつもどおりプレーするだけ。ラリーを自動で区切ってスコアを数え、ラリーが終わるたびに公式の形でコールします。数え間違いの言い合いも、メモを取る手間も、もうありません。',
                'points': ['ラリーとスコアを自動で記録', 'スコアを声でコール（英語・日本語）', '試合か練習かも自動で判定'],
                'alt': '試合の画面。11対8のスコアと、読み上げたスコアコールの一覧',
            },
            {
                'screen': 'shots-flat',
                'title': 'あなたの|打球が、|コートの上に',
                'body': '動画の中で自分を1回タップするだけ。あなたが打ったすべての打球を、打った位置から着地点まで線で描きます。インかアウトか、相手にボレーされたかまで、ひと目でわかります。',
                'points': ['打った位置と着地点を1本ずつ', 'イン率・ボレーの割合を自動で集計', '試合ごと・週・月でまとめて'],
                'alt': '試合の画面。自分の打球47本を、上から見たコートに線で重ねて表示している',
            },
            {
                'screen': 'kinds',
                'title': 'ショットの|種類ごとに、|くせが見える',
                'body': 'サーブ、リターン、ドロップ、ディンク、ドライブ。打球を種類ごとに分けて、軌道を見比べられます。「リターンが浅い」「ドロップが長い」といった自分のくせが、図と数字で見えてきます。',
                'points': ['サーブ・リターン・ディンクなど種類別', '着地のばらつきを図で表示', '種類ごとに0〜100点で評価'],
                'alt': '試合の画面。リターンだけに絞り込んだ打球の軌道',
            },
            {
                'screen': 'shots-3d',
                'title': '高さまで|立体で。|指で回して|確かめる',
                'body': '打球の軌道を立体で描き、ネットの何cm上を通ったかも推定します。ディンクが浮いていないか、ドライブが低く通っているかを、好きな角度から確かめられます。',
                'points': ['軌道の高さを立体で表示', 'ネットからの高さ（中央値）', '回転・拡大で好きな角度に'],
                'alt': '試合の画面の立体表示。打球の軌道を斜め上から見ている',
            },
            {
                'screen': 'coach',
                'title': 'AI コーチが、|次に直す|ことを教える',
                'body': '試合の数字と打球の傾向から、AI コーチが良かった点と、次に直すポイントを3つに絞って伝えます。練習の動画では、フォームについてもアドバイスします。',
                'points': ['良かった点と、次に直すポイント', 'すぐ試せる、具体的なアドバイス', '試合・練習・週や月のふりかえりに'],
                'alt': 'AI コーチのアドバイスの例。良かった点と、次に試す3つのポイント',
            },
            {
                'screen': 'practice',
                'title': 'レベルに|合った|練習メニューを',
                'body': 'USA Pickleball のスキルレベルを目安に、25種類のドリルを用意しました。ディンク・ドロップ・ボレーなどの種類ごとに、コートの図とやり方つきで、あなたのレベルに合う練習をおすすめします。',
                'points': ['25種類のドリルをレベル別に', 'コートの図と手順つき', '練習の記録と週の目標'],
                'alt': '練習タブ。レベルに合わせたおすすめと、種類ごとの練習メニュー',
            },
        ],
    },
    'privacy': {
        'eyebrow': 'プライバシー',
        'title': '動画は、|あなたの|スマホの|中だけに',
        'lead': '撮った動画は、スマホの中だけに保存します。動画の解析もすべて端末の中で行い、動画をサーバーに送ることはありません。',
        'items': [
            ('ri-smartphone-line', '解析はスマホの中で', '骨格やボールの検出も、ラリーとスコアの判定も、端末の中で行います。'),
            ('ri-lock-line', '動画は外に出ない', '動画はアプリ専用の場所に保存します。共有するのは、あなたが選んだときだけです。'),
            ('ri-user-unfollow-line', 'ログインなしで使える', '名前もメールアドレスも要りません。機種変更で記録を引き継ぎたいときだけ、アカウントを作れます。'),
        ],
        'link': 'プライバシーポリシーを読む',
    },
    'how': {
        'eyebrow': '使い方',
        'title': '3ステップで、|次の|試合から',
        'steps': [
            ('コートの後ろに置く', 'ベースラインの後ろの、なるべく高い位置にスマホを置きます。コートの四隅と、手前でサーブを待つ人まで入れば準備完了です。'),
            ('試合を撮る', '「撮影をはじめる」を押して、いつもどおりプレーします。スコアは自動で数えて、声でお知らせします。'),
            ('打球とアドバイスを見る', '試合の画面と分析タブで自分の打球を振り返り、AI コーチのアドバイスを読みます。'),
        ],
    },
    'faq': {
        'eyebrow': 'よくある質問',
        'title': 'よくある質問',
        'items': [
            ('どんな撮り方が必要ですか？', 'コートの後ろから、コートの四隅と手前のサーバーまで入るように撮ってください。アプリの「撮影のしかた」で、置き方の見本を見られます。'),
            ('撮った動画はどこに保存されますか？', 'スマホの中の、アプリ専用の場所に保存します。動画をサーバーに送ることはありません。'),
            ('分析はどれくらい正確ですか？', 'スマホ1台の映像から推定するため、奥のコートの着地点や球の高さには誤差があります。判定に十分な確かさがない打球は図に描かず、「判定不能」として数えます。'),
            ('無料で使えますか？', '録画、スコアの自動カウントと読み上げ、練習メニューは無料です。打球の分析は最初の動画1本を無料で見られ、プレミアムなら何本でも見られます。'),
            ('対応している機種は？', 'iPhone 版と Android 版を準備しています。公開したら、このページでお知らせします。'),
        ],
        'more': 'サポートページを見る',
    },
    'cta': {'title': '次の|試合を、|撮ってみませんか。', 'lead': 'スマホを置いて撮るだけで、スコアも打球も見えてきます。'},
    'footer': {
        'tagline': 'ピックルボールの試合を撮って、スコアと打球を自動で分析するアプリ',
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
    'title': 'Pickle Up | Film your pickleball games: score, shots and an AI coach',
    'description': 'Set your phone behind the court and film the game. Pickle Up keeps and calls the score, shows every shot you hit on the court, and an AI coach tells you what to work on next.',
    'nav': {'features': 'Features', 'how': 'How it works', 'faq': 'FAQ', 'support': 'Support', 'download': 'Download', 'menu': 'Menu'},
    'langSwitch': 'Change language',
    'soon': 'Coming soon',
    'storeAlt': {'appStore': 'Download on the App Store', 'googlePlay': 'Get it on Google Play'},
    'hero': {
        'eyebrow': 'Your pickleball AI coach',
        'title': ['Film the game.', 'See the score', 'and every shot.'],
        'lead': 'Set your phone behind the court and play as usual. Pickle Up keeps and calls the score, draws every shot you hit on a 3D court, and an AI coach tells you what to work on next.',
        'screen': 'shots-3d',
        'screenAlt': 'The match screen, with your shots drawn on the court in 3D',
    },
    'features': {
        'eyebrow': 'Features',
        'title': 'Film the match. The app does the rest.',
        'items': [
            {
                'screen': 'score',
                'title': 'Just film it.|The score|keeps itself.',
                'body': 'Set your phone down and play as usual. Pickle Up splits the rallies, keeps the score, and calls it out the official way after every rally. No more arguing over the score, no more scribbled notes.',
                'points': ['Rallies and score, recorded for you', 'Score called out loud (English or Japanese)', 'Tells a match from practice'],
                'alt': 'The match screen, with a score of 11–8 and the calls made during the game',
            },
            {
                'screen': 'shots-flat',
                'title': 'Every shot you hit,|on the court',
                'body': 'Tap yourself once in the video. Every shot you hit is drawn from where you hit it to where it landed. In or out, and whether it was volleyed back, at a glance.',
                'points': ['Where you hit and where it landed', 'In rate and volley share, counted for you', 'By match, week or month'],
                'alt': 'The match screen, with your 47 shots drawn on the court from above',
            },
            {
                'screen': 'kinds',
                'title': 'Spot your habits,|shot by shot',
                'body': 'Serves, returns, drops, dinks and drives. Split your shots by kind and compare their paths. Habits like short returns or long drops show up in the picture and the numbers.',
                'points': ['Serves, returns, dinks and more', 'Landing spread, drawn on the court', 'A 0–100 score for each kind of shot'],
                'alt': 'The match screen, showing only your returns',
            },
            {
                'screen': 'shots-3d',
                'title': 'See the height in 3D.|Turn it with a finger.',
                'body': 'Shots are drawn in 3D, with an estimate of how far above the net each one passed. Check whether your dinks float or your drives stay low, from any angle.',
                'points': ['Shot height in 3D', 'Height from the net (median)', 'Turn and zoom to any angle'],
                'alt': 'The match screen in 3D, looking at the shots from above and to the side',
            },
            {
                'screen': 'coach',
                'title': 'An AI coach that tells you|what to fix next',
                'body': 'From your match numbers and shot patterns, the AI coach tells you what went well and narrows what to work on down to three points. On practice videos, it looks at your form too.',
                'points': ['What went well, and what to fix', 'Concrete tips you can try next time', 'For matches, practice and weekly recaps'],
                'alt': 'An example of AI coach advice: what went well and three things to try',
            },
            {
                'screen': 'practice',
                'title': 'Drills that match|your level',
                'body': '25 drills, sorted by USA Pickleball skill level. Dinks, drops, volleys and more, each with a court diagram and steps, with the ones for your level suggested first.',
                'points': ['25 drills, by skill level', 'Court diagrams and step-by-step', 'Practice log and weekly goals'],
                'alt': 'The Practice tab, with drills suggested for your level and drills by shot',
            },
        ],
    },
    'privacy': {
        'eyebrow': 'Privacy',
        'title': 'Your videos stay on your phone',
        'lead': 'Your videos are kept on your phone only. All of the video analysis happens on the device, and videos are never sent to our servers.',
        'items': [
            ('ri-smartphone-line', 'Analysed on your phone', 'Finding players and the ball, splitting rallies and keeping the score all happen on the device.'),
            ('ri-lock-line', 'Videos never leave it', 'Videos are kept in the app’s own storage. They are shared only when you choose to.'),
            ('ri-user-unfollow-line', 'No sign-up needed', 'No name or email needed. Create an account only if you want to move your records to a new phone.'),
        ],
        'link': 'Read the privacy policy',
    },
    'how': {
        'eyebrow': 'How it works',
        'title': 'Three steps, starting with your next match',
        'steps': [
            ('Set it behind the court', 'Put your phone behind the baseline, as high as you can. Once all four corners and the server waiting behind the near line are in view, you are ready.'),
            ('Film the match', 'Tap Start recording and play as usual. The score is kept and called out for you.'),
            ('See your shots and tips', 'Go through your shots on the match screen and in the Insights tab, and read the AI coach’s advice.'),
        ],
    },
    'faq': {
        'eyebrow': 'FAQ',
        'title': 'Frequently asked questions',
        'items': [
            ('How should I film?', 'From behind the court, with all four corners and the server on the near side in view. The app’s filming guide shows where to put your phone.'),
            ('Where are my videos kept?', 'In the app’s own storage on your phone. Videos are never sent to our servers.'),
            ('How accurate is the analysis?', 'Everything is estimated from a single phone’s video, so landings on the far side and ball heights have some error. Shots that cannot be judged with enough certainty are not drawn; they are counted as unclear.'),
            ('Is it free?', 'Recording, automatic scoring and calls, and the drills are free. Shot analysis is free for your first video, and unlimited with Premium.'),
            ('Which phones does it run on?', 'Versions for iPhone and Android are on the way. We will announce them on this page.'),
        ],
        'more': 'Visit the support page',
    },
    'cta': {'title': 'Film your next match.', 'lead': 'Set your phone down and play. The score and every shot are there when you finish.'},
    'footer': {
        'tagline': 'Film your pickleball games. Get the score and every shot, analysed for you.',
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
