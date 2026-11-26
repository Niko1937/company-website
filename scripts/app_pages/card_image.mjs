// The image of an app's card in Solutions (images/apps/<app>/card-<lang>.webp): the app page's hero (court and
// shots, phone and its three number cards) without its words, cut to 16:9 and taken at 1920 x 1080.
//   Needs the site served locally (python3 -m http.server 8080) and Playwright (npm i playwright, outside the repo).
//   node scripts/app_pages/card_image.mjs <ja|en> <out.png> [app]
// Then shrink it to 1560 x 878 webp (see README "アプリのカード").
import { chromium } from 'playwright';

const [lang, out, app = 'pickle-up'] = process.argv.slice(2);
if (!['ja', 'en'].includes(lang) || !out) throw new Error('usage: node card_image.mjs <ja|en> <out.png> [app]');

// The hero on a wide screen (the court with its shots, the phone and its three number cards), its words
// hidden, cut to 16:9 around the phone: the picture is laid out for the wide hero, so it stays where it
// belongs. The cut is centred on the phone, which puts the court in the middle of the frame too.
const VIEW = { width: 1536, height: 864 };
const CLIP_HEIGHT = 612;
const CLIP_WIDTH = CLIP_HEIGHT * 16 / 9;

const browser = await chromium.launch(process.env.CHROME ? { executablePath: process.env.CHROME } : {});
try {
  const page = await browser.newPage({ viewport: VIEW, deviceScaleFactor: 1920 / CLIP_WIDTH });
  await page.goto(`http://localhost:8080/${lang}/apps/${app}/`, { waitUntil: 'networkidle' });
  await page.addStyleTag({ content: `
    *{animation:none!important;transition:none!important}
    .hero-copy{visibility:hidden!important}
    .app-header,.site-header,header{visibility:hidden!important}
  ` });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  const hero = await page.locator('.hero').boundingBox();
  const phone = await page.locator('.hero-media .phone').boundingBox();
  const middle = phone.x + phone.width / 2;
  const x = Math.min(Math.max(middle - CLIP_WIDTH / 2, hero.x), hero.x + hero.width - CLIP_WIDTH);
  await page.screenshot({ path: out, clip: { x, y: phone.y - 42, width: CLIP_WIDTH, height: CLIP_HEIGHT } });
} finally {
  await browser.close();
}
