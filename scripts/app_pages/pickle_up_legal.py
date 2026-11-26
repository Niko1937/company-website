# The Pickle Up privacy policy and support FAQ (ja/en), kept apart from the app page's text in pickle_up.py.
# Written from the app's own docs (pickle-up repo: docs/BACKEND.md, FEATURES.md, PRICING.md, STORE.md); update
# them together when the app changes how it handles information.


UPDATED = {'ja': '2026年11月23日', 'en': 'November 23, 2026'}

PRIVACY_LEAD = {
    'ja': 'Quests Bay Pte. Ltd.（以下「当社」）は、スマートフォン向けアプリ「Pickle Up」（以下「本アプリ」）で扱う情報について、以下のとおり定めます。当社全体の個人情報の取り扱いは、<a href="/ja/privacy/">当社のプライバシーポリシー</a>をご覧ください。',
    'en': 'This policy explains how Quests Bay Pte. Ltd. (“we”) handles information in the Pickle Up app for smartphones (“the app”). For how we handle personal data in general, see <a href="/en/privacy/">our privacy policy</a>.',
}

SUPPORT_LEAD = {
    'ja': '困ったときは、まず下のよくある質問をご覧ください。解決しないときは、お問い合わせフォームからご連絡ください。',
    'en': 'If something isn’t working as you expect, start with the questions below. If they don’t help, send us a message through the contact form.',
}

