# Výsledek overhaulu — Svatební appka + checklist

> **HISTORICKÝ DOKUMENT z 16.5.2026** — 38 úkolů, 4 osoby, projekt C:\dev\PS7.
> Aktuální stav viz CLAUDE.md nebo data/tasks.md (36 úkolů, 5 osob, 100k Kč).

**Datum:** 16. května 2026
**Rozsah:** Kompletní přepis svatebních dat — appka + Brain docs
**Stav:** ✅ Úspěšně dokončeno

---

## Co se změnilo (overhaul)

### Nová finální data
- **Datum:** 15.6./20.6./15.7. → **29.8.2026** (potvrzeno po návštěvě radnice)
- **Místo:** Terasa → **Nová radnice Ostrava + Zlatá koliba (U Miloše)**
- **Rozpočet:** 200k / 111.8k → **MAX 100 000 Kč (hard cap)**
- **Svědci:** nevyřešeno → **Kikinka (za Mamku), Žanetka (za Taťku)**
- **Organizátor:** Mamka+Taťka+Děti → **Žanetka (hlavní organizátor)**

### Appka (C:\dev\PS7\src\index.html)
- 38 tasků kompletně přepsáno (86.5k mandatory + 11k important + 2.5k optional = 100k)
- 4 hotové tasky presetnuty: termín, radnice, děti, svědci
- 4 assignees: Mamka, Taťka, Žanetka, Kikinka
- iPhone optimalizace: input zoom fix, -webkit-overflow-scrolling, 16px číselné vstupy
- Budget checkbox fix: už nezávisí na původní ceně
- Filter buttons fix: inline onclick místo broken event listenerů
- State v2 s migrací (staré localStorage done → nové [1,2,3,4])
- Budget limit: 200 000 → 100 000 Kč
- Weather coords: Ostrava (49.82, 18.26)
- README, state.json aktualizovány

### Brain docs (C:\Brain)
- master_prompt.md — sekce 8 přepsána
- knowledge.json — přidán wedding objekt + nové rozhodnutí
- CLAUDE.md — wedding sekce aktualizována
- goals.json — deadline 2026-08-29
- priorities.json — upcoming event 2026-08-29
- identity.json — talk_about refresh
- current.json — session update
- episodic.jsonl — nový záznam
- contexts/2026-05-16_personal-ms.md — přepsán
- PRD-svatba-paprckovi-2026.md — kompletní přepis
- wedding-checklist-1month.md — datum a lokace opraveny
- wedding-data-instructions.md — NOVÝ SOUBOR s pravidly konzistence

### Deployment
- Commit + push → GitHub Actions → gh-pages → https://doma77git.github.io/PaprckoviSvatba2026/

---

## Verifikace

| Check | Stav |
|---|---|
| Rozpočet = 100 000 Kč | ✅ |
| Countdown → 29.8.2026 | ✅ |
| 4 hotové tasky presetnuty | ✅ |
| 4 assignees v person filteru | ✅ |
| Žádné reference na Terasu | ✅ |
| Diakritika v názvech tasků | ✅ |
| Filter buttons fungují | ✅ |
| Budget checkbox nezávislý | ✅ |
| iPhone optimalizace | ✅ |
| Všechny Brain docs konzistentní | ✅ |
