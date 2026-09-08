---
name: People Rules
description: Enforce naming conventions — Deti never removed, no surnames, no hacek on Mikesovi
---

---

> ⚠️ **LEGACY — pozor.** Tento check cílí na zrušené `data/*.md`
> soubory (tasks.md, guests.md) a `v2/`. Dnes jsou data v `data/*.csv`
> a platná jména pro úkoly: Mamka, Taťka, Žanetka, Kikinka, Děti
> (novomanželé po svatbě = **Dagmar + Martin Paprčkovi**).

If no file touching person names was changed (`data/tasks.md`, `data/guests.md`, `CLAUDE.md`, `index.html`, `v2/index.html`), no action is needed.

When these files change, verify:

## 1. Deti never removed from any task

- Search for all `Kdo` column values in tasks.md (pipe column index 3).
- **Děti** (or **Deti**) must appear as assignee on at least one task. If zero appearances, FAIL.
- If a task previously had Děti and the diff removes them, FAIL — Děti can only be co-assigned (`Děti, Mamka`), never replaced.

## 2. Only allowed people as assignees

Allowed people: `Mamka`, `Taťka`, `Žanetka`, `Kikinka`, `Děti`

- Every value in the `Kdo` column (split by comma) must be one of these five names.
- Variants with hacek (`Žanetka`, `Taťka`, `Děti`) are the canonical forms and are OK.
- Unknown names or surnames: FAIL.

## 3. No surnames

- No surname should appear in `Kdo` column or in People table.
- Allowed: first names or nicknames only (Mamka, Taťka, Žanetka, Kikinka, Děti).

## 4. Mikesovi without hacek

- If `Mikešovi` (with hacek on s) appears in any data file: FAIL. Must be `Mikesovi`.
- Search pattern: `Mikeš`

## 5. People table in tasks.md

The people table lists 5 rows: Mamka, Taťka, Žanetka, Kikinka, Děti. Verify:
- All 5 present
- No extra rows
- Task count per person matches actual task assignments (a task with `Děti, Mamka` counts for both)
