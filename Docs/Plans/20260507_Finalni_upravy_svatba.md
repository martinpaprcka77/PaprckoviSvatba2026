# 📋 Plán finálních úprav — Svatba Paprčkovi 2026

## 🔄 Merge: Spojení obou verzí appky

### Vezmeme z PaprckoviSvatba2026app.html (design)
- ✅ Cream/béžový design (#fdf8f0, rounded karty 32px)
- ✅ MUST-DO widget s deadliny nahoře
- ✅ Duální progress bar (celkový + povinné)
- ✅ Editable budget inputy (klikací ceny v tabulce)
- ✅ Tvé finální ceny (107 300 Kč základ)

### Vezmeme ze svatba_app.html (featury)
- ✅ Countdown v hlavičce (živý odpočet)
- ✅ Person filter chips (filtrování dle osoby)
- ✅ Timeline view (samostatný view)
- ✅ Urgence štítky (🔴⚠️ overdue, 🔵 brzy)
- ✅ Bottom navigation (3 view: Úkoly / Časová osa / Info)
- ✅ Statistika po osobách
- ✅ Budget breakdown (P/D/V kategorie)

### Výsledek
Jeden soubor: `PaprckoviSvatba2026app.html` se vším — design Paprčkovi + featury.

---

---

## 📌 UI testování appky

Po mergi je potřeba appku otestovat. Možnosti:

| Způsob | Kdo/Nástroj | Co umí |
|--------|-------------|--------|
| **Computer use** | Claude Desktop | Vidí obrazovku, kliká, scrolluje, čte console errors |
| **Statická analýza** | DeepSeek TUI | Projde JS/CSS/HTML logiku |
| **Headless test** | Playwright | Automatické testy (napsat umí, spustit musí uživatel) |
| **Ruční test** | Ty v prohlížeči | Otevřít F12 → Console, Lighthouse, mobile view |

Doporučení: mergi udělej, pushni na Pages, pak otevři Claude Desktop a nech ho proklikat appku. DeepSeek TUI obrazovku nevidí.

---

## 📐 Best Practices

### HTML appka
1. **Jeden soubor** — vše v HTML (žádné závislosti)
2. **localStorage** pro perzistenci (nevyžaduje server)
3. **Mobile-first** — iPhone ready, viewport-fit, tap-highlight
4. **Offline** — funguje bez internetu po prvním načtení
5. **Záloha RAW url** — gist záloha pro případ výpadku Pages

### Git workflow
1. **master** = zdrojový kód + dokumentace
2. **gh-pages** = deploynutá verze (automaticky z masteru)
3. **Commit messages** bez diakritiky (problém s cmd.exe)
4. **Před větší změnou**:
   ```powershell
   git add . && git commit -m "backup-before-change" && git push
   ```

### Publikování
1. **Hlavní:** GitHub Pages (automatické)
2. **Záložní:** Gist (ručně přes `.\Scripts\Publish-Svatba.ps1`)
3. **RAW přes raw.githack.com:** pro sdílení bez Pages

### Zálohování
1. PS7: `backup` (alias pro Backup-Environment)
2. Wedding app: git push + gist
3. Dokumentace: git push (vše v Docs/)

---

## ⏱️ Timeline — co stihnout do 15.6.2026

| Kdy | Co | Kdo |
|-----|-----|-----|
| **Teď** | Merge appky (spojit featury) | AI |
| **Tento týden** | Matrika — potvrdit termín | Mamka + Taťka |
| **Týden 1** | Domluvit svědky | Mamka + Taťka |
| **Týden 1** | Pronájem terasy — smlouva + záloha | Mamka + Taťka |
| **Týden 2** | Rozeslat pozvánky + RSVP | Dcery |
| **Týden 2** | Objednat prstýnek (výroba 2-4 týdny) | Taťka |
| **Týden 3** | Catering — výběr menu | Mamka + Taťka |
| **Týden 3** | Domluva s fotografem (kamarád) | Taťka |
| **Týden 4** | Oblek pro taťku | Taťka |
| **Týden 4** | DJ výbava / repráky | Známý |
| **1.6.** | Finální zkouška šat | Mamka + dcery |
| **5.6.** | Finální počet hostů | Mamka + dcery |
| **5.6.** | Potvrzení techniky (stoly, židle) | Pronajímatel |
| **8.6.** | Kytice pro nevěstu | Mamka + dcery |
| **10.6.** | Dort a sladké | Dcery/mamka |
| **10.6.** | Zkouška líčení a účesu | Mamka |
| **10.6.** | Dárky pro svědky | Mamka + Taťka |
| **12.6.** | Nákup nápojů | Dcery |
| **12.6.** | Dekorace terasy | 4 dcery |
| **14.6.** | Pomocné focení/video | Dcery |
| **15.6.** | **SVATBA 🍀** | Všichni |

---

## 🔗 Užitečné příkazy

```powershell
# Zkontrolovat appku
svatba-status

# Publikovat zálohu na gist
.\Scripts\Publish-Svatba.ps1

# Otevřít v prohlížeči
start https://doma77git.github.io/PaprckoviSvatba2026/

# Rychlý push
git add . && git commit -m "update" && git push origin master
git push origin gh-pages
```

---

*Generováno: Květen 2026 • Svatba Paprčkovi 2026*
