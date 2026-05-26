> ⚠️ **Historický dokument** — květen 2025. Aktuální stav: 37 úkolů, 6/37 hotovo, 5 osob, 100 000 Kč. Autoritativní data v data/tasks.md.
# Task Checklist - iOS Wedding Planner & PRD Sync

- `[x]` **Phase 1: Foundation & Data Sync**
  - `[x]` Expand default tasks array to match PRD's 35 tasks exactly
  - `[x]` Upgrade storage keys to `svatba_state_v3` and `svatba_tasks_v3`
  - `[x]` Add support for 5 people in filters (Mamka, Taťka, Žanetka, Kikinka, Děti)
  - `[x]` Implement automatic completed task preset for IDs 1-5
  - `[x]` Extend month names to include September (`2026-09`)
- `[x]` **Phase 2: Premium iOS UI/UX Redesign**
  - `[x]` Integrate elegant Google Fonts (Outfit, Playfair Display)
  - `[x]` Apply glassmorphic styles with `backdrop-filter: blur`
  - `[x]` Upgrade navigation and bottom tab bar to feel native iOS
  - `[x]` Implement iOS Bottom Sheet Modal overlay system with pull-down handle
  - `[x]` Improve touch targets to Apple standards (min 44px)
  - `[x]` Introduce smooth touch scale animations and custom animated checkboxes
  - `[x]` Add automatic system dark mode support and a toggle
  - `[x]` Add PWA capabilities (Manifest metadata, icon support)
- `[x]` **Phase 3: Interactive Planning Features**
  - `[x]` Create dynamic "Add Task" bottom sheet modal
  - `[x]` Create dynamic "Edit Task" bottom sheet modal
  - `[x]` Implement delete task option
  - `[x]` Enforce 100,000 Kč budget hard cap with iOS suggestion overlay for offsets
- `[x]` **Phase 4: Verification & Polish**
  - `[x]` Run automated integrity tests
  - `[x]` Review visual look at mobile widths
  - `[x]` Validate storage persistence and offline-ready standalone behavior