PRIVACY_SECTIONS = {
    'ja': [
        ('summary', '1. 要点', '''<ul>
<li>撮った動画は、お使いのスマートフォンの中だけに保存します。動画をサーバーに送ることはありません。</li>
<li>動画の解析（人の姿勢、ボール、ラリーの区切り、スコア）も、すべてスマートフォンの中で行います。</li>
<li>記録と解析の結果は、アカウントにバックアップします。ログインは必須ではありません。必要になったとき、本アプリが匿名のアカウントを自動で作ります（3章）。</li>
<li>AI コーチを使ったときだけ、端末で計算した数値と、フォームの静止画（最大4枚）を送ります。静止画は、アドバイスを作ったらすぐに削除します（3章）。</li>
<li>機能ごとの1日の利用回数などの匿名の統計を送ります。設定からいつでも止められます（3章）。</li>
<li>情報を売ることはありません。広告やトラッキングにも使いません。</li>
</ul>'''),
        ('device', '2. スマートフォンの中だけに保存する情報', '''<p>次の情報は、お使いのスマートフォンの中の、本アプリ専用の場所に保存します。当社のサーバーには送りません。</p>
<ul>
<li>撮った動画と、その音声</li>
<li>動画のサムネイル</li>
<li>骨格とボールの解析ファイル（動画なしで骨格を再生するためのもの）</li>
<li>ボイスオーバーの音声</li>
<li>端末ごとの設定（画面の明るさ、言語、単位、通知、振動など）</li>
</ul>
<p>解析では、選手を見分けるために、映っている人の位置や服の色を使います。顔を認識したり、誰なのかを特定したりはしません。</p>
<p>録画を声で始めたり止めたりする機能（「スタート」「ストップ」）は、声をこの端末の中だけで聞き取ります。声を外部に送ったり、録音したりはしません。</p>'''),
        ('server', '3. サーバーに送る情報と、その目的', '''<h3>アカウント</h3>
<p>AI コーチ、購入、記録のバックアップなど、サーバーが必要な機能を初めて使うとき、本アプリが匿名のアカウントを自動で作ります。名前やメールアドレスは要りません。ログインに使う鍵は、端末のキーチェーン（キーストア）にだけ保存します。iPhone では、アプリを削除してもこの鍵が残り、入れ直すと同じアカウントを使います。</p>
<p>設定 › アカウントの「アカウントを作成／ログイン」から、メールアドレス、Google、Apple、パスキーのいずれかで、いつでも任意にアカウントを作れます。そのとき、メールアドレスなど、ログインに必要な情報を受け取ります。メールアドレスは、確認コードやログインのために使います。</p>
<h3>記録のバックアップと引き継ぎ</h3>
<p>記録と解析の結果をアカウントに保存します。アカウントを作ってログインすれば、新しいスマートフォンにも引き継げます。保存するのは次の情報です。</p>
<ul>
<li>動画の情報（撮影日、長さ、メモ、お気に入り、使ったパドル、コートの四隅の位置など）。動画のファイルそのものは送りません</li>
<li>解析の結果（ラリーの区切り、スコア、打球の位置と高さ、自分として選んだ人）</li>
<li>試合と練習の記録、場面メモ、描き込み、手で付けた着地点、タグとフォルダ</li>
<li>プロフィール（呼び名、レベル、利き手、目標など）、週の目標、登録したパドル（メーカー、モデル、重さ、形、購入日）</li>
<li>AI コーチの答え</li>
</ul>
<h3>AI コーチ</h3>
<p>AI コーチのボタンを押したときだけ、端末で計算した数値（関節の角度、打点、スコアや打球のまとめなど）と、レベル・利き手・表示言語などの選択肢を送ります。練習の動画のフォームの評価では、構え・バックスイング・インパクト・フォロースルーの静止画（最大4枚）を送ることがあります。動画は送りません。試合や週・月のふりかえりでは、数値だけを送ります。</p>
<p>アドバイスの作成には、Amazon Web Services（AWS）の Amazon Bedrock を通じて、Anthropic 社の AI モデル「Claude」を使います。静止画はアドバイスを作ったらすぐに削除し、消し忘れがあっても1日で自動的に削除します。</p>
<h3>購入</h3>
<p>「Pickle Up プレミアム」と「AI コーチ 10回分」は、App Store または Google Play で購入します。支払いの情報（カード番号など）を当社が受け取ることはありません。購入の状態は RevenueCat 社のサービスで管理し、当社はアカウントごとのプランと残りの回数を保存します。RevenueCat には、当社が付けたアカウントの ID と購入の記録が渡ります。</p>
<h3>利用状況の統計</h3>
<p>どの機能がどれくらい使われているかを、利用者全体でまとめて見て、アプリの改善に役立てるために、匿名の統計を送ります。送るのは、決まった機能（録画の開始、動画の読み込み、練習の記録など）の1日ごとの利用回数と、アプリのバージョン、OS の種類、表示言語、日付（時刻なし）だけです。画面の案を比べる試験をするときは、その案の名前も送ります。</p>
<p>名前、メールアドレス、アカウント ID、端末 ID、広告 ID、位置情報、動画、記録の内容、入力した文章は送りません。統計をアカウントや端末と結び付けることもありません。</p>
<p>統計は、最初から送る設定になっています。設定 › プライバシーとデータの「使い方の統計を送る」をオフにすると、送るのをやめ、まだ送っていない分も消します。</p>
<h3>通信の記録と利用状況の分析</h3>
<p>サービスの提供と安全のため、通信の IP アドレスを最大30日保存します。IP アドレスから推定したおおよその地域（国・地方・都市）は、個人を特定しない件数に集計して、利用状況の分析とサービスの改善に使います。月ごとの利用者数を数えるため、その月のあいだだけ、IP アドレスを元に戻せない形（月ごとの秘密の値を使ったハッシュ）で扱い、月が終わると秘密の値を消して個人に結び付かないようにします。地域ごとのキャンペーンなど、個人に結び付けて使うときは、別に同意をいただきます。</p>
<p>また、サービスの改善のため、アカウントごとの利用の状況（使った日、作った記録の数、AI コーチの回数、プランの状態）を、名前やメールアドレスを含まない形で分析します。アカウントを削除すると、それまでの分析のデータは、どのアカウントのものか分からなくなります。</p>
<p>サーバーの動作の記録には、メモや AI への入力、画像などの個人的な内容を書きません。</p>
<h3>通知</h3>
<p>練習のリマインダーと、分析が終わったときのお知らせは、スマートフォンの中で作って表示します。通知のために、当社のサーバーへ情報を送ることはありません。</p>'''),
        ('providers', '4. 委託先と保存場所', '''<p>当社は、次の事業者のサービスを使って本アプリを運営しています。</p>
<div class="table-wrap"><table>
<tr><th>Amazon Web Services, Inc.</th><td>アカウント、記録のバックアップ、AI コーチの受け付け、利用状況の統計の保存と処理。シンガポール リージョンに保存します。確認コードのメールも AWS から送ります。</td></tr>
<tr><th>Anthropic, PBC（Amazon Bedrock 経由）</th><td>AI コーチのアドバイスの作成。処理は、シンガポールに限らず、AWS の世界各地のリージョンで行われることがあります。</td></tr>
<tr><th>RevenueCat, Inc.</th><td>App Store と Google Play での購入の状態の管理</td></tr>
<tr><th>Apple Inc.・Google LLC</th><td>アプリの配信、購入と支払い、Apple または Google でのログイン（選んだ場合）</td></tr>
</table></div>
<p>Apple、Google、RevenueCat が扱う情報は、それぞれのプライバシーポリシーに従って扱われます。</p>'''),
        ('retention', '5. 保存期間', '''<div class="table-wrap"><table>
<tr><th>記録のバックアップ、プロフィール、AI コーチの答え、購入の状態</th><td>アカウントを削除するまで。端末で削除した記録は、サーバーからも削除します。</td></tr>
<tr><th>AI コーチに送った数値と、作ったアドバイス（サーバーの処理用）</th><td>180日</td></tr>
<tr><th>AI コーチに送った静止画</th><td>アドバイスを作ったらすぐ削除。遅くとも1日以内</td></tr>
<tr><th>利用状況の統計</th><td>最大30日</td></tr>
<tr><th>IP アドレスを含む通信の記録</th><td>最大30日</td></tr>
<tr><th>地域ごとの件数、アカウントごとの利用の分析</th><td>2年（個人を特定しない月ごとの合計の件数は、期限を設けずに保存することがあります）</td></tr>
<tr><th>障害に備えたバックアップ</th><td>最大35日</td></tr>
</table></div>
<p>アカウントを削除したときの扱いは、9章をご覧ください。</p>'''),
        ('permissions', '6. 端末の機能へのアクセス', '''<div class="table-wrap"><table>
<tr><th>カメラ</th><td>試合や練習を撮影するため</td></tr>
<tr><th>マイク</th><td>動画に音声を記録するため、打球音を聞き取るため、「スタート」「ストップ」の声の操作と、ボイスオーバーの録音のため</td></tr>
<tr><th>音声認識</th><td>「スタート」「ストップ」の声を、端末の中で聞き取るため（使う場合だけ）</td></tr>
<tr><th>写真</th><td>アプリの外で撮った動画を取り込むため、また選んだ動画を写真アプリ（ギャラリー）に保存するため</td></tr>
<tr><th>通知</th><td>練習のリマインダーと、分析が終わったときのお知らせを表示するため</td></tr>
</table></div>
<p>いずれも、許可していただいた場合にだけ使います。許可は、端末の設定アプリからいつでも変えられます。</p>'''),
        ('people', '7. 映っている方と、顔のぼかし', '''<p>動画には、一緒にプレーする方や周りの方が映ることがあります。撮影する前に、映る方の了承を得てください。動画を共有するときも同様です。</p>
<p>動画やハイライトを共有するときは、ほかの人の顔に自動でぼかしを入れたコピーを作ります。自分の顔もぼかすかどうかは、設定 › プライバシーとデータの「自分の顔もぼかす」で決められ（最初はオフ）、共有のたびにも選べます。解析が終わっていない動画は顔の位置が分からないため、ぼかせません。顔の位置は解析で見つけた骨格から推定するため、小さく映った人など、骨格が見つからない人の顔はぼかされないことがあります。共有する前にご確認ください。元の動画と、写真アプリに保存した動画は変わりません。</p>'''),
        ('sharing', '8. 共有と第三者への提供', '''<p>動画や画像の共有と、写真アプリへの保存は、操作したときにだけ、選んだ先に対して行います。</p>
<p>当社は、本アプリの情報を売ることはありません。広告やトラッキングにも使いません。本アプリには、広告や行動の追跡のための外部のツールを組み込んでいません。4章の委託先のほかに、本アプリの情報を第三者に提供することはありません。ただし、法令に基づいて求められた場合を除きます。</p>'''),
        ('delete', '9. 情報の削除', '''<h3>動画</h3>
<ul>
<li>1本ずつ: 動画の画面から削除できます。分析のある動画は「動画だけ削除」を選ぶと、動画のファイルだけを消して、骨格や打球を動画なしで見られます。</li>
<li>まとめて: 動画ライブラリやフォルダの「選択」で、複数の動画をまとめて削除できます。</li>
<li>容量を空ける: 設定 › プライバシーとデータの「容量を空ける」で、大きい動画や古い動画を選んで削除できます。分析のある動画は動画のファイルだけを消して、分析と記録を残します。分析のない動画は、記録ごと消えます。</li>
<li>フォルダ: フォルダを削除するとき、「フォルダだけ削除（動画は残す）」か「フォルダと中の動画を削除」を選べます。</li>
</ul>
<h3>すべてのデータ</h3>
<p>設定 › プライバシーとデータの「すべてのデータを削除」で、この端末の動画、記録、設定をすべて削除できます。ログインしている場合、アカウントに保存した記録は消えず、次の同期でこの端末に戻ります。サーバーのデータも消すには、アカウントを削除してください。写真アプリに保存した動画は残ります。</p>
<h3>アカウント</h3>
<p>設定 › アカウントの「アカウントを削除」で、アカウントと、サーバーの記録、AI コーチの結果、残りの回数を削除できます。自動で作った匿名のアカウントも、同じように削除できます。この端末に入っていた、そのアカウントの動画・記録・設定も削除します。</p>
<ul>
<li>サーバーのデータは、削除を受け付けたあと、まもなく削除します。</li>
<li>解約の傾向などを分析するため、個人を特定できない形にした利用データを2年間保持します。保持するのは、試合と練習の数値、プランと利用回数などです。名前、メモ、入力した文章、メールアドレス、各種の ID は保持しません。同じメールアドレスなどで登録し直しても、新しいアカウントになり、保持したデータとは結び付きません。</li>
<li>削除したアカウントにデータを書き戻さないよう、削除したアカウントの ID と日時だけを約400日残します。</li>
<li>有料プランは自動では解約されません。App Store または Google Play で解約してください。</li>
<li>RevenueCat にある購入の記録の削除を希望する場合は、お問い合わせください。</li>
</ul>
<p>本アプリを端末から削除すると、本アプリ専用の場所にある情報も削除されます。写真アプリに保存した動画は残ります。</p>'''),
        ('children', '10. お子さまの利用', '''<p>お子さまが本アプリを使う場合は、保護者の方の同意のもとでご利用ください。お子さまの情報が、保護者の方の同意なく送られたと思われる場合は、お問い合わせください。確認のうえ削除します。</p>'''),
        ('changes', '11. 本ポリシーの変更', '''<p>本ポリシーを変更するときは、このページでお知らせします。情報の扱いが大きく変わるときは、本アプリでもお知らせし、あらためて同意をお願いします。</p>'''),
        ('contact', '12. お問い合わせ', '''<p>本ポリシーについてのご質問や、ご自身の情報の開示・訂正・削除のご希望は、お問い合わせフォームからご連絡ください。</p>
<div class="contact"><p>Quests Bay Pte. Ltd.<br>68 Circular Road, #02-01, Singapore 049422（シンガポール）<br><a href="/ja/apps/pickle-up/support/#contact">お問い合わせフォーム</a></p></div>'''),
    ],
    'en': [
        ('summary', '1. In short', '''<ul>
<li>The videos you film stay on your phone. We never upload them.</li>
<li>Videos are analysed on your phone too: body positions, the ball, rallies and the score.</li>
<li>Your records and analysis results are backed up to an account. You don’t have to sign in: when needed, the app creates an anonymous account for you (section 3).</li>
<li>Only when you use the AI coach, the app sends numbers worked out on your phone and up to 4 still images of your form. The images are deleted as soon as the advice is ready (section 3).</li>
<li>The app sends anonymous statistics, such as how many times a day each feature is used. You can turn them off in Settings at any time (section 3).</li>
<li>We never sell your information or use it for advertising or tracking.</li>
</ul>'''),
        ('device', '2. What stays on your phone', '''<p>The following is kept in the app’s own storage on your phone and is never sent to our servers:</p>
<ul>
<li>The videos you film, with their sound</li>
<li>Video thumbnails</li>
<li>Skeleton and ball analysis files (used to replay skeletons without the video)</li>
<li>Voice-over recordings</li>
<li>Settings for this phone (appearance, language, units, notifications, haptics and so on)</li>
</ul>
<p>To tell players apart, the analysis uses where people stand and the colours of their clothes. It does not recognise faces or identify anyone.</p>
<p>When you start or stop recording by voice (“Start” and “Stop”), your voice is recognised on this phone only. It is never sent anywhere or recorded.</p>'''),
        ('server', '3. What we send, and why', '''<h3>Your account</h3>
<p>The first time you use a feature that needs our servers, such as the AI coach, a purchase or backing up your records, the app quietly creates an anonymous account. No name or email address is needed. The key used to sign in is kept only in your phone’s keychain (keystore). On iPhone, the key stays even if you delete the app, so reinstalling picks up the same account.</p>
<p>You can create a full account at any time, if you wish, with email, Google, Apple or a passkey: go to Settings › Account › Create account / Sign in. We then receive what is needed to sign you in, such as your email address. We use your email address for verification codes and signing in.</p>
<h3>Backing up your records</h3>
<p>Your records and analysis results are saved to your account. Create an account and sign in, and they move to a new phone with you. We save:</p>
<ul>
<li>Video details (date, length, notes, favourites, the paddle used, court corner positions and so on). The video files themselves are never sent</li>
<li>Analysis results (rallies, the score, shot positions and heights, and which player is you)</li>
<li>Match and practice records, scene notes, drawings, landing spots you tagged, tags and folders</li>
<li>Your profile (name, level, dominant hand, goals and so on), weekly goals, and your paddles (maker, model, weight, shape and purchase date)</li>
<li>AI coach answers</li>
</ul>
<h3>AI coach</h3>
<p>Only when you tap the AI coach button, the app sends numbers worked out on your phone (joint angles, contact point, score and shot summaries and so on) with your level, dominant hand and app language. For the form review of a practice video, it may also send up to 4 still images: ready position, backswing, contact and follow-through. Videos are never sent. For matches and weekly or monthly recaps, only numbers are sent.</p>
<p>The advice is written by Claude, an AI model from Anthropic, through Amazon Bedrock on Amazon Web Services (AWS). Still images are deleted as soon as the advice is ready, and deleted automatically within a day if anything is missed.</p>
<h3>Purchases</h3>
<p>Pickle Up Premium and 10 AI Coach sessions are bought through the App Store or Google Play. We never receive your payment details, such as card numbers. Purchases are managed with RevenueCat, and we keep each account’s plan and remaining sessions. RevenueCat receives the account ID we assign and the purchase records.</p>
<h3>Usage statistics</h3>
<p>To see which features are used across all players, and so decide what to improve, the app sends anonymous statistics. We send only how many times a day a fixed set of features was used (such as starting a recording, importing a video or logging practice), with the app version, the operating system, the app language and the date (without the time). When we test two versions of a screen, the name of the version you see is sent too.</p>
<p>We never send your name, email address, account ID, device ID, advertising ID, location, videos, the content of your records or anything you type. We don’t link the statistics to your account or your phone.</p>
<p>Usage statistics are on by default. Turn off Send usage statistics in Settings › Privacy and data to stop sending them; anything not yet sent is deleted too.</p>
<h3>Connection logs and usage analysis</h3>
<p>To run the service and keep it secure, we keep the IP address of each connection for up to 30 days. We estimate a rough location (country, region and city) from it and use only totals that identify no one to understand usage and improve the service. To count monthly users, IP addresses are kept during that month only in a form that can’t be reversed (hashed with a monthly secret); at the end of the month the secret is deleted, so they can no longer be linked to anyone. If we ever want to use your location in a way linked to you, such as a local campaign, we will ask for your consent first.</p>
<p>To improve the service, we also analyse how each account is used (days used, the number of records created, AI coach use and plan status), without names or email addresses. If you delete your account, this data can no longer be linked to it.</p>
<p>Our server logs never contain personal content such as your notes, what is sent to the AI, or images.</p>
<h3>Notifications</h3>
<p>Practice reminders and analysis-finished alerts are created and shown by your phone itself. Nothing is sent to our servers for them.</p>'''),
        ('providers', '4. Service providers and where data is kept', '''<p>We use the following companies to run the app.</p>
<div class="table-wrap"><table>
<tr><th>Amazon Web Services, Inc.</th><td>Accounts, record backups, AI coach requests, and storing and processing usage statistics. Data is kept in the Singapore region. Verification emails are also sent through AWS.</td></tr>
<tr><th>Anthropic, PBC (through Amazon Bedrock)</th><td>Writing AI coach advice. Processing may take place in any AWS region worldwide, not only Singapore.</td></tr>
<tr><th>RevenueCat, Inc.</th><td>Managing purchases made on the App Store and Google Play</td></tr>
<tr><th>Apple Inc. and Google LLC</th><td>Distributing the app, purchases and payment, and signing in with Apple or Google (if you choose to)</td></tr>
</table></div>
<p>Information handled by Apple, Google and RevenueCat is subject to their own privacy policies.</p>'''),
        ('retention', '5. How long we keep it', '''<div class="table-wrap"><table>
<tr><th>Record backups, profile, AI coach answers and purchase status</th><td>Until you delete your account. Records you delete on your phone are deleted from our servers too.</td></tr>
<tr><th>Numbers sent to the AI coach, and the advice written (for processing on our servers)</th><td>180 days</td></tr>
<tr><th>Still images sent to the AI coach</th><td>Deleted as soon as the advice is ready, within a day at most</td></tr>
<tr><th>Usage statistics</th><td>Up to 30 days</td></tr>
<tr><th>Connection logs, including IP addresses</th><td>Up to 30 days</td></tr>
<tr><th>Location totals and per-account usage analysis</th><td>2 years (monthly totals that identify no one may be kept without a time limit)</td></tr>
<tr><th>Backups for disaster recovery</th><td>Up to 35 days</td></tr>
</table></div>
<p>For what happens when you delete your account, see section 9.</p>'''),
        ('permissions', '6. Access to your phone’s features', '''<div class="table-wrap"><table>
<tr><th>Camera</th><td>To film matches and practice</td></tr>
<tr><th>Microphone</th><td>To record sound with your videos, hear paddle hits, listen for “Start” and “Stop”, and record voice-overs</td></tr>
<tr><th>Speech recognition</th><td>To recognise “Start” and “Stop” on the phone itself (only if you use it)</td></tr>
<tr><th>Photos</th><td>To bring in videos filmed outside the app, and to save videos you choose to your Photos app or gallery</td></tr>
<tr><th>Notifications</th><td>To show practice reminders and let you know when analysis has finished</td></tr>
</table></div>
<p>Each is used only if you allow it. You can change this at any time in your phone’s Settings.</p>'''),
        ('people', '7. People in your videos, and face blur', '''<p>Your videos may show the people you play with and others nearby. Please get their agreement before you film them, and before you share a video.</p>
<p>When you share a video or highlight, the app makes a copy with other people’s faces blurred automatically. Whether your own face is blurred too is up to you: Blur my face too in Settings › Privacy and data (off at first), and you can choose again each time you share. Videos whose analysis hasn’t finished can’t be blurred, as the faces haven’t been located yet. Faces are located from the skeletons found during analysis, so people whose skeleton isn’t found, such as those far away, may not be blurred. Please check before you share. Your original video, and videos saved to your Photos app, are not changed.</p>'''),
        ('sharing', '8. Sharing and third parties', '''<p>Videos and images are shared or saved to your Photos app only when you do so, and only to where you choose.</p>
<p>We never sell information from the app, and we never use it for advertising or tracking. The app contains no third-party tools for advertising or for tracking what you do. Apart from the providers in section 4, we don’t give information from the app to anyone, unless the law requires us to.</p>'''),
        ('delete', '9. Deleting your information', '''<h3>Videos</h3>
<ul>
<li>One at a time: delete a video from its screen. For a video with analysis, choose Delete video only to remove just the video file and keep watching its skeletons and shots without the video.</li>
<li>Several at once: tap Select in the video library or a folder, then delete the videos you pick.</li>
<li>Free up space: in Settings › Privacy and data, choose Free up space and pick large or old videos to delete. Videos with analysis lose only the video file; their analysis and records stay. Videos without analysis are deleted with their record.</li>
<li>Folders: when you delete a folder, choose Delete folder only (keep videos), or delete the folder and the videos in it.</li>
</ul>
<h3>All data</h3>
<p>Delete all data, in Settings › Privacy and data, removes every video, record and setting from this phone. If you are signed in, the records saved to your account are not deleted and come back at the next sync. To delete them from our servers too, delete your account. Videos saved to your Photos app stay there.</p>
<h3>Your account</h3>
<p>Delete account, in Settings › Account, deletes your account with its records, AI coach results and remaining sessions on our servers. The anonymous account the app created for you can be deleted the same way. This account’s videos, records and settings on this phone are deleted too.</p>
<ul>
<li>Your data on our servers is deleted shortly after we receive the request.</li>
<li>To understand why people stop using the app, we keep usage data that can’t be traced to you for 2 years: match and practice figures, plan and usage counts and so on. We don’t keep names, notes, anything you typed, email addresses or IDs. If you sign up again, even with the same email address, you get a new account that isn’t linked to this data.</li>
<li>So that nothing is written back to a deleted account, we keep only its ID and the deletion date for about 400 days.</li>
<li>A paid plan is not cancelled automatically. Cancel it in the App Store or Google Play.</li>
<li>To have your purchase records deleted from RevenueCat, please contact us.</li>
</ul>
<p>Deleting the app from your phone also removes what it stored there. Videos saved to your Photos app stay there.</p>'''),
        ('children', '10. Children', '''<p>Children should use the app with a parent’s or guardian’s consent. If you think a child’s information has been sent to us without that consent, please contact us and we will delete it once we have checked.</p>'''),
        ('changes', '11. Changes to this policy', '''<p>When we change this policy, we will post the update on this page. If a change significantly affects how your information is handled, we will also tell you in the app and ask you to agree again.</p>'''),
        ('contact', '12. Contact', '''<p>For questions about this policy, or to ask to see, correct or delete your information, please use the contact form.</p>
<div class="contact"><p>Quests Bay Pte. Ltd.<br>68 Circular Road, #02-01, Singapore 049422<br><a href="/en/apps/pickle-up/support/#contact">Contact form</a></p></div>'''),
    ],
}

