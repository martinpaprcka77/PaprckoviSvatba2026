# 🧪 IterativeExperiment Skill — Roadmap & Decision Log

**Datum:** 2026-05-07
**Kontext:** Diskuse nad karpathy/autoresearch — agent iterativně edituje kód, měří metriku, rozhoduje keep/discard.

---

## Problém

Autoresearch pattern je přenositelný mimo LLM training: agent dostane skript + metriku + časový budget, v cyklu edituje → měří → vyhodnocuje → opakuje. PAPROS tento pattern nemá.

## Rozhodnutí → Varianta B

| Varianta | Rozsah | Stav |
|----------|--------|------|
| **A** — wrapper + log | ~20 řádků, jen měří | ❌ zamítnuto — nechytá podstatu |
| **B** — iterativní smyčka | ~80 řádků, skill v Skills.ps1 | ✅ **doporučeno** |
| **C** — PAPROS.Research modul | ~300+ řádků, standalone modul | ⏳ později až B ukáže potřebu |

**Zdůvodnění:** B demonstruje keep/discard cyklus, vejde se do jednoho skillu, je hned použitelný. A je jen logger, C je předčasný bez reálného použití.

---

## Specifikace varianty B

### Název skillu
`Invoke-IterativeExperiment` + alias `iterate`

### Vstup
| Parametr | Povinný | Popis |
|----------|---------|-------|
| `-ScriptPath` | ✅ | Cesta ke skriptu, který agent edituje |
| `-ProgramPath` | ✅ | Cesta k program.md s instrukcemi |
| `-MetricScript` | ✅ | Skript který vrátí metriku (jako float) |
| `-Iterations` | ❌ | Počet iterací (default: 10) |
| `-LogPath` | ❌ | Cesta k log souboru (default: Logs/experiments.json) |
| `-KeepThreshold` | ❌ | Metrika musí být <= tato hodnota pro keep (default: $null) |

### Cyklus
```
1. Načti program.md → předej agentovi jako kontext
2. Agent edituje ScriptPath
3. Spusť MetricScript s timeboxem
4. Načti metriku z MetricScript výstupu
5. Porovnej s předchozí metrikou:
   - lepší → keep (commit), log
   - horší → discard (git checkout --), log
6. Pokud zbývají iterace → goto 2
7. Výstup: log všech experimentů
```

### Log formát (experiments.json)
```json
{
  "session": "2026-05-07T23:42:00",
  "script": "train.py",
  "experiments": [
    {
      "iteration": 1,
      "timestamp": "...",
      "metric": 1.24,
      "kept": true,
      "diff_summary": "changed learning rate from 1e-4 to 3e-4"
    }
  ]
}
```

### Co skill NEDĚLÁ (v B)
- Nespouští sub-agenty — agent běží přímo v session
- Neřeší paralelní experimenty — jedna iterace po druhé
- Nemá vlastní UI — loguje do JSON, výstup do konzole

---

## Umístění

```powershell
DotSources\Skills.ps1          # samotná funkce + alias
Docs\Plans\program.md.template # vzorový program.md
```

## Další kroky (až se do toho někdo pustí)

1. Přidat `Invoke-IterativeExperiment` do `DotSources\Skills.ps1`
2. Vytvořit `Docs\Plans\program.md.template` jako výchozí instrukcí soubor
3. Otestovat na jednoduchém Python skriptu (např. optimalizace parametru)
4. Podle potřeby rozšířit na variantu C

---

## Související

- https://github.com/karpathy/autoresearch — inspirace
- `DotSources\Skills.ps1` — místo kam skill patří
- GTX 1060 6GB + Windows + Python 3.14 — HW na kterém se to bude testovat

---

## 📌 Poznámka: UI testování

Tento skill se zaměřuje na **backend/metrické** iterace (skript → metrika → keep/discard).

Pro **frontend/UI testování** (např. svatební HTML appka) je vhodnější Claude Desktop s **computer use** — vidí obrazovku, může klikat, scrollovat, číst console errors. DeepSeek TUI tuto schopnost nemá.

Možnosti testování HTML appek bez screen accessu:
- **Statická analýza** — projít JS, CSS, strukturu (umí DeepSeek TUI)
- **Playwright/Puppeteer** — headless testy (napsat umí, spustit musí uživatel)
- **Claude Desktop** — computer use, plnohodnotné UI testování
