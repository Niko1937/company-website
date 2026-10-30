// サイト表示設定。値を変更して main に push すると反映されます。
// このファイルは公開されるため、秘密情報は書かないでください。
window.SITE_CONFIG = {
  // Offices に Quests Ltd.（Marshall）を表示するか
  showMarshallOffice: false,
  // LP に表示する法人名（"Quests" または "Quests Bay"）。Offices の正式名称は変わりません
  companyName: "Quests",
  // Solutions に載せるデモ動画（書き方は README の「表示設定」）。表示する動画が 0 本の段は隠れ、
  // 法人向け・個人向けとも 0 本ならセクションとメニューの項目も隠れます。
  // show: false の動画も ID は誰でも見られるため、未公開の動画はここに書かないでください。
  solutions: [
    {
      id: "ai-claim-assessment",
      category: "business",
      show: true,
      video: { en: "6ovCw16oMjo", ja: "CWNEwtN3p10" },
      title: { en: "AI Auto Claims Assessment", ja: "AI自動車事故査定" },
      description: {
        en: "Calculates the insurance payout from photos of the damaged car and the accident report in under a minute.",
        ja: "事故車の写真と事故報告書から、保険金を1分以内で算定します。",
      },
    },
    // ▼ ローカル確認用のテスト動画（使うときはコメントを外す。本番に出さないこと）
    // { id: "test-business-1", category: "business", show: true,
    //   video: { en: "aqz-KE-bpKQ", ja: "jNQXAC9IVRw" },
    //   title: { en: "AI Document Assistant (test)", ja: "AI文書アシスタント（テスト）" },
    //   description: { en: "Reads contracts and reports, then answers questions in seconds.", ja: "契約書やレポートを読み込み、質問に数秒で回答します。" } },
    // { id: "test-business-2", category: "business", show: true,
    //   video: { en: "M7lc1UVf-VE" },
    //   title: { en: "Demand Forecasting Dashboard (test)", ja: "需要予測ダッシュボード（テスト）" },
    //   description: { en: "English video only: the Japanese page shows the same video." } },
    // { id: "test-consumer-1", category: "consumer", show: true,
    //   video: { ja: "jNQXAC9IVRw" },
    //   title: { ja: "日本語のみの動画（テスト）" },
    //   description: { ja: "日本語だけ設定した例です。英語ページでもこの動画と文が表示されます。" } },
    // { id: "test-consumer-2", category: "consumer", show: true,
    //   video: "aqz-KE-bpKQ", title: "Same Title in Both Languages (test)" },
    // { id: "test-consumer-3", category: "consumer", show: true,
    //   video: { en: "M7lc1UVf-VE", ja: "M7lc1UVf-VE" },
    //   title: { en: "Third Video: arrows appear (test)", ja: "3本目：矢印が表示されます（テスト）" },
    //   description: { en: "Line one\nLine two", ja: "1行目\n2行目" } },
    // { id: "test-business-3", category: "business", show: true, video: "aqz-KE-bpKQ",
    //   title: { en: "Business demo 3 (test)", ja: "法人向けデモ 3（テスト）" } },
    // { id: "test-business-4", category: "business", show: true, video: "jNQXAC9IVRw",
    //   title: { en: "Business demo 4 (test)", ja: "法人向けデモ 4（テスト）" } },
    // { id: "test-business-5", category: "business", show: true, video: "M7lc1UVf-VE",
    //   title: { en: "Business demo 5 (test)", ja: "法人向けデモ 5（テスト）" } },
    // { id: "test-business-6", category: "business", show: true, video: "aqz-KE-bpKQ",
    //   title: { en: "Business demo 6 (test)", ja: "法人向けデモ 6（テスト）" } },
    // { id: "test-consumer-4", category: "consumer", show: true, video: "jNQXAC9IVRw",
    //   title: { en: "Consumer demo 4 (test)", ja: "個人向けデモ 4（テスト）" } },
    // { id: "test-consumer-5", category: "consumer", show: true, video: "M7lc1UVf-VE",
    //   title: { en: "Consumer demo 5 (test)", ja: "個人向けデモ 5（テスト）" } },
    // ▲ ここまでテスト
    // {
    //   id: "ai-chatbot",                // リンク名（#solutions-ai-chatbot）。英小文字・数字・ハイフン
    //   category: "business",            // "business"（法人向け）または "consumer"（個人向け）
    //   show: true,
    //   video: { en: "YouTubeのID", ja: "YouTubeのID" },  // 片方だけでも可（もう片方の言語でも表示）
    //   title: { en: "AI Chatbot", ja: "AIチャットボット" },
    //   description: { en: "...", ja: "..." },
    //   preview: "/videos/solutions/ai-chatbot.mp4",     // 任意: カードで流す数秒の無音ループ映像
    // },
  ],
};