SUPPORT_GROUPS = {
    'ja': [
        ('撮影', [
            ('スマホはどこに置けばよいですか？', 'ベースラインの後ろの、なるべく高い位置に置いてください。コートの四隅と、手前のラインの後ろでサーブを待つ人まで入るように、少し広めに映します。三脚やフェンスに付けるホルダーが便利です。'),
            ('前（ネット側）から撮れますか？', '打球がスマホに当たるおそれがあるため、後ろか横から撮ってください。分析は、コートの後ろから撮った動画を前提にしています。'),
            ('試合か練習かを選ぶ必要はありますか？', 'ありません。撮った動画から自動で判定します。違っていたら、動画の画面で直せます。'),
            ('スマホに触らずに録画を始められますか？', '録画タブの「自動録画」で「待機を始める」を押すと、動き出したときや「スタート」と言ったときに録画を始めます。「ストップ」で止められます。端末によっては、録画中は声で止められません。声は端末の中だけで聞き取り、外部には送りません。'),
            ('動画を写真アプリに保存できますか？', 'できます。動画の画面から、端末の写真に保存できます。'),
        ]),
        ('スコアと読み上げ', [
            ('スコアは自動で数えますか？', 'はい。録画した試合をラリーごとに区切り、スコアを数えます。試合中は、ラリーが終わるたびにスコアを読み上げます。'),
            ('読み上げを日本語にできますか？', 'できます。読み上げは、最初は英語です。ピックルボールのコールは、どこのコートでも英語が基本のためです。録画タブの「読み上げの言語」で日本語に切り替えられます。'),
            ('読み上げを止めたいときは？', '録画タブの「スコアを読み上げる」をオフにしてください。スコアは、読み上げなしでも数えます。'),
        ]),
        ('分析', [
            ('分析は、どこで行いますか？', 'すべてスマホの中で行います。骨格・ボール・ラリー・スコアの解析のために動画をサーバーに送ることはありません。'),
            ('自分の打球を出すには？', '試合の動画を開き、「自分」から、全員が映った場面で自分の四角をタップします。ラリーごとに打球を取り出し、分析タブに表示します。'),
            ('「判定不能」とは何ですか？', '着地点やイン・アウトを判断できるほど確かでない打球です。図には描かず、本数だけを数えます。'),
            ('ネットからの高さはどう測っていますか？', '映像から打球の軌道を立体で推定し、ネットの真上を通った位置で、球の下端からネットの上端までの高さを出しています。ネットにかかった球は、ネットに当たった位置の高さをマイナスで表します。'),
            ('コートの位置がずれています', '動画の画面の「コートの位置」から、四隅の位置を直せます。直した位置で分析し直します。'),
            ('AI コーチには何が送られますか？', '端末で計算した数値と、練習の動画ではフォームの静止画（最大4枚）です。動画は送りません。静止画は、アドバイスを作ったらすぐに削除します。'),
        ]),
        ('練習メニュー', [
            ('どんな練習メニューがありますか？', '練習タブの「練習メニュー」に、25種類のドリルがあります。USA Pickleball の基準で、レベルの目安ごとに選べます。'),
            ('練習を記録できますか？', 'できます。「練習を記録」から、行ったドリルと練習した時間を記録できます。'),
        ]),
        ('アカウントとデータ', [
            ('ログインは必要ですか？', '要りません。AI コーチや購入、記録のバックアップを初めて使うとき、アプリが匿名のアカウントを自動で作ります。'),
            ('機種変更したときは？', '記録と解析の結果は、アカウントにバックアップしています。前のスマホで、設定 › アカウントの「アカウントを作成／ログイン」からアカウントを作ってください。新しいスマホで同じアカウントにログインすると、記録が戻ります。動画のファイルは引き継がれないので、残したい動画は写真アプリに保存してください。'),
            ('動画はサーバーに送られますか？', '送りません。動画はスマホの中だけに保存します。アカウントに保存するのは、記録と解析の結果だけです。'),
            ('スマホの容量を空けたい', '設定 › プライバシーとデータの「容量を空ける」で、大きい動画や古い動画をまとめて削除できます。分析のある動画は、動画のファイルだけを消して、分析と記録を残します。'),
            ('動画を削除するには？', '動画の画面から1本ずつ削除できます。動画ライブラリやフォルダの「選択」で、まとめて削除もできます。分析のある動画は「動画だけ削除」を選ぶと、骨格や打球を動画なしで見られます。'),
            ('フォルダを削除すると、中の動画も消えますか？', '選べます。「フォルダだけ削除（動画は残す）」なら、中の動画は残ります。「フォルダと中の動画を削除」なら、動画も削除します。'),
            ('すべてのデータを消すには？', '設定 › プライバシーとデータの「すべてのデータを削除」を使ってください。この端末の動画・記録・設定を削除します。ログイン中は、アカウントの記録は消えず、次の同期で戻ります。'),
            ('アカウントを削除するには？', '設定 › アカウントの「アカウントを削除」を使ってください。サーバーの記録も削除します。有料プランは自動では解約されないので、App Store または Google Play で解約してください。'),
            ('使い方の統計を止めたい', '設定 › プライバシーとデータの「使い方の統計を送る」をオフにしてください。送るのは、機能ごとの1日の利用回数などの匿名の数だけです。個人を特定できる情報は送りません。'),
            ('共有する動画の顔をぼかせますか？', 'はい。共有するときは、ほかの人の顔に自動でぼかしが入ります。自分の顔もぼかしたいときは、設定 › プライバシーとデータの「自分の顔もぼかす」をオンにしてください。小さく映った人など、ぼかされないことがあるので、共有の前にご確認ください。'),
            ('パドルを登録できますか？', 'できます。設定タブの「パドル」から、メーカー・モデル・重さ・形・購入日を登録できます。新しく撮った動画や、練習・試合の記録に、使ったパドルが付きます。'),
        ]),
        ('プランと購入', [
            ('無料でどこまで使えますか？', '録画、スコアの自動カウントと読み上げ、ラリーの区切り、練習の記録は無料で使えます。打球の分析とフォームの評価はそれぞれ毎月60分まで、AI コーチは月2回まで無料で使えます。'),
            ('プレミアムでは何ができますか？', '打球の分析を何本でも見られます。AI コーチは月50回まで使えます。月額と年額から選べます。'),
            ('「AI コーチ 10回分」とは？', 'AI コーチを10回分、追加で使える商品です。期限はありません。今月のプランの回数を使い切ったあとに使います。'),
            ('購入した内容を、新しいスマホで使うには？', '同じアカウントでログインしてください。設定 › プランの「購入を復元」でも、以前に購入したプランを使えるようにできます。'),
            ('解約するには？', '設定 › プランの「サブスクリプションを管理・解約」から、App Store または Google Play で解約できます。アカウントを削除しても、自動では解約されません。'),
        ]),
    ],
    'en': [
        ('Filming', [
            ('Where should I put my phone?', 'Behind the baseline, as high as you can. Frame it a little wide, so all four corners and the player waiting to serve behind the near line are in view. A tripod or a fence mount helps.'),
            ('Can I film from the front, by the net?', 'Please film from behind or from the side: a shot could hit your phone. The analysis expects video taken from behind the court.'),
            ('Do I need to say whether it’s a match or practice?', 'No. The app works it out from the video. If it gets it wrong, you can change it on the video’s screen.'),
            ('Can I start recording without touching my phone?', 'Yes. In the Record tab, open Auto record and tap Arm. Recording starts when you start moving or say “Start”, and “Stop” stops it. On some phones you can’t stop by voice while recording. Your voice is recognised on your phone only and never sent anywhere.'),
            ('Can I save a video to my Photos app?', 'Yes. Save it to your phone’s photos from the video’s screen.'),
        ]),
        ('Score and calls', [
            ('Does the app keep the score?', 'Yes. It splits your recorded match into rallies and keeps the score. During a match, it calls the score after each rally.'),
            ('Can the score be called in Japanese?', 'Yes. Calls are in English by default, as pickleball calls are in English on any court. Switch to Japanese under Voice language in the Record tab.'),
            ('How do I turn the calls off?', 'Turn off Call the score aloud in the Record tab. The score is still kept without them.'),
        ]),
        ('Analysis', [
            ('Where are my videos analysed?', 'On your phone. Your videos are never uploaded to analyse skeletons, the ball, rallies or the score.'),
            ('How do I see my own shots?', 'Open the match’s video, choose You, and tap your box in a frame where everyone is in view. Your shots are found rally by rally and shown in the Insights tab.'),
            ('What does “Unclear” mean?', 'A shot whose landing, or whether it was in or out, can’t be judged with enough certainty. It is counted but not drawn.'),
            ('How is the height over the net measured?', 'The shot’s flight is estimated in 3D from the video. Where it passes over the net, we measure from the bottom of the ball to the top of the net. For a ball that hits the net, the height where it met the net is shown as a negative number.'),
            ('The court is in the wrong place', 'Open Court position on the video’s screen and move the corners. The video is analysed again with the corrected court.'),
            ('What does the AI coach send?', 'Numbers worked out on your phone and, for practice videos, up to 4 still images of your form. Videos are never sent. The images are deleted as soon as the advice is ready.'),
        ]),
        ('Practice', [
            ('What drills are there?', 'The Practice tab has 25 drills, grouped by level on the USA Pickleball scale, so you can pick ones that suit you.'),
            ('Can I log my practice?', 'Yes. Use Log practice to record the drills you did and for how long.'),
        ]),
        ('Account and data', [
            ('Do I need to sign in?', 'No. The first time you use the AI coach, buy something or back up your records, the app creates an anonymous account for you.'),
            ('What happens when I change phones?', 'Your records and analysis results are backed up to your account. On your old phone, create an account in Settings › Account › Create account / Sign in. Sign in with it on your new phone and your records come back. Video files don’t move across, so save the ones you want to keep to your Photos app.'),
            ('Are my videos uploaded?', 'No. Videos stay on your phone. Only your records and analysis results are saved to your account.'),
            ('How do I free up space?', 'Use Free up space in Settings › Privacy and data to delete large or old videos in one go. Videos with analysis lose only the video file; their analysis and records stay.'),
            ('How do I delete videos?', 'Delete one from its screen, or tap Select in the video library or a folder to delete several at once. For a video with analysis, choose Delete video only to keep its skeletons and shots without the video.'),
            ('Does deleting a folder delete its videos?', 'You choose. Delete folder only (keep videos) leaves the videos. Deleting the folder and its videos removes them too.'),
            ('How do I delete all my data?', 'Use Delete all data in Settings › Privacy and data. It removes every video, record and setting from this phone. If you’re signed in, your account’s records are kept and come back at the next sync.'),
            ('How do I delete my account?', 'Use Delete account in Settings › Account. Your records on our servers are deleted too. A paid plan isn’t cancelled automatically, so cancel it in the App Store or Google Play.'),
            ('How do I stop usage statistics?', 'Turn off Send usage statistics in Settings › Privacy and data. Only anonymous counts are sent, such as how many times a day each feature is used. Nothing that identifies you is sent.'),
            ('Can I blur faces in videos I share?', 'Yes. When you share, other people’s faces are blurred automatically. To blur your own face too, turn on Blur my face too in Settings › Privacy and data. Some faces, such as people far away, may not be blurred, so please check before you share.'),
            ('Can I add my paddles?', 'Yes. Add the maker, model, weight, shape and purchase date under Paddles in the Settings tab. Your paddle is then added to new videos and to practice and match records.'),
        ]),
        ('Plans and purchases', [
            ('What can I do for free?', 'Recording, automatic scoring and calls, rally splitting and practice logs are all free. Shot analysis and form review are each free for 60 minutes of video a month, and the AI coach twice a month.'),
            ('What does Premium add?', 'Shot analysis for every video, and the AI coach up to 50 times a month. Choose monthly or yearly.'),
            ('What are 10 AI Coach sessions?', 'Ten extra uses of the AI coach. They never expire, and are used once your plan’s sessions for the month run out.'),
            ('How do I use my purchases on a new phone?', 'Sign in with the same account. You can also use Restore purchases in Settings › Plan to bring back a plan you bought before.'),
            ('How do I cancel?', 'Use Manage or cancel subscription in Settings › Plan to cancel in the App Store or Google Play. Deleting your account doesn’t cancel it.'),
        ]),
    ],
}
