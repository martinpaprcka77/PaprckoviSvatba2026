# Master Prompt — Svatba Paprčkovi 2026

> Interaktivní rozhodovací strom pro úpravy projektu.
> Podle odpovědí na otázky určí, které soubory změnit a zkontrolovat.

---

## 🚀 Start

**Co chceš udělat?**

> Vyber jednu z možností a následuj její sekci.

- [Přidat/Změnit/Odebrat úkol](#a-úkoly)
- [Změnit rozpočet / cenu / platbu](#b-rozpočet)
- [Přidat/Změnit hosta](#c-hosté)
- [Změnit vzhled nebo funkci appky](#d-aplikace)
- [Aktualizovat dokumentaci / README](#e-dokumentace)
- [Jen zkontrolovat konzistenci](#f-kontrola-konzistence)

---

## A) 📋 Úkoly

### A1 — Chceš přidat nový úkol?

```
Otázka: Je úkol hotový nebo plánovaný?
  → Hotový → přidej s [x] + timestamp (ISO 8601)
  → Plánovaný → přidej s [ ]

Otázka: Kdo ho dělá?
  → Mamka / Taťka / Žanetka / Kikinka / Děti (jen tyto!)
  → Pokud Děti, nikdy je neodebírej z existujících úkolů (co-assign)

Otázka: Kategorie?
  → mandatory / important / optional

Otázka: Cena?
  → Pokud > 0, zkontroluj jestli se vejde do 100 000 Kč
```

**Soubory k editaci:**
- `data/tasks.md` — přidat řádek do tabulky
- `data/budget.md` — přidat řádek (odhad, zatím bez rezerv/zaplac)

**Po editaci zkontrolovat:**
- [ ] Header v tasks.md: `X úkolů` (správný počet)
- [ ] Tabulka Lidé v tasks.md — přepočítat počty
- [ ] Tabulka Rozpočet v tasks.md — přepočítat kategorie
- [ ] budget.md — přidat položku, zkontrolovat součty
- [ ] Celkový budget ≤ 100 000 Kč
- [ ] Spustit ověřovací Python skript

### A2 — Chceš změnit existující úkol?

```
Otázka: Co měníš?
  → Název / Termín / Kdo / Kategorii / Cenu / Stav / Poznámku

Otázka: Měníš Kdo?
  → Pokud byl Děti, zachovej je (co-assign, nenahrazuj)

Otázka: Měníš cenu?
  → Uprav i budget.md, zkontroluj celkový budget
```

**Soubory k editaci:**
- `data/tasks.md` — upravit řádek
- `data/budget.md` — pokud se mění cena

### A3 — Chceš odebrat úkol?

> ⚠️ Toto se nedělá. Úkoly se označí jako hotové `[x]`, nemažou se.

---

## B) 💰 Rozpočet

### B1 — Chceš změnit odhad (cenu)?

```
Otázka: Která položka?
  → Najdi v budget.md # + název

Otázka: Nová cena?
  → Uprav Odhad v budget.md i Plán v tasks.md
  → Zkontroluj celkový budget ≤ 100 000 Kč
  → Pokud se mění Koliba, uprav i rozpad (7a + 7b)
```

**Soubory k editaci:**
- `data/budget.md` — Odhad sloupec
- `data/tasks.md` — Plán (Kč) sloupec

### B2 — Chceš zaznamenat rezervaci / platbu?

```
Otázka: Co zadáváš?
  → Rezervováno (kolik je domluveno)
  → Zaplaceno (kolik už je zaplaceno)
  → Obojí

Otázka: Kolik?
  → Zapiš do budget.md → Rezerv / Zaplac
  → Zbývá se dopočítá (Rezerv − Zaplac)
```

**Soubor k editaci:**
- `data/budget.md` — Rezerv / Zaplac sloupce

### B3 — Koliba — chceš upravit rozpad?

```
Otázka: Mění se počet hostů?
  → Přepočti 7a1 (95 Kč × počet) a 7a2 (275 Kč × počet)
  → 7a = SUMA(7a1+7a2), 7b = 30 000 − 7a

Otázka: Mění se celková cena Koliby?
  → Uprav #7 Odhad v obou tabulkách
  → Přepočti 7b
  → Zkontroluj celkový budget
```

---

## C) 👥 Hosté

### C1 — Chceš přidat hosta?

```
Otázka: Čí strana?
  → Mamka / Taťka

Otázka: Jméno?
  → Bez příjmení, bez háčků (Mikesovi, ne Mikešovi)
  → Křestní jména / přezdívky

Otázka: Počet osob?
  → 1 / 2 / 4 (rodina) / ?

Otázka: Jídlo?
  → Normální / Vegetarián / Dítě / _

Otázka: Potvrzeno?
  → Ano / Ne / _
```

**Soubor k editaci:**
- `data/guests.md` — přidat řádek do příslušné tabulky

### C2 — Chceš změnit / odebrat hosta?

- Upravit řádek v `data/guests.md`
- Odebrat = smazat řádek (host nepřijde)

---

## D) 📱 Aplikace

### D1 — Kterou verzi měníš?

| Verze | Soubor | Kdy měnit |
|-------|--------|-----------|
| **v0** | `v0/index.html` | Nikdy (archiv) |
| **v1** | `index.html` | Stabilní verze — opravy bugů |
| **v2** | `v2/index.html` | Nové featury, redesign |

### D2 — Co chceš změnit?

```
Otázka: Vzhled?
  → CSS proměnné v :root (:primary, :bg, fonty, dark mode)
  → Header / karty / tlačítka

Otázka: Data?
  → Fetch URL (GitHub Raw) / parser / render

Otázka: Funkce?
  → Nový view / filter / tlačítko / storage klíč

Otázka: Storage?
  → localStorage klíč / formát / migrace ze starého
```

### D3 — Přidáváš nový view (pouze v2)?

```
1. Přidat HTML: <div class="view" id="myView">...</div>
2. Přidat tlačítko: <button class="nav-btn" data-view="myView">
3. Přidat funkci: renderMyView() + zavolat v init
4. Přidat do switchView() pokud má speciální chování
```

### D4 — Měníš localStorage formát?

> ⚠️ Migrace: stará data se ztratí. Uživatelé přijdou o stav.

```
Postup:
1. Zvedni verzi v názvu klíče (svatba_done_v4 → v5)
2. Při startu zkus načíst starý klíč
3. Pokud existuje, zkopíruj data do nového formátu
4. Smaž starý klíč
5. Všechny další operace používají nový klíč
```

---

## E) 📄 Dokumentace

### E1 — Který dokument měníš?

| Dokument | Komu slouží | Účel |
|----------|-------------|------|
| `README.md` | Lidé + AI | Hlavní README repa |
| `AGENTS.md` | Všechny AI (Claude Code, Cursor, Windsurf) | Pracovní konfigurace |
| `.github/copilot-instructions.md` | GitHub Copilot | AI v editoru |
| `data/budget.md` | Lidé | Rozpočet |
| `data/tasks.md` | Lidé + appky | Úkoly |
| `data/guests.md` | Lidé + appky | Hosté |
| `docs/ARCHITEKTURA-APLIKACI.md` | Vývojáři | Technický popis appek |
| `docs/PRD-svatba-paprckovi-2026.md` | Všichni | Specifikace (neměnná) |
| `HISTORY.md` | Všichni | Historie změn |
| `walkthrough.md` | (historický) | Checkpoint — neměnit |
| `task.md` | (historický) | Checkpoint — neměnit |

### E2 — Měníš data → aktualizuj i dokumentaci

Po každé změně `data/tasks.md` nebo `data/budget.md`:
- [ ] `README.md` — čísla v headeru
- [ ] `AGENTS.md` — čísla v current state
- [ ] `.github/copilot-instructions.md` — čísla v tasks
- [ ] `docs/PRD-svatba-paprckovi-2026.md` — pokud se mění struktura
- [ ] `HISTORY.md` — přidat záznam změny

---

## F) ✅ Kontrola konzistence

Spustit po každé změně datových souborů:

### F1 — tasks.md integrita
```bash
python -c "
import re
with open('data/tasks.md', encoding='utf-8') as f:
    md = f.read()
lines = [l for l in md.split('\n') if l.startswith('| 2026')]
m = i = o = 0
mc = ic = oc = 0
for l in lines:
    parts = [p.strip() for p in l.split('|')]
    cat = parts[4]; price = int(parts[5]) if parts[5].isdigit() else 0
    if cat == 'mandatory': m += price; mc += 1
    elif cat == 'important': i += price; ic += 1
    elif cat == 'optional': o += price; oc += 1
total = m + i + o
print(f'Tasks: {len(lines)} (36) | Mand: {mc}/{m} | Imp: {ic}/{i} | Opt: {oc}/{o} | Total: {total}')
print('OK' if total <= 100000 and len(lines) == 36 else 'GAP — fix before commit')
"
```

### F2 — Cross-doc sync

| Co | tasks.md | budget.md | README | AGENTS.md | copilot |
|----|----------|-----------|--------|-----------|---------|
| Počet úkolů | ✅ 36 | ✅ 36 | ✅ 36 | ✅ 36 | ✅ 36 |
| Mandatory | ✅ 19 / 84 500 | ✅ 19 / 84 500 | ✅ 19 / 84 500 | ✅ 19 / 84 500 | ✅ 19 / 84 500 |
| Important | ✅ 13 / 4 500 | ✅ 13 / 4 500 | ✅ 13 / 4 500 | ✅ 13 / 4 500 | ✅ 13 / 4 500 |
| Optional | ✅ 4 / 500 | ✅ 4 / 500 | ✅ 4 / 500 | ✅ 4 / 500 | ✅ 4 / 500 |
| CELKEM | ✅ 36 / ≤100 000 | ✅ 36 / ≤100 000 | ✅ 36 / ≤100 000 | ✅ 36 / ≤100 000 | ✅ 36 / ≤100 000 |

### F3 — Pravidla pro jména

- [ ] Děti jsou vždy aspoň u 1 úkolu
- [ ] Děti nebyly odebrány (co-assign, ne replace)
- [ ] Žádná příjmení v Kdo sloupci
- [ ] Mikesovi (ne Mikešovi s háčkem)
- [ ] Hosté v guests.md bez příjmení

### F4 — Git ready?

- [ ] `$null` a `%SystemDrive%/` nejsou v repu (přidat do .gitignore)
- [ ] package.json není v repu (přidat do .gitignore)
- [ ] Všechny změny commited
- [ ] Push do masteru → GitHub Actions → deploy

---

## 📌 Rychlé odkazy

| Akce | Příkaz |
|------|--------|
| Ověřit tasks.md | `python -c "..."` (viz F1) |
| Zobrazit rozdíly | `git diff --stat` |
| Commit + push | `git add . && git commit -m "..." && git push` |
| Zobrazit log | `git log --oneline -5` |
| Zobrazit status | `git status --short` |

---

## 🔄 Checklist po každé změně

- [ ] Všechna čísla sedí (36 úkolů, 89 500 Kč, 5 osob)
- [ ] Budget ≤ 100 000 Kč
- [ ] Děti nebyly odebrány
- [ ] Jména bez háčků
- [ ] HISTORY.md aktualizován
- [ ] Všechny docs syncnuty (README, AGENTS, copilot, PRD)
- [ ] Excel regenerován (hook nebo ručně)
- [ ] Commit + push → Actions → live
