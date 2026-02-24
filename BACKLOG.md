# Zone Defence — Development Backlog

## 📖 TERMINOLOGY
- **Universe** = themed stage/world (e.g. Andromeda). Each introduces new mechanics.
- **Constellation** = individual playable level within a universe (e.g. Orion). Named after real constellations.
- **Round** = one attempt/life within a constellation.

**Last updated:** 2026-02-24
**Game:** Qix-style territory capture across constellations
**Live:** https://zone-defence.kbot.uk
**Status:** Playable with 12 levels, 5 ships, 7 enemy types, auto-shooting, capture kills

---

## ✅ COMPLETED

- [x] Core Qix gameplay (move on border, cut through void, claim territory)
- [x] 12 constellation-themed levels across 3 galaxies (Inner Rim → Deep Void → Outer Reach)
- [x] Real constellation star patterns as level backgrounds (Orion, Lyra, Cassiopeia, etc.)
- [x] Galaxy groupings with transition announcements
- [x] 7 enemy types: Patrol, Hunter, Phase, Tracer, Armor, Orbit, Split
- [x] Auto-shooting system (fires in movement direction)
- [x] Capture kills (enclose enemies in claimed zone for +500)
- [x] 5 unlockable ships (Viper, Phantom, Titan, Pulse, Nova) with unique stats
- [x] Ship hangar screen with stat bars and preview
- [x] Stars unlock system for ships
- [x] 4 power-ups with drawn icons (Speed, Shield, +1 Life, Slow)
- [x] Pickup radius with visual indicator
- [x] Efficiency ranking (S/A/B/C based on cuts count)
- [x] Smooth player interpolation (sub-pixel movement)
- [x] Smooth trail rendering (3-layer glow line)
- [x] Clean territory visuals (dark fill + edge glow)
- [x] Constellation star chart (map screen) with galaxy labels
- [x] Fullscreen with landscape lock on mobile
- [x] Auto-pause on tab switch (prevents black screen)
- [x] Moveable d-pad (lock/unlock, drag to reposition, saved position)
- [x] Swipe controls + d-pad + keyboard input
- [x] HUD with score, cuts counter, zone %, lives, pause button
- [x] Retro menus with scanlines, modern gameplay without

---

## 🔥 PRIORITY 1 — Music & Audio

### 1.1 Background Music
- [ ] Procedural/synthesized background music using Web Audio API
- [ ] Different tracks per galaxy (ambient for Inner Rim, tense for Deep Void, epic for Outer Reach)
- [ ] Dynamic music that intensifies when cutting (in the void) vs calm on border
- [ ] Boss level music for Phoenix (level 12)
- [ ] Music volume control + mute toggle in pause menu

### 1.2 Sound Effects Upgrade
- [ ] More satisfying claim sound (layered, bassy)
- [ ] Unique sounds per enemy type (phase warp, orbit hum, split crack)
- [ ] Bullet impact variations
- [ ] Capture kill fanfare
- [ ] Power-up collect jingle per type
- [ ] Low health warning pulse
- [ ] Galaxy transition cinematic sound

---

## 🎨 PRIORITY 2 — Graphics & Visual Polish

### 2.1 Sprite System
- [ ] Build a canvas-based sprite generator for ships and enemies
- [ ] Each ship gets a detailed multi-frame sprite (idle, thrusting, cutting, damaged)
- [ ] Animated engine flames per ship type
- [ ] Ship colour skins (unlockable cosmetics separate from ship type)
- [ ] Damage flash / hit animation on player ship

### 2.2 Enemy Sprites
- [ ] Unique visual identity per enemy type (not just colour + label)
  - Patrol: standard drone
  - Hunter: red aggressive ship with tracking eye
  - Phase: shimmering ghost ship that fades in/out
  - Tracer: green snake-like trail follower
  - Armor: bulky shielded tank with visible shield layers
  - Orbit: spinning ring/satellite
  - Split: organic blob that visibly divides
- [ ] Enemy death animations (explosion, dissolve, split animation)
- [ ] Health bars on Armor enemies

### 2.3 Territory & Environment
- [ ] Animated claimed territory (subtle pulse, energy flow lines)
- [ ] Different territory colours per galaxy/constellation
- [ ] Trail particles while cutting (sparks, energy wisps)
- [ ] Better border glow (animated pulse)
- [ ] Nebula/space dust parallax layers in background
- [ ] Constellation lines that illuminate as you claim territory over them

### 2.4 UI Polish
- [ ] Animated score counter (rolls up)
- [ ] Screen flash on big claims
- [ ] Better floating text (scale + fade, not just drift up)
- [ ] Level intro cinematic (constellation draws itself with star connections lighting up)
- [ ] Win screen with fireworks/particle celebration
- [ ] Smoother menu transitions (fade in/out)

---

## 🗺️ PRIORITY 3 — Map & Level Navigation

