# Design: V1 Improvements + v3music

> 2026-05-27 | Paprckovi Svatba 2026

## Overview

Two-track improvement:
1. **v1 production** — hide completed tasks toggle, collapsed budget by default
2. **v3music** — v1 copy + background audio player (2 songs), deploy switch via Actions

## 1. V1 Improvements (`index.html`)

### 1.1 Hide Completed Tasks Toggle

| Attribute | Value |
|-----------|-------|
| **Position** | Right side of filter bar `[Mamka][Tatka]...[Zobraz hotové ●]` |
| **Default** | ON (completed tasks hidden) |
| **Storage** | `localStorage` key `svatba_hide_done` (boolean) |
| **Logic** | AND with person filters — "Mamka + hide done" = only active Mamka tasks |
| **Scope** | Main task list + mandatory summary section |
| **Progress bar** | Unaffected — always counts 37 total, 6 done |

### 1.2 Budget Collapsed

| Attribute | Value |
|-----------|-------|
| **Default** | Collapsed — show only total sum + expand button |
| **Expanded** | Full budget table (existing behavior) |
| **Storage** | `localStorage` key `svatba_budget_collapsed` (boolean) |
| **Transition** | CSS height transition on expand/collapse |

## 2. V3music (`v3music/index.html`)

### 2.1 Base

Copy of v1 `index.html` with identical structure, CSS, and task management logic.

### 2.2 Audio Player

| Attribute | Value |
|-----------|-------|
| **Tracks** | `media/Sweet_Caroline_Remix.mp3` (DJ Ötzi, 3:26, refrain ~1:05), `media/Sweet_Caroline_Hoff.mp3` (Hasselhoff, 3:43, refrain ~1:08) |
| **Track switch** | Button to toggle between tracks |
| **Refrain start** | `audio.currentTime = refrainTimestamp` on play |
| **Format** | MP3 only (universal browser support) |

### 2.3 Audio Controls (3 synchronized)

| Control | Location | Behavior |
|---------|----------|----------|
| **Header button** | Next to title | 🔊/🔇 toggle, shows current track |
| **Floating button** | Bottom-right, fixed | Play/pause, thumb-accessible |
| **First-tap autoplay** | Anywhere in app | First user interaction starts audio |

All three share one `isPlaying` state. iOS PWA: audio starts only after user gesture (Safari restriction).

### 2.4 Storage

| Key | Purpose |
|-----|---------|
| `svatba_audio_playing` | Play state |
| `svatba_audio_track` | Current track index |
| `svatba_audio_time` | Last position |

(Plus all existing v1 localStorage keys)

## 3. Deploy Switch

### 3.1 DEPLOY_DEFAULT File

```
Repo root: DEPLOY_DEFAULT
Content:  v1 (one line, no trailing newline)
```

### 3.2 GitHub Actions Logic

```
deploy.yml reads DEPLOY_DEFAULT:
  if "v1"        → cp index.html deploy_out/ (v1 as /)
  if "v3music"   → cp v3music/index.html deploy_out/ (v3music as /)

Always deploys: v0/, v2/, v3music/, Older/, Older_up2date/, public/

After deploy: commit back DEPLOY_DEFAULT with "v1" (safe default)
```

### 3.3 Usage

```
User edits DEPLOY_DEFAULT → "v3music"
User pushes
Actions deploys v3music as /
Actions resets DEPLOY_DEFAULT → "v1"
Next push without edit → v1 back as /
```

## 4. Impact Analysis — Files to Update

| File | Action | Reason |
|------|--------|--------|
| `index.html` | Edit | Add hide-done toggle + budget collapse |
| `v3music/index.html` | **New** | Copy v1 + audio player |
| `.github/workflows/deploy.yml` | Edit | Add v3music copy + DEPLOY_DEFAULT logic |
| `DEPLOY_DEFAULT` | **New** | Default version selector |
| `.gitignore` | Edit | Ensure media/*.mp3 is NOT ignored |
| `CLAUDE.md` | Edit | Add v3music to version table, update deploy section |
| `README.md` | Edit | Add v3music link to quick links |
| `walkthrough.md` | Edit | Add v3music to version table, deployment |
| `CHANGELOG.md` | Edit | Add 1.3.2 entry |
| `media/*.mp3` | Git add | Only the 2 needed mp3 files (~9MB) |

### Media Files to Commit

| File | Size | Needed |
|------|------|--------|
| `media/Sweet_Caroline_Remix.mp3` | 4.4 MB | YES |
| `media/Sweet_Caroline_Hoff.mp3` | 4.8 MB | YES |
| Other 7 files (.mp4, .m4a, original) | ~29 MB | NO — skip |

## 5. localStorage Keys Summary

| Key | Version | Purpose |
|-----|---------|---------|
| `svatba_done_v4` | v1/v2/v3music | Completed task IDs |
| `svatba_budget_v4` | v1/v2/v3music | Budget edits |
| `svatba_hide_done` | **NEW** | Hide completed toggle |
| `svatba_budget_collapsed` | **NEW** | Budget collapse state |
| `svatba_audio_playing` | **NEW** v3music only | Audio play state |
| `svatba_audio_track` | **NEW** v3music only | Current track index |
| `svatba_audio_time` | **NEW** v3music only | Playback position |
