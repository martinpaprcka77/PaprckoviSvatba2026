# Architektura aplikací — Svatba Paprčkovi 2026

> Šablony, UML, instrukce pro všechny 3 verze svatebního plánovače.
> Každá verze je samostatný HTML soubor — žádný build, žádný npm.

---

## Přehled verzí

| Verze | Soubor | Velikost | Účel | Datum vzniku |
|-------|--------|----------|------|-------------|
| **v0** | `v0/index.html` | 22 KB | Archivní baseline (Svatba_001, 20 úkolů) | 24. 5. 2026 |
| **v1** | `index.html` | 26 KB | Produkce — stabilní, offline-first | 14. 5. 2026 |
| **v2** | `v2/index.html` | 50 KB | Testovací — git-backed, PIN, bottom nav | 21. 5. 2026 |

---

## v0 — Archivní baseline

### Účel
Referenční bod před PRD expanzí. 20 úkolů, inline data, žádný fetch.

### UML struktura

```mermaid
graph TD
    A[index.html v0] --> B[CSS: systémové fonty, béžová paleta]
    A --> C[JS: 3 sekce]
    C --> D[Data: tasksData (20 úkolů, inline)]
    C --> E[Budget: budgetItems (10 položek, inline)]
    C --> F[Storage: weddingChecklistV0]
    D --> G[Renders: TaskList, Filters, Progress]
    E --> H[Renders: BudgetTable s inputy]
    F --> I[Ukládá: done stavy]
```

### Co se zobrazuje
1. **Hero karta** — datum 29. srpna 2026
2. **Seznam úkolů** — filtrovatelný (Vše/Povinné/Důležité/Volitelné)
3. **Rozpočet** — 10 položek, editovatelná input pole, 120% tolerance
4. **Harmonogram dne** — časový harmonogram svatebního dne

### Jak se plní data
- **Úkoly:** Inline `const tasksData = [...]` v JS — mění se přímo v HTML
- **Budget:** Inline `let budgetItems = [...]` — mění se přímo v HTML
- **Storage:** Pouze done stavy v `localStorage('weddingChecklistV0')`

### Klíčové funkce v JS
| Funkce | Účel |
|--------|------|
| `renderTasks()` | Vykreslí všechny úkoly |
| `renderBudgetTable()` | Vykreslí budget |
| `updateBudgetTotal()` | Spočítá total + toleranci |
| `initFilters()` | Inicializuje filtry |
| `toggleTask(id)` | Označí/odznačí úkol |

---

## v1 — Produkce

### Účel
Stabilní verze pro denní použití. Fetchuje data z GitHubu, localStorage pro stav.

### UML struktura

```mermaid
graph TD
    A[index.html v1] --> B[CSS: Outfit+Playfair, burgundská, dark mode]
    A --> C[JS: 6 sekcí]
    
    C --> D[Fetch data z GitHub Raw]
    D --> E[parseTasksMD(tasks.md)]
    D --> F[parseGuestsMD(guests.md)]
    
    C --> G[Rendering]
    G --> H[Header: countdown, progress bary]
    G --> I[TaskList: 4 filtry, mandatory summary]
    G --> J[BudgetTable: 17 položek, inputy]
    G --> K[Guests: tabulka Mamka+Taťka]
    
    C --> L[Storage: 2 klíče]
    L --> M[svatba_done_v4: {key: bool}]
    L --> N[svatba_budget_v4: [{name, cost}]]
    
    C --> O[Funkce]
    O --> P[fetchTasks(), fetchGuests()]
    O --> Q[renderTasks(), renderBudget(), renderGuests()]
    O --> R[saveDone(), saveBudget()]
```

### Co se zobrazuje
1. **Header** — gradient burgundský, 💍 watermark, velký countdown (94 dní)
2. **Progress** — overall bar + mandatory bar (gradient)
3. **Seznam úkolů** — 4 filtry (Vše/Povinné/Důležité/Volitelné) + mandatory summary
4. **Rozpočet** — 17 editovatelných položek s inputy, 120% tolerance
5. **Seznam hostů** — Mamka/Taťka strana, tabulka s počty
6. **Offline status** — indikátor připojení

### Datový tok
```
GitHub (tasks.md) ──fetch──▶ parseTasksMD() ──▶ renderTasks()
                                  │
localStorage (svatba_done_v4) ────┘ (overrides GitHub done state)

GitHub (guests.md) ──fetch──▶ parseGuestsMD() ──▶ renderGuests()

localStorage (svatba_budget_v4) ──▶ renderBudget()
```

### Klíčové konstanty
```js
const DATA_URL = 'https://raw.githubusercontent.com/doma77git/PaprckoviSvatba2026/master/data/';
const LS_DONE = 'svatba_done_v4';
const LS_BUDGET = 'svatba_budget_v4';
```

---

## v2 — Git-backed (testovací)

### Účel
Testovací verze s PIN zámkem a zápisem do GitHubu. Bottom navigace, 4 viewy.

### UML struktura

```mermaid
graph TD
    A[v2/index.html] --> B[CSS: stejná paleta + bottom nav + dark]
    A --> C[JS: 10 sekcí, ~800 řádků]
    
    C --> D[Fetch+Parse: tasks.md + guests.md]
    
    C --> E[Storage: jeden klíč]
    E --> F[svatba_v2_state]
    F --> G[done: [indexy]]
    F --> H[timestamps: {index: ISO}]
    F --> I[actualCosts: {index: number}]
    F --> J[notes: {index: text}]
    F --> K[pinHash: SHA-256]
    F --> L[encryptedPAT: AES-GCM]
    F --> M[budgetVisible: bool]
    F --> N[filter: string]
    F --> O[lastSync: ISO]
    
    C --> P[PIN Security]
    P --> Q[deriveKey(pin) - PBKDF2]
    P --> R[encryptPAT/decryptPAT - AES-GCM]
    P --> S[GitHub API write s PAT]
    
    C --> T[4 Viewy]
    T --> U[📋 Úkoly: task list + budget bar]
    T --> V[⏱ Čas: timeline příprav + svatební den]
    T --> W[👥 Hosté: guest tables]
    T --> X[ℹ️ Info: venue, PIN, PAT, sync status]
    
    C --> Y[Bottom navigace]
    Y --> Z[switchView() - show/hide viewy]
```

