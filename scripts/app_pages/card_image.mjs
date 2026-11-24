// The image of an app's card in Solutions (images/apps/<app>/card-<lang>.webp): the app page's hero (court, phone
// and its three number cards) re-laid out in a 16:9 frame of 640 x 360 CSS px, taken at 3x.
//   Needs the site served locally (python3 -m http.server 8080) and Playwright (npm i playwright, outside the repo).
//   node scripts/app_pages/card_image.mjs <ja|en> <out.png> [app]
// Then shrink it to 1560 x 878 webp (see README "アプリのカード").
import { chromium } from 'playwright';

const [lang, out, app = 'pickle-up'] = process.argv.slice(2);
if (!['ja', 'en'].includes(lang) || !out) throw new Error('usage: node card_image.mjs <ja|en> <out.png> [app]');

// The court behind: its top right (the shot ends) beside the phone, as in the hero.
const COURT = { width: 900, left: -230, top: -80 };

const browser = await chromium.launch(process.env.CHROME ? { executablePath: process.env.CHROME } : {});
try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 3 });
  await page.goto(`http://localhost:8080/${lang}/apps/${app}/`, { waitUntil: 'networkidle' });
  await page.addStyleTag({ content: `
    *{animation:none!important;transition:none!important}
    body>*:not(main){display:none!important} main>*:not(.hero){display:none!important}
    .hero{position:fixed!important;top:0;left:0;width:640px;height:360px;overflow:hidden;z-index:9999}
    .hero .court-lines{inset:auto!important;left:${COURT.left}px!important;top:${COURT.top}px!important;
      width:${COURT.width}px!important;height:${COURT.width * 700 / 1200}px!important}
    .hero-copy{display:none!important}
    .hero-grid{position:static!important;display:block!important;padding:0!important;max-width:none!important}
    .hero-media{position:absolute!important;inset:0!important;display:block!important}
    .hero-media .phone{position:absolute;left:50%;top:26px;transform:translateX(-50%);width:236px;padding:8px;border-radius:40px}
    .hero-media .phone img{border-radius:32px}
    .hero-stats{display:contents!important}
    .hero-stat{position:absolute;width:156px}
    .hero-stat-1{left:30px;top:52px}
    .hero-stat-3{left:30px;top:196px}
    .hero-stat-2{right:30px;top:118px}
  ` });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 640, height: 360 } });
} finally {
  await browser.close();
}
