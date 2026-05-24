# Wedding Data Consistency Rules

> **Created: 16.5.2026** — historický dokument. Sync body (§KDE VŠE) odkazují na starý projekt C:\dev\PS7 + C:\Brain.
> Immutable Facts + Assignment Rules stále platné. Aktuální workflow viz CLAUDE.md.

> Purpose: Kodifikovat jak udržovat svatební data konzistentní napříč Brainem a appkou

---

## Immutable Facts (NEMĚNIT bez potvrzení uživatele)

| Field | Value |
|---|---|
| **Datum** | 29.8.2026 (August 29, 2026) |
| **Obřad** | 11:15, Nová radnice Ostrava |
| **Hostina** | U Miloše, Zlatá koliba |
| **Rozpočet** | MAX 100 000 Kč (hard cap) |
| **Svědkyně za nevěstu** | Kikinka |
| **Svědkyně za ženicha** | Žanetka |
| **Organizátor** | Žanetka |
| **Hotové úkoly** | IDs 1-4: termín (potvrzen), radnice (11.5.), děti (proběhlo), svědci (15.5.) — + #5 oddávající v pondělí, #8 Miloš potvrzen |

## Assignment Rules

- **Žanetka** → catering, venue logistics, bar, decoration, games, confetti
- **Kikinka** → ceremony logistics, flowers, legal docs, speeches, photos
- **Mamka** → clothing, guest list, invitations, gifts, guestbook
- **Taťka** → transport, rings, music, suit, umbrellas, honeymoon

## Sync Points — KDE VŠE JE TŘEBA AKTUALIZOVAT

Při jakékoliv změně svatebních dat aktualizovat VŽDY:

### App data (`C:\dev\PS7`)
1. `src/index.html` — TASKS array, WEDDING constant, budget limit (řádek ~735), settings about text
2. `src/state.json` — pokud se mění hotové tasky
3. `README.md` — pouze pokud se mění klíčové info

### Brain data (`C:\Brain`)
4. `master_prompt.md` — sekce 8 (autoritativní zdroj)
5. `.state/knowledge.json` — wedding objekt
6. `.state/goals.json` — deadline
7. `.state/priorities.json` — upcoming event
8. `.state/identity.json` — talk_about
9. `CLAUDE.md` — wedding kontext
10. `contexts/<today>_personal-ms.md` — daily context

### Brain derived docs (jen při velkých změnách)
11. `.brain-docs/PRD-svatba-paprckovi-2026.md`
12. `.brain-docs/wedding-checklist-1month.md`
13. `.brain-docs/wedding-checklist-1month-result.md`

## Verification Checklist

Po každé změně svatebních dat ověřit:

1. [ ] Suma všech task prices = přesně 100 000 Kč? (mandatory 94 500 + important 5 000 + optional 500)
2. [ ] Všechny deadliny před 29.8.2026 (kromě post-svatebních — změna příjmení 5.9.)?
3. [ ] Všechny 5 hotové tasky (IDs 1-5) jsou marked done?
4. [ ] Žádné reference na Terasa?
5. [ ] Všechny názvy mají správnou diakritiku?
6. [ ] Appka deploynutá a funkční na GitHub Pages?
7. [ ] Person filter ukazuje 5 jmen: Mamka, Taťka, Žanetka, Kikinka, Děti?
8. [ ] Countdown ukazuje dny do 29.8.2026?
9. [ ] Budget bar ukazuje limit 100 000 Kč?

## Budget Breakdown

```
POVINNÉ (mandatory):      94 500 Kč (19 tasků)
DŮLEŽITÉ (important):      5 000 Kč (13 tasků)
VOLITELNÉ (optional):        500 Kč (4 tasky)
─────────────────────────────────────────
CELKEM:                  100 000 Kč (36 tasků)
```
