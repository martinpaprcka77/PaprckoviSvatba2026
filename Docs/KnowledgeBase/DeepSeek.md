# 🤖 DeepSeek CLI & TUI — Reference

## Přehled

Nainstalováno přes npm jako balíček `deepseek-tui`.
Oba příkazy (`deepseek` a `deepseek-tui`) jsou ze stejného balíčku, jen různé entry pointy.

**Verze:** `0.8.14`
**Umístění:** `%AppData%\npm\node_modules\deepseek-tui\bin\`

---

## `deepseek` — CLI (příkazový řádek)

```powershell
deepseek "tvůj dotaz"
```

Má 18 podpříkazů pro různé scénáře:

### Hlavní příkazy

| Příkaz | Účel |
|--------|-------|
| `deepseek "text"` | Jednorázový dotaz, vrátí odpověď a skončí |
| `deepseek run` | Spustí interaktivní chat v terminálu |
| `deepseek exec` | Spustí neinteraktivní agentní příkaz |
| `deepseek review` | Code review nad aktuálním git diffem |
| `deepseek apply` | Aplikuje patch soubor nebo stdin |
| `deepseek doctor` | Diagnostika TUI |

### Správa session

| Příkaz | Účel |
|--------|-------|
| `deepseek sessions` | Seznam uložených session |
| `deepseek resume` | Obnoví předchozí session |
| `deepseek fork` | Rozvětví session (větev) |
| `deepseek thread` | Správa session metadat |

### Konfigurace a API

| Příkaz | Účel |
|--------|-------|
| `deepseek login` | Uložit API klíč |
| `deepseek logout` | Smazat uložený API klíč |
| `deepseek auth` | Správa autentizace |
| `deepseek config` | Čtení/zápis nastavení |
| `deepseek model` | Seznam/výběr modelů |
| `deepseek models` | Seznam live modelů |

### Ostatní

| Příkaz | Účel |
|--------|-------|
| `deepseek init` | Vytvoří `AGENTS.md` v aktuálním adresáři |
| `deepseek setup` | Bootstrap MCP config a skills |
| `deepseek eval` | Offline evaluace |
| `deepseek mcp` | Správa MCP serverů |
| `deepseek features` | Inspekce feature flagů |
| `deepseek serve` | Spustí lokální TUI server |
| `deepseek completions` | Generování shell completions |
| `deepseek update` | Aktualizace na nejnovější verzi |
| `deepseek metrics` | Usage statistiky |
| `deepseek help` | Nápověda |

### Užitečné parametry

```powershell
deepseek --model deepseek-v4 --prompt "dotaz"
deepseek --provider openai --model gpt-4
deepseek --output-mode json --prompt "dotaz"
deepseek --log-level debug
deepseek --no-alt-screen           # vypne alternativní obrazovku
deepseek --approval-policy never   # nikdy se neptat na potvrzení
```

---

## `deepseek-tui` — Interaktivní TUI

```powershell
deepseek-tui
```

Spustí plnohodnotné terminálové rozhraní s:
- Rozdělená obrazovka (chat + nástroje)
- Barevné zvýraznění syntaxe
- Markdown renderování včetně kódu
- Historie konverzace
- Práce se soubory (čtení, zápis, patch)
- Git integrace
- MCP servery
- Lokální sandbox
- Tool calls (vyhledávání, čtení souborů, shell příkazy)

Tento režim používáš **právě teď** — celá tahle konverzace běží v deepseek-tui.

---

## Kdy co použít

| Situace | Příkaz |
|---------|--------|
| Rychlý dotaz, jedna odpověď | `deepseek "otázka"` |
| Interaktivní chat bez nástrojů | `deepseek run` |
| Code review | `deepseek review` |
| **Plné UI s nástroji** | **`deepseek-tui`** |
| Diagnostika | `deepseek doctor` |
| Seznam modelů | `deepseek models` |
| Správa klíčů | `deepseek login` |
| Aktualizace | `deepseek update` |

---

## Užitečné tipy

### Session management
```powershell
# Uložit session (automaticky při ukončení)
# Obnovit session
deepseek resume

# Fork — vytvořit větev z existující session
deepseek fork <session-id>
```

### Config
```powershell
# Zobrazit aktuální config
deepseek config list

# Nastavit výchozí model
deepseek config set model deepseek-v4

# Nastavit providera
deepseek config set provider deepseek
```

### Rychlé dotazy bez interaktivního režimu
```powershell
deepseek "napiš PowerShell funkcí na zálohu souborů"
deepseek --model deepseek-v4 --prompt "vysvětli rozdíl mezi CLR a CRT"
```
