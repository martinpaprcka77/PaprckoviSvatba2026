# Rozpočet — Svatba Paprčkovi 2026

> **Autoritativní zdroj rozpočtu.** Jediný zdroj pravdy pro peníze.
> Editace: PC → git. Appka pouze zobrazuje (žádný zápis z appky).
> Odhad: [`data/tasks.md`](tasks.md) (Plán Kč)
> **MAX 100 000 Kč hard cap.** Nad 100 000 = červená.

## Přehled

| Kategorie | Položek | Odhad (Kč) | Rezervováno (Kč) | Zaplaceno (Kč) | Zbývá (Kč) |
|-----------|---------|-----------|------------------|----------------|-------------|
| 🔴 Povinné (mandatory) | 19 | 94 500 | _ | _ | _ |
| 🟡 Důležité (important) | 14 | 5 000 | _ | _ | _ |
| 🟢 Volitelné (optional) | 4 | 500 | _ | _ | _ |
| **CELKEM** | **37** | **100 000** | _ | _ | _ |

> Zbývá = Rezervováno − Zaplaceno. Vyplňuje se při platbách.

## Položky

| # | Položka | Kat. | Odhad (Kč) | Rezerv (Kč) | Zaplac (Kč) | Zbývá (Kč) | Poznámka |
|---|---------|------|-----------|-------------|-------------|------------|----------|
| 1 | Termín konfirmace | M | 0 | _ | _ | _ | ✅ Hotovo |
| 2 | Návštěva radnice | M | 0 | _ | _ | _ | ✅ Hotovo |
| 3 | Informování dětí | M | 0 | _ | _ | _ | ✅ Hotovo |
| 4 | Svědci domluveni | M | 0 | _ | _ | _ | ✅ Hotovo |
| 5 | Domluva oddávajícího | M | 0 | _ | _ | _ | ✅ Hotovo |
| 6 | Svatební oznámení | M | 1 500 | _ | _ | _ | _ |
| 7 | **Zlatá koliba** | M | 30 000 | _ | _ | _ | Viz rozpad ↓ |
| 8 | Svatební šaty (Mamka) | M | 12 000 | _ | _ | _ | Plán 11 100, max 15 000 |
| 9 | Oblek a sako (Taťka) | M | 8 000 | _ | _ | _ | _ |
| 10 | Prstýnky | M | 20 000 | _ | _ | _ | Vyhlédnuty 25. 5. |
| 11 | Finální seznam hostů | M | 0 | _ | _ | _ | _ |
| 12 | Nápoje a bar | M | 6 000 | _ | _ | _ | Součást domluvy s Milošem |
| 13 | Doplňky (Mamka) | M | 3 000 | _ | _ | _ | _ |
| 14 | Ubytování pro hosty | M | 5 000 | _ | _ | _ | _ |
| 15 | Dekorace a květiny (radnice) | M | 3 000 | _ | _ | _ | _ |
| 16 | Doprava (radnice → koliba) | M | 3 000 | _ | _ | _ | _ |
| 17 | Svatební dort | M | 3 000 | _ | _ | _ | Děti, Mamka |
| 18 | Oddací list, podpisy, doklady | M | 0 | _ | _ | _ | _ |
| 19 | Změna příjmení (Mamka) | M | 0 | _ | _ | _ | Po svatbě |
| 20 | Schůzka — prstýnky | I | 0 | _ | _ | _ | ✅ Hotovo |
| 21 | Rozlučka se svobodou | I | 0 | _ | _ | _ | Žanetka zorganizuje |
| 22 | Dárky pro svědky | I | 500 | _ | _ | _ | _ |
| 23 | Dekorace Zlaté koliby | I | 1 000 | _ | _ | _ | Děti |
| 24 | Dárky pro rodiče | I | 500 | _ | _ | _ | _ |
| 25 | První tanec (nácvik) | I | 0 | _ | _ | _ | _ |
| 26 | Fotokoutek / selfie zóna | I | 1 000 | _ | _ | _ | Děti |
| 27 | Uvítací cedule | I | 0 | _ | _ | _ | _ |
| 28 | Dárky na přivítanou | I | 0 | _ | _ | _ | _ |
| 29 | Hry pro hosty | I | 0 | _ | _ | _ | _ |
| 30 | Hudba a playlist | I | 0 | _ | _ | _ | Děti |
| 31 | Proslovy | I | 0 | _ | _ | _ | _ |
| 32 | Líčení / nehty / vlasy (Mamka) | I | 1 500 | _ | _ | _ | _ |
| 33 | Střih a úprava (Taťka) | I | 500 | _ | _ | _ | _ |
| 34 | Svatební cesta | O | 0 | _ | _ | _ | _ |
| 35 | Drobnosti pro hosty (guestbook + favory) | O | 500 | _ | _ | _ | _ |
| 36 | Confetti a prskavky | O | 0 | _ | _ | _ | _ |
| 37 | Fotograf / dokumentace | O | 0 | _ | _ | _ | Děti |

## Rozpady

Složené položky s vnitřním rozpočtem.

### #7 — Zlatá koliba (30 000 Kč)

| # | Položka | Částka (Kč) | Kalkulace | Poznámka |
|---|---------|------------|-----------|----------|
| 7a | **Pohoštění (společný oběd)** | **11 100** | SUMA(7a1+7a2) | Záloha před obědem |
| 7a1 | · Polévka | 2 850 | 95 Kč × 30 os | U Miloše |
| 7a2 | · Druhé jídlo | 8 250 | 275 Kč × 30 os | U Miloše |
| 7b | **Poobědový budget** | **18 900** | 30 000 − 11 100 | Nápoje, bar, servis |
| | **Celkem** | **30 000** | | ✅ |

```
Oběd:      (95 + 275) × 30 os = 11 100 Kč
Po obědě:  30 000 − 11 100    = 18 900 Kč
Celkem:                       30 000 Kč ✓
```

## Ověření

```python
# Spustit po každé změně:
# python -c "
# Odhad: 19M + 14I + 4O = 37 položek = 100 000 Kč
# mandatory: 19 items, 94 500 Kč
# important: 14 items, 5 000 Kč
# optional:  4 items, 500 Kč
# CELKEM:  37 items, 100 000 Kč ✓
# "
```
