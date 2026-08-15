#!/bin/bash
# install-hooks.sh — install the pre-commit documentation-sync hook.
#
# The hook runs `scripts/sync-docs.sh --check-only` before every commit and
# aborts the commit (exit 1) when README/PRD are out of sync with data/*.csv.
# An existing foreign hook is preserved as .git/hooks/pre-commit.bak.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$ROOT/.git/hooks/pre-commit"

if [ -e "$HOOK" ] && ! grep -q "Installed by scripts/install-hooks.sh" "$HOOK" 2>/dev/null; then
  cp "$HOOK" "$HOOK.bak"
  echo "Záloha původního pre-commit hooku: .git/hooks/pre-commit.bak"
fi

cat > "$HOOK" <<'HOOK_EOF'
#!/bin/bash
# Installed by scripts/install-hooks.sh — documentation sync validation.
# Aborts the commit when README.md / PRD are out of sync with data/*.csv.
# Run `./scripts/sync-docs.sh` to reconcile, or commit with --no-verify.
ROOT="$(git rev-parse --show-toplevel)"
exec bash "$ROOT/scripts/sync-docs.sh" --check-only
HOOK_EOF

chmod +x "$HOOK"
echo "pre-commit hook nainstalován: $HOOK"
