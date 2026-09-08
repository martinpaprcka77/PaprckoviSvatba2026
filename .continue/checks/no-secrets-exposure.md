---
name: No Secrets Exposure
description: Block accidental commit of API keys, tokens, PIN hashes, or credentials
---

> ⚠️ **LEGACY — pozor.** Tento check cílí na zrušené `v2/index.html`
> a `data/*.md` architekturu. Repo migrovalo na `data/*.csv` (2026-06)
> a `v2/` zaniklo. Univerzální pravidlo ale platí dál: **žádné tokeny,
> klíče ani hesla do commitu** (PIN v `planner.html` je hardcoded
> organizátorská zámka, ne tajemství pro produkci).

## What to flag

Search all changed files for these patterns (case-insensitive unless noted):

### GitHub tokens
- `ghp_` followed by alphanumeric characters (GitHub Personal Access Token)
- Any base64 string near `token`, `pat`, `github` keywords longer than 30 chars
- Exception: `ghp_...` as placeholder text in HTML/UIs is OK

### API keys / encrypted data
- Long base64 strings (100+ chars) labeled as encrypted, key, or secret — flag for review
- `sk-ant-` or `sk-ant-api` (Anthropic API keys)
- Any `-----BEGIN` private key blocks

### PIN hashes
- Hex strings of exactly 64 characters near `pin`, `hash`, `SHA-256` — these might be committed PIN hashes
- Exception: the SHA-256 hash derivation code in `v2/index.html` is library code, not a committed hash

### LocalStorage / config
- Hardcoded localStorage keys with sensitive values (e.g. `localStorage.setItem('pin', '1234')`)
- Test files with real credentials (check `_test_profile.ps1`, `scripts/`)

### .env / credentials files
- `.env` files in the diff: FAIL immediately
- `credentials.json`, `secrets.json`, `*.pem` files: FAIL

## Exceptions (do NOT flag)

- `v2/index.html`: PAT input field placeholder `ghp_...` — this is UI, not a real token
- `v2/index.html`: AES-GCM, PBKDF2, SHA-256 crypto code — this is library logic, not secrets
- `svatba2026-salt` — this is a hardcoded salt string, not a secret (salt is public by design)
- Test files that use obviously fake values like `test_token`, `fake_key`, `0000...`

## Action on finding

If any real secret is found:
1. FAIL the check
2. List the file, line, and type of secret
3. Recommend: rotate the secret immediately, remove from file, use environment variable or `.gitignore`'d file