### 3.1 Walkable Star Chart
- [ ] Replace click-to-select with a moveable avatar/ship icon on the map
- [ ] Player flies their selected ship between constellation nodes
- [ ] Animated travel path between stars
- [ ] Unlock visual: locked constellations are dim/grey, unlocked ones glow
- [ ] Galaxy boundaries visible (nebula regions, colour zones)
- [ ] Zoom in/out on map (pinch on mobile)

### 3.2 Level Format Improvements
- [ ] Variable grid shapes per level (not always rectangle)
  - Some levels could have L-shapes, islands, corridors
- [ ] Obstacle cells in the grid (rocks/asteroids you can't claim through)
- [ ] Warp zones that teleport you to another edge
- [ ] Timed bonus zones (claim this area within X seconds for mega bonus)
- [ ] "Challenge" variant for each level (harder target %, less lives, leaderboard)

---

## 🚀 PRIORITY 4 — Ships & Progression

### 4.1 Ship Skins
- [ ] Multiple colour skins per ship (unlocked by completing levels with that ship)
- [ ] Skin preview in hangar
- [ ] Special skins for 3-starring all levels in a galaxy
- [ ] Animated/glowing legendary skins

### 4.2 Ship Upgrades
- [ ] Upgrade paths per ship (spend stars to improve stats)
- [ ] Upgrade tree: Speed → Trail Speed → Fire Rate → Bullet Damage → Special
- [ ] Visual upgrades reflected on the ship sprite (bigger engines, more guns)

### 4.3 New Ships (future)
- [ ] **Wraith** — Cloaks when not moving (enemies lose track)
- [ ] **Bomber** — Slow fire but area-of-effect bullets
- [ ] **Swarm** — Deploys mini-drones that auto-target enemies
- [ ] **Architect** — Trail is thicker (claims more territory per cut)

---

## 👾 PRIORITY 5 — Enemy Improvements

### 5.1 New Enemy Types
- [ ] **Minelayer** — drops mines on empty cells that damage trail
- [ ] **Mirror** — copies your movement direction with a delay
- [ ] **Berserker** — normally slow, enrages (goes fast + red) when you start cutting
- [ ] **Healer** — slowly repairs claimed territory back to empty
- [ ] **Boss enemies** — large multi-cell enemies with attack patterns for galaxy finales

### 5.2 Enemy Visual Upgrade
- [ ] Animated sprites (wing flapping, eye tracking, engine glow)
- [ ] Type-specific particle trails
- [ ] Warning indicators before phase teleport or berserker enrage
- [ ] Mini health bars for multi-hit enemies

---

## 🏆 PRIORITY 6 — Scoring & Achievements

### 6.1 Achievements System
- [ ] Achievement popups (first claim, first capture kill, S-rank, etc.)
- [ ] Achievement gallery screen
- [ ] Achievement-based unlocks (skins, ships)

### 6.2 Leaderboard
- [ ] Per-level high scores
- [ ] Total score leaderboard
- [ ] Best efficiency rank per level
- [ ] Fewest cuts record

### 6.3 Daily Challenge
- [ ] Procedurally generated daily level with fixed seed
- [ ] Unique enemy composition each day
- [ ] Daily leaderboard

---

## 📱 PRIORITY 7 — Mobile & UX

### 7.1 Controls
- [ ] Haptic feedback on mobile (vibrate on hit, claim, death)
- [ ] D-pad opacity/size slider in settings
- [ ] Alternative control: virtual joystick mode
- [ ] Two-thumb mode (left thumb = move, right thumb = special ability)

### 7.2 Settings Screen
- [ ] Music volume slider
- [ ] SFX volume slider
- [ ] Control scheme selection
- [ ] D-pad size/opacity
- [ ] Reset progress option

### 7.3 PWA / Install
- [ ] Service worker for offline play
- [ ] Manifest.json for "Add to Home Screen"
- [ ] App icon

---

## 🔮 FUTURE / STRETCH

- [ ] Multiplayer: competitive territory race (WebSocket)
- [ ] Level editor: create and share custom levels
- [ ] Story mode: brief narrative between galaxies
- [ ] Endless mode: procedurally generated infinite levels
- [ ] Replay system: watch your best runs
- [ ] Twitch integration: viewers vote on enemy spawns

---

## 📋 IMMEDIATE NEXT STEPS (suggested order)

1. **Music** — Procedural background music (biggest immersion impact)
2. **Enemy sprites** — Unique visuals per type (readability + polish)
3. **Walkable map** — Avatar navigation on star chart
4. **Ship skins** — Cosmetic unlocks for replayability
5. **Level intro cinematic** — Constellation draw animation
6. **Settings screen** — Volume controls, d-pad options
7. **PWA manifest** — Installable on mobile home screen

## Snake/Formation Enemies (Later Levels)
- Enemies that fly in patterns: lines, snake-like forms
- Player can follow and pick them off along a path
- Introduce in later universe levels for variety

