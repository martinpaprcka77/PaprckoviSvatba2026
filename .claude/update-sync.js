#!/usr/bin/env node
/**
 * Generate data/sync.json from the authoritative CSV files.
 *
 * The public web remains read-only: CSV files are the source of truth and this
 * script only produces a derived JSON snapshot for fast client-side loading.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DATA = path.join(ROOT, 'data');
const OUT = path.join(DATA, 'sync.json');
const CAP = 100000;

function parseCsv(file) {
  const text = fs.readFileSync(path.join(DATA, file), 'utf8').trim();
  const lines = text.split(/\r?\n/);
  if (!lines.length) return [];
  const headers = lines.shift().split(',').map(v => v.trim());
  return lines.filter(Boolean).map(line => {
    const values = [];
    let value = '';
    let quoted = false;
    for (let i = 0; i < line.length; i += 1) {
      const ch = line[i];
      if (ch === '"') {
        if (quoted && line[i + 1] === '"') { value += '"'; i += 1; }
        else quoted = !quoted;
      } else if (ch === ',' && !quoted) {
        values.push(value); value = '';
      } else value += ch;
    }
    values.push(value);
    return Object.fromEntries(headers.map((h, i) => [h, values[i] ?? '']));
  });
}

function number(value) {
  return Number(String(value || 0).replace(/\s/g, '').replace(',', '.')) || 0;
}

function build() {
  const tasks = parseCsv('tasks.csv');
  const budget = parseCsv('budget.csv');
  const guests = parseCsv('guests.csv');
  const changelog = parseCsv('changelog.csv');

  const completed = tasks.filter(t => t.status.toLowerCase() === 'done');
  const open = tasks.filter(t => t.status.toLowerCase() === 'open');
  const byCategory = {};
  for (const category of ['mandatory', 'important', 'optional']) {
    const rows = tasks.filter(t => t.category === category);
    const budgetRows = budget.filter(b => b.category === category);
    byCategory[category] = {
      tasks: rows.length,
      planned: budgetRows.reduce((s, r) => s + number(r.planned), 0),
      actual: budgetRows.reduce((s, r) => s + number(r.actual), 0),
    };
  }

  const planned = budget.reduce((s, r) => s + number(r.planned), 0);
  const actual = budget.reduce((s, r) => s + number(r.actual), 0);
  const confirmed = guests.filter(g => /^(yes|confirmed|ano|true|1)$/i.test(String(g.status || g.confirmed || ''))).length;
  const latest = changelog.map(r => r.date).filter(Boolean).sort().pop() || null;

  return {
    generatedAt: new Date().toISOString(),
    source: 'data/*.csv',
    wedding: { date: '2026-08-29', ceremony: '11:15', city: 'Ostrava' },
    tasks: {
      total: tasks.length,
      completed: completed.length,
      open: open.length,
      byCategory,
      completedTitles: completed.map(t => t.title),
      openTitles: open.map(t => t.title),
    },
    budget: { planned, actual, cap: CAP, reserve: CAP - planned },
    guests: { total: guests.length, confirmed },
    latestChange: latest,
  };
}

fs.writeFileSync(OUT, `${JSON.stringify(build(), null, 2)}\n`, 'utf8');
console.log(`Generated ${path.relative(ROOT, OUT)}`);
