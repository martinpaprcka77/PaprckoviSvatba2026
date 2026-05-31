# Rozpočet — Svatba Paprčkovi 2026

> **Autoritativní zdroj rozpočtu.** Jediný zdroj pravdy pro peníze.
> Editace: PC → git. Appka pouze zobrazuje (žádný zápis z appky).
> Odhad: [`data/tasks.md`](tasks.md) (Plán Kč)
> **MAX 100 000 Kč hard cap.** Nad 100 000 = červená.

## Přehled

| Kategorie | Položek | Odhad (Kč) |
|-----------|---------|-----------|
| 🔴 Povinné (mandatory) | 19 | 84 500 |
| 🟡 Důležité (important) | 13 | 4 500 |
| 🟢 Volitelné (optional) | 4 | 500 |
| **CELKEM** | **36** | **89 500** |

**MAX 100 000 Kč hard cap** — máme rezervu 10 500 Kč.

## Položky

| # | Položka | Kat. | Odhad (Kč) | Poznámka |
|---|---------|------|-----------|----------|
| 1 | Termín konfirmace | M | 0 | ✅ Hotovo |
| 2 | Návštěva radnice | M | 0 | ✅ Hotovo |
| 3 | Informování dětí | M | 0 | ✅ Hotovo |
| 4 | Svědci domluveni | M | 0 | ✅ Hotovo |
| 5 | Domluva oddávajícího | M | 0 | ✅ Hotovo |
| 6 | Svatební oznámení | M | 1 500 | — |
| 7 | **Zlatá koliba** | M | 30 000 | Viz rozpad ↓ |
| 8 | Svatební šaty (Mamka) | M | 12 000 | Plán 11 100, max 15 000 |
| 9 | Oblek a sako (Taťka) | M | 8 000 | — |
| 10 | Prstýnky | M | 10 000 | Vyhlédnuty 25. 5. |
| 11 | Finální seznam hostů | M | 0 | — |
| 12 | Nápoje a bar | M | 6 000 | Součást domluvy s Milošem |
| 13 | Doplňky (Mamka) | M | 3 000 | — |
| 14 | Ubytování pro hosty | M | 5 000 | — |
| 15 | Dekorace a květiny (radnice) | M | 3 000 | — |
| 16 | Doprava (radnice → koliba) | M | 3 000 | — |
| 17 | Svatební dort | M | 3 000 | Děti, Mamka |
| 18 | Oddací list, podpisy, doklady | M | 0 | — |
| 19 | Změna příjmení (Mamka) | M | 0 | Po svatbě |
| 20 | Schůzka — prstýnky | I | 0 | ✅ Hotovo |
| 21 | Rozlučka se svobodou | I | 0 | Žanetka zorganizuje |
| 22 | Dárky pro svědky | I | 500 | — |
| 23 | Dekorace Zlaté koliby | I | 1 000 | Děti |
| 24 | První tanec (nácvik) | I | 0 | — |
| 25 | Fotokoutek / selfie zóna | I | 1 000 | Děti |
| 26 | Uvítací cedule | I | 0 | — |
| 27 | Dárky na přivítanou | I | 0 | — |
| 28 | Hry pro hosty | I | 0 | — |
| 29 | Hudba a playlist | I | 0 | Děti |
| 30 | Proslovy (svědci) | I | 0 | — |
| 31 | Líčení / nehty / vlasy (Mamka) | I | 1 500 | — |
| 32 | Střih a úprava (Taťka) | I | 500 | — |
| 33 | Svatební cesta | O | 0 | — |
| 34 | Drobnosti pro hosty (guestbook + favory) | O | 500 | — |
| 35 | Confetti a prskavky | O | 0 | — |
| 36 | Fotograf / dokumentace | O | 0 | Děti |

## Rozpady

Složené položky s vnitřním rozpočtem.

### #7 — Zlatá koliba (30 000 Kč)

| # | Položka | Částka (Kč) | Kalkulace | Poznámka |
|---|---------|------------|-----------|----------|
| 7a | **Pohoštění (společný oběd)** | **9 250** | SUMA(7a1+7a2) | Záloha před obědem |
| 7a1 | · Polévka | 2 375 | 95 Kč × 25 os | U Miloše |
| 7a2 | · Druhé jídlo | 6 875 | 275 Kč × 25 os | U Miloše |
| 7b | **Poobědový budget** | **20 750** | 30 000 − 9 250 | Nápoje, bar, servis |
| | **Celkem** | **30 000** | | ✅ |

```
Oběd:      (95 + 275) × 25 os = 9 250 Kč
Po obědě:  30 000 − 9 250     = 20 750 Kč
Celkem:                       30 000 Kč ✓
```

## Ověření

```python
# Spustit po každé změně:
# python -c "
# Odhad: 19M + 13I + 4O = 36 položek = 89 500 Kč
# mandatory: 19 items, 84 500 Kč
# important: 13 items, 4 500 Kč
# optional:  4 items, 500 Kč
# CELKEM:  36 items, 89 500 Kč ✓
# "
```
