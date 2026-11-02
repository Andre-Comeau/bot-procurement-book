const { chromium } = require('playwright');
(async () => {
  const [,, html, png, w, h] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 2 });
  await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  console.log(await p.evaluate(() => [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).join(',')));
  await p.screenshot({ path: png, clip: { x: 0, y: 0, width: +w, height: +h } }); await b.close();
})();