### Co se zobrazuje — 4 viewy

| View | Obsah |
|------|-------|
| **📋 Úkoly** | Seznam úkolů, budget bar, tlačítko "Zobrazit splněné" |
| **⏱ Čas** | Timeline — měsíce Květen až Září, hotové/pending úkoly + harmonogram svatebního dne |
| **👥 Hosté** | Tabulky Mamka + Taťka strana, počty, jídlo, potvrzení |
| **ℹ️ Info** | Místo (mapa), PIN nastavení, PAT token, sync status |

### Klíčové funkce
| Funkce | Účel |
|--------|------|
| `fetchData()` | Fetch tasks + guests, paralelní Promise.all |
| `parseTasksMD()` | Parsování markdown tabulky na pole objektů |
| `switchView(view)` | Přepínání mezi 4 viewy, scroll na začátek |
| `toggleTask(index)` | Označení úkolu + timestamp + uložení + sync |
| `setPIN()` | Nastavení 4-místného PINu (SHA-256 hash) |
| `encryptPAT()` | Zašifrování GitHub tokenu (AES-GCM) |
| `syncToGit()` | Commit done stavu do GitHubu API |
| `renderBudget()` | Zobrazení rozpočtu (pouze odhad, žádné inputy) |
| `renderTimeline()` | Časová osa příprav + harmonogram dne |
| `renderGuests()` | Tabulka hostů podle stran |

### Datový tok
```
GitHub (tasks.md) ──fetch──▶ parseTasksMD() ──▶ renderTaskList()
GitHub (guests.md) ──fetch──▶ parseGuestsMD() ──▶ renderGuests()

localStorage (svatba_v2_state) ──▶ done + timestamps + actualCosts + notes

PIŇ: user zadá PIN ──▶ SHA-256 hash ──▶ uloží do localStorage
PAT: user zadá PAT ──▶ AES-GCM šifrování ──▶ uloží do localStorage
Sync: toggleTask() ──▶ saveLocalState() ──▶ syncToGit() ──▶ GitHub API commit
```

---

## Porovnání renderovacích funkcí

| Co se renderuje | v0 | v1 | v2 |
|-----------------|----|----|----|
| Task list | ✅ `renderTasks()` | ✅ `renderTasks()` | ✅ `renderTaskList()` |
| Filtry | ✅ Vše/M/I/O | ✅ Vše/M/I/O | ✅ Vše/M/I/O + osoby |
| Progress bar | ❌ | ✅ `computeProgress()` | ✅ budget bar |
| Countdown | ❌ | ✅ v headeru | ✅ v headeru |
| Budget | ✅ `renderBudgetTable()` | ✅ `renderBudget()` | ✅ `renderBudget()` |
| Budget inputy | ✅ input[number] | ✅ input[number] | ❌ read-only |
| Hosté | ❌ | ✅ `renderGuests()` | ✅ `renderGuests()` |
| Timeline | ❌ | ❌ | ✅ `renderTimeline()` |
| Info/PIN | ❌ | ❌ | ✅ settings view |
| Splněné skrýt | ❌ | ❌ | ✅ `renderShowDoneButton()` |
| Venue mapa | ❌ | ❌ | ✅ info view |

---

## Způsoby ukládání dat

| Co se ukládá | v0 | v1 | v2 |
|-------------|----|----|----|
| Done stavy | `weddingChecklistV0` | `svatba_done_v4` | `svatba_v2_state.done` |
| Timestampy | ❌ | ❌ | `svatba_v2_state.timestamps` |
| Skutečné ceny | ❌ | `svatba_budget_v4` | `svatba_v2_state.actualCosts` |
| Poznámky | ❌ | ❌ | `svatba_v2_state.notes` |
| PIN hash | ❌ | ❌ | `svatba_v2_state.pinHash` |
| PAT token | ❌ | ❌ | `svatba_v2_state.encryptedPAT` |
| Formát done | `{"1":bool}` | `{"deadline\|nazev":bool}` | `[index, index, ...]` |

---

## Barevná schémata

| Prvek | v0 | v1 | v2 |
|-------|----|----|----|
| Primární | `#d4a373` (zlatavá) | `#722f37` (burgundská) | `#722f37` (burgundská) |
| Akcent | `#b5835a` | `#c9a84c` (zlatá) | `#c9a84c` (zlatá) |
| Pozadí | `#fdf8f0` | `#FAF6F0` | `#FAF6F0` |
| Font nadpisy | system-ui | Playfair Display | Playfair Display |
| Font text | system-ui | Outfit | Outfit |
| Dark mode | ❌ | ✅ auto | ✅ CSS proměnné |
| Radius karet | 32px | 20px | 20px |

---

## Lokalizace (čeština)

Všechny 3 verze jsou v češtině. Jednotné názvosloví:

| Používá se | Nepoužívá se |
|------------|-------------|
| Mamka, Taťka | Máma, Táta, rodiče |
| Žanetka, Kikinka | sestra, švagrová |
| Děti (Gabriela, Kristýnka, Natálka, Kačka) | dcery, holky |
| Mikesovi (bez háčku) | Mikešovi |
| Zlatá koliba / U Miloše | restaurace, sál |
| Nová radnice Ostrava | radnice, úřad |
