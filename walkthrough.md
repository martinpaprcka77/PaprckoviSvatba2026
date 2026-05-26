> ⚠️ **Historický dokument** — květen 2026. Aktuální stav: 37 úkolů, 19 mandatory + 14 important + 4 optional, 5 osob. Autoritativní data v data/tasks.md.
# Technical Walkthrough — Wedding Planner & PRD Synchronization

This walkthrough details the major technical updates and structural synchronization achieved for **Svatba Paprčkovi 2026** static planner application. All spec-to-code gaps have been eliminated, and the user interface has been redesigned to look and feel like a premium, native iOS mobile application tailored for iPhone users.

---

## 1. Core PRD Data Synchronization

All gaps between the **Product Requirements Document (PRD)** and the codebase have been fully resolved:

- **Exact Task Matching:** Sync'd the default tasks array to contain precisely **35 tasks** (19 Mandatory, 12 Important, 4 Optional) with correct prices, assignees, timelines, and deadlines.
- **Budget Realignment:** Prices now sum up to exactly **100,000 Kč** across the categories:
  - **Mandatory:** 94,500 Kč (19 tasks)
  - **Important:** 5,000 Kč (12 tasks)
  - **Optional:** 500 Kč (4 tasks)
- **Assignee Filter Expansion:** Implemented fully reactive filters supporting all 5 PRD roles: `Mamka`, `Taťka`, `Žanetka`, `Kikinka`, and `Děti`.
- **Month Extension:** Expanded the timeline renderer to support September 2026 (`2026-09`) to capture post-wedding items (e.g. name changes).
- **Auto-Initialization:** The application now auto-completes tasks with IDs `1` to `5` upon first load.
- **Key Upgrade:** Upgraded `localStorage` keys to `svatba_state_v3` (for completed item IDs) and `svatba_tasks_v3` (for editable tasks data).

---

## 2. Premium iOS UI/UX Overhaul

The interface has been redesigned to deliver a luxury, app-like experience for iOS devices:

- **Typography & Aesthetics:** Integrated Google Fonts (`Outfit` for geometric sans UI, `Playfair Display` for elegant serif headings). Styled using a luxury palette of Rose Gold, Dusty Rose, Champagne Gold, and soft ivory cream, with full automatic dark mode support.
- **Touch-Friendly Layout:** Enhanced touch targets to at least `44px` in height and width. Added CSS `-webkit-tap-highlight-color: transparent` and instant active scaling triggers (`transform: scale(0.97)`) on press/touch states to emulate iOS physical haptics.
- **SVG Circular Progress Gauge:** An elegant, animated circular SVG progress indicator dynamically displays the percentage of completed tasks alongside the `completed/total` fraction.
- **Horizontal swipeable "Must-Do" Feed:** A beautiful horizontal carousel display specifically highlighting pending mandatory tasks for quick access.
- **iOS Bottom Navigation Tab Bar:** A fixed glassmorphic bottom navigation tab bar utilizing `backdrop-filter: blur(20px)` and safe-area padding (`env(safe-area-inset-bottom)`) for notch-less and notched iPhones.
- **PWA Ready:** Enabled full standalone mode using standalone Web App Manifests, meta tags, and high-quality Apple touch icons so the couple can "Add to Home Screen" and use it as a native iOS app.

---

## 3. Interactive Planning & Budget Guardrails

To facilitate active planning, the app includes fully interactive task management:

- **iOS Bottom Sheets:** Created native-looking bottom sheets sliding up from the bottom with a dark backdrop overlay and a top swipe drag handle. These are used for **Přidat nový úkol** (Add Task) and **Upravit úkol** (Edit/Delete Task).
- **Hard Cap Budget Protection:** Every task creation or price change is vetted in real-time. If an edit or new task overruns the **100,000 Kč budget cap**, the app halts the operation and pops up an elegant **Rozpočet překročen!** sheet.
- **Cost-Reduction Suggestions:** The overrun sheet computes the excess cost and dynamically renders cost-reduction recommendations within the Important/Optional categories. A **"Zrušit cenu"** (Quick Cut) button allows users to immediately drop a voluntary cost to 0 Kč to quickly balance the budget.

---

## 4. Verification Results

### Automated Data Integrity Script
We executed the authoritative Node.js verification script directly against the newly synchronized code. The results confirm a **100% perfect match** with the PRD requirements:

```
Tasks: 35 (target: 35) | Budget: 100000 (target: 100000)
Mand: 94500 Imp: 5000 Opt: 500
OK - matches PRD
Storage key version: 3
```

### Build & Deploy Status
- Staged, committed, and pushed changes successfully.
- Triggered GitHub Actions deploy workflow, deploying the updated `v3` app to:  
  👉 [Live Planner Page](https://doma77git.github.io/PaprckoviSvatba2026/)
