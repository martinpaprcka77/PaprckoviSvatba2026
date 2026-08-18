/**
 * Load the derived sync snapshot for pages that need current project stats.
 * CSV files remain authoritative; sync.json is only a cached read model.
 */
(function (global) {
  'use strict';

  const KEY = 'paprckovi-sync-v1';
  const TTL = 5 * 60 * 1000;

  async function loadSync(options) {
    const opts = options || {};
    const url = opts.url || 'data/sync.json';
    const now = Date.now();

    try {
      const cached = localStorage.getItem(KEY);
      if (cached) {
        const parsed = JSON.parse(cached);
        if (parsed.timestamp && now - parsed.timestamp < TTL && parsed.data) {
          return parsed.data;
        }
      }
    } catch (_) {
      // Ignore invalid/unavailable localStorage and use the network copy.
    }

    try {
      const response = await fetch(`${url}?v=${now}`, { cache: 'no-store' });
      if (!response.ok) throw new Error(`sync.json: HTTP ${response.status}`);
      const data = await response.json();
      try {
        localStorage.setItem(KEY, JSON.stringify({ timestamp: now, data }));
      } catch (_) {
        // Cache is optional.
      }
      return data;
    } catch (error) {
      if (opts.fallback !== undefined) return opts.fallback;
      throw error;
    }
  }

  global.PaprckoviSync = { loadSync };
})(window);
