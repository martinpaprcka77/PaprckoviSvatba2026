#!/usr/bin/env node
// Minimal chromium-cli-style REPL for driving the static site with Playwright.
// Reads one command per line from stdin, executes against a shared page.
//
// Commands:
//   nav <url>                  goto (relative paths resolve against BASE_URL)
//   wait-for <selector>        wait for selector visible (5s timeout)
//   wait-text <text>           wait for text visible anywhere on page
//   click <selector>           click selector
//   fill <selector> <text>     fill input
//   press <key>                keyboard press on focused element
//   eval <js>                  page.evaluate(js), prints result
//   setls <key> <value>        localStorage.setItem(key, value)
//   screenshot [name]          save PNG to SHOTS_DIR
//   console-errors             print collected console errors
//   sleep <ms>                 raw wait, use sparingly
//   quit                       close browser and exit

const { chromium } = require('playwright');
const readline = require('node:readline');
const path = require('node:path');
const fs = require('node:fs');

const BASE_URL = process.env.BASE_URL || 'http://localhost:8080';
const SHOTS_DIR = process.env.SHOTS_DIR || '/tmp/shots';
fs.mkdirSync(SHOTS_DIR, { recursive: true });

let browser, page;
let shotSeq = 0;
const consoleErrors = [];

function resolveUrl(u) {
  return /^https?:\/\//.test(u) ? u : new URL(u, BASE_URL).toString();
}

async function run(line) {
  const [cmd, ...rest] = line.trim().split(/\s+/);
  const arg = rest.join(' ');
  try {
    switch (cmd) {
      case 'nav': {
        await page.goto(resolveUrl(rest[0]), { waitUntil: 'load' });
        console.log('OK nav', page.url());
        break;
      }
      case 'wait-for': {
        await page.waitForSelector(rest[0], { state: 'visible', timeout: 5000 });
        console.log('OK wait-for', rest[0]);
        break;
      }
      case 'wait-text': {
        await page.getByText(arg).first().waitFor({ state: 'visible', timeout: 5000 });
        console.log('OK wait-text', arg);
        break;
      }
      case 'click': {
        await page.click(arg, { timeout: 5000 });
        console.log('OK click', arg);
        break;
      }
      case 'fill': {
        const sel = rest[0];
        const text = rest.slice(1).join(' ');
        await page.fill(sel, text, { timeout: 5000 });
        console.log('OK fill', sel);
        break;
      }
      case 'press': {
        await page.keyboard.press(arg);
        console.log('OK press', arg);
        break;
      }
      case 'eval': {
        const result = await page.evaluate(arg);
        console.log('OK eval', JSON.stringify(result));
        break;
      }
      case 'setls': {
        const [key, ...vparts] = rest;
        await page.evaluate(([k, v]) => localStorage.setItem(k, v), [key, vparts.join(' ')]);
        console.log('OK setls', key);
        break;
      }
      case 'screenshot': {
        shotSeq += 1;
        const name = rest[0] || `shot-${shotSeq}`;
        const file = path.join(SHOTS_DIR, `${name}.png`);
        await page.screenshot({ path: file, fullPage: true });
        console.log('OK screenshot', file);
        break;
      }
      case 'console-errors': {
        console.log('OK console-errors', JSON.stringify(consoleErrors));
        break;
      }
      case 'sleep': {
        await new Promise((r) => setTimeout(r, Number(rest[0]) || 0));
        console.log('OK sleep');
        break;
      }
      case 'quit': {
        await browser.close();
        process.exit(0);
      }
      default:
        console.log('ERR unknown command:', cmd);
    }
  } catch (e) {
    console.log('ERR', cmd, e.message.split('\n')[0]);
  }
}

async function main() {
  browser = await chromium.launch({ args: ['--no-sandbox'] });
  const context = await browser.newContext();
  page = await context.newPage();
  page.on('console', (msg) => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });
  page.on('pageerror', (err) => consoleErrors.push(String(err)));

  // Commands must run one at a time, in order: readline emits 'line' for
  // every buffered line before earlier async handlers resolve, so without
  // this queue a piped heredoc runs all commands concurrently (e.g. `quit`
  // closing the browser while `nav` is still in flight).
  let queue = Promise.resolve();
  const rl = readline.createInterface({ input: process.stdin });
  rl.on('line', (line) => {
    if (!line.trim() || line.trim().startsWith('#')) return;
    queue = queue.then(() => run(line));
  });
  rl.on('close', async () => {
    await queue;
    await browser.close();
    process.exit(0);
  });
}

main();
