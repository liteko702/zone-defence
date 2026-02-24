# Zone Defence — Development Roadmap

**Last updated:** 2026-02-24
**Live:** https://zone-defence.kbot.uk

---

## 🎯 CURRENT SPRINT: Phase 1 — Zoomable Star Chart

### Phase 1: Zoomable Star Chart + Level Info
- [ ] Wide view showing all 3 galaxies with constellation shapes as clusters
- [ ] Tap/pinch a constellation to zoom in smoothly
- [ ] Zoomed view shows each star as a level node within the constellation shape
- [ ] Selected level shows enemy breakdown tooltip (types, count, difficulty)
- [ ] Back/pinch-out to zoom back to galaxy wide view
- [ ] Smooth animated transitions between zoom levels

### Phase 2: Constellation = Multiple Levels (expand content)
- [ ] Each constellation's real stars become individual levels (Orion=7, Cygnus=5, etc.)
- [ ] Levels follow the constellation shape — progress star to star
- [ ] ~50+ levels total (up from 12)
- [ ] Progressive difficulty curve within each constellation
- [ ] Save system bump to `zd6`
- [ ] Enemy composition per level defined in data

### Phase 3: Constellation Bosses (varied types)
- [ ] Final star in each constellation = boss fight
- [ ] **Andromeda bosses** (easy): Big armored enemy, simple dodge patterns
- [ ] **Milky Way bosses** (medium): Fires rockets at player, shoot to break apart
- [ ] **Nebula Prime bosses** (hard): Phase-shifting, splits, shoots back, complex patterns
- [ ] Boss health bar UI
- [ ] Unique boss music per galaxy (need `boss.mp3`)

### Phase 4: Enemy Sprites & Visual Polish
- [ ] Unique drawn sprite per enemy type (not just coloured circles)
  - Patrol: standard drone
  - Hunter: red aggressive ship with tracking eye
  - Phase: shimmering ghost that fades in/out
  - Tracer: green snake-like trail follower
  - Armor: bulky shielded tank
  - Orbit: spinning ring/satellite
  - Split: organic blob that divides
- [ ] Boss sprites (unique per galaxy)
- [ ] Ship sprite improvements (multi-frame, engine flames)

### Phase 5: Polish & Content
- [ ] Ship skins (cosmetic colour variants per ship)
- [ ] Level intro cinematic (constellation draws itself)
- [ ] Settings screen (volume sliders, d-pad size/opacity)
- [ ] PWA manifest + service worker for mobile install
- [ ] Walkable star chart with flyable ship avatar

---

## ✅ COMPLETED

### Audio System ✓
- [x] External music via MP3 files (menu, theme, galaxy1-3)
- [x] Music crossfading between scenes
- [x] 24 synthesized SFX (v2 futuristic)
- [x] Per-SFX volume levels
- [x] Music mute toggle
- [x] Suno generation guide + manifest

### Star Chart v1 ✓
- [x] Galaxy-separated views with ◄ ► navigation
- [x] Swipe between galaxies on mobile
- [x] Galaxy dot indicators
- [x] Constellation background pattern for selected level

### Core Game ✓
- [x] 12 levels across 3 galaxies
- [x] 7 enemy types
- [x] 5 ships with unique stats
- [x] Auto-shooting (Galaxy 2+)
- [x] Capture kills, power-ups, efficiency ranking
- [x] Smooth interpolation, trail glow, territory visuals
- [x] Mobile controls (d-pad + swipe + keyboard)
- [x] Fullscreen landscape lock

---

## 🎵 AUDIO STILL NEEDED
- [ ] `boss.mp3` — Boss level music (waiting for Suno tokens)
- [ ] `victory.mp3` — Level complete sting
- [ ] `gameover.mp3` — Game over sting
- [ ] `pause.mp3` — Pause screen ambient

---

## 📝 NOTES
- Save key: `zd5` (will bump to `zd6` when level count changes)
- Single file: `index.html` (~1600 lines)
- Audio files: `audio/` directory (served by Caddy)
- Reminder set: Tomorrow 10am UTC for remaining Suno tracks
