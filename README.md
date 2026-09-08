# 💍 Dagmar + Martin Paprčkovi — svatební web

Památka na svatbu **Dagmar Sobkové a Martina Paprčky**, kteří se vzali v sobotu **29. srpna 2026 v 11:15** na Nové radnici v Ostravě. Stránka je poděkování pro hosty s galerií fotek a interním plánovačem pro rodinu.

## 🔗 Odkazy

- **Web:** https://martinpaprcka77.github.io/PaprckoviSvatba2026/
- **Repo:** https://github.com/martinpaprcka77/PaprckoviSvatba2026 (veřejné)
- **Plánovač (rodina, PIN):** https://martinpaprcka77.github.io/PaprckoviSvatba2026/planner.html
- **Detailní PRD / historie:** [`docs/PRD-svatba-paprckovi-2026.md`](docs/PRD-svatba-paprckovi-2026.md)

## 🖼️ Veřejná stránka (`index.html`)

- Jména **Dagmar + Martin Paprčkovi** s watermarkem „JUST MARRIED".
- Počítadlo „společného času" s vtipnou tovární cedulí a tlačítkem **MASTER STOP** (incident se zaznamená, hlavní počítadlo se neresetuje).
- Galerie **„Fotky z našeho dne"** (fotky v `media/fotky/`, fullscreen prohlížeč).

## 🧱 Stack a lokalní běh

Statická HTML/CSS/JS stránka, bez build systému a bez backendu.

```bash
python -m http.server 8080      # pak otevři http://localhost:8080/
```

Data jsou v `data/*.csv` a web je čte read-only. Vývojové adresáře (`docs/`, `.github/`) se na web nepublikují.

## 📄 Stránky

| Stránka | Popis | Stav |
|---|---|---|
| `index.html` | poděkování + galerie | publikovaná (`/`) |
| `planner.html` | plánovač pro rodinu (PIN) | publikovaná |
| `landing.html`, `karaoke.html`, `index_june.html`, `tests.html` | archiv | v repu, nepublikuje se |

## 🚀 Deploy

Push na `master` → GitHub Actions → GitHub Pages. Publikuje se jen `index.html` + `planner.html` + `data/`, `media/`, `public/`.

> Repo musí zůstat **veřejné** — na free účtu GitHub Pages fungují jen na veřejných repozitářích. Pokud repo zprivatizuješ, stránka přestane fungovat.
