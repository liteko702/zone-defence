# Zone Defence — Design Document

**Live:** https://zone-defence.kbot.uk
**GitHub:** https://github.com/liteko702/zone-defence
**Discord:** #zone-defence
**Updated:** 2026-02-27

---

## Concept
Space-themed Qix-style territory capture game. Player pilots a spaceship along the border of a zone, ventures into unclaimed space to draw lines, and returns to claim territory. Enemies patrol the unclaimed area. Retro arcade feel with modern polish.

## Visual References
- **TRON arcade** — glowing neon lines, dark grid, light cycle territory claiming
- **Galaxy Attack / Space Shooter** — detailed ships, glowing engines, score popups, boss fights
- **Bubble Bobble** — retro pixel art, arcade HUD, chunky feel
- **Candy Crush** — winding level select map with nodes, stars, progression

## Design Principles
1. **Easy to learn, hard to master** — simple controls, deep strategy
2. **Juice everywhere** — particles, screen shake, popups, sound
3. **Retro soul, modern polish** — pixel font + smooth animations
4. **Always expandable** — modular enemy/level/power-up system
5. **Mobile-first** — touch controls, portrait-friendly
6. **No ads, no paywalls** — pure game

## Tech
- Single HTML file, no build step
- Canvas 2D rendering
- Web Audio API for SFX + synth music fallback
- localStorage for saves (`zd6`)
- Static hosting (Caddy)
- ~3200 lines

---

## ✅ WHAT'S BUILT (Current State)

### Core Gameplay ✅
- Qix territory claiming (border movement, trail cutting, flood-fill)
- 7 enemy types with unique behaviours + boss type
- 6 unlockable ships (Viper/Striker/Phantom/Titan/Pulse/Nova)
- Auto-shooting (per ship `canShoot`)
- Capture kills (+500), 4 power-up types (Speed/Shield/Life/Slow)
- Star ratings (1-3 per level), coin economy
- Fullscreen landscape lock, auto-pause, moveable d-pad
- Settings cog (⚙) with music/SFX toggles + volume sliders + d-pad size

### Map System ✅
- Two-level zoom: galaxy view → constellation view
- Galaxy ◄ ► navigation + swipe between galaxies
- Constellation view with enemy info panel
- Smooth animated zoom transitions
- Tap-to-select, tap-again-to-play

### Ships & Hangar ✅
- Canvas-rendered hangar with stat bars + purchase flow
- 6 ships with unique stats (speed/trail/fire rate/damage/lives)
- Ship-specific trail colours in gameplay
- Ship-specific engine exhaust particles

### Audio ✅
- External MP3 music (menu, theme, galaxy1-3) + synth fallback
- Music crossfading between scenes
- 24 synthesised SFX
- Per-SFX volume control

### Visuals ✅
- Detailed ship sprites (per-type canvas art)
- Unique enemy sprites (patrol/hunter/phase/tracer/armor/orbit/split/boss)
- Animated starfield + debris background
- Particle effects, screen shake, floating score popups
- CRT scanlines overlay

---

## 🗺️ CURRENT GAME STRUCTURE

### 3 Galaxies × 4 Constellations + Boss

| Galaxy | Constellations | Levels | Boss |
|--------|---------------|--------|------|
| **ANDROMEDA** (blue) | Cassiopeia (5), Lyra (6), Cygnus (6), Aquila (7) | 24 + boss | Andromeda Guardian (8HP) |
| **MILKY WAY** (purple) | Perseus (8), Phoenix (8), Leo (9), Gemini (10) | 35 + boss | Milky Way Wyrm (12HP) |
| **NEBULA PRIME** (orange) | Sagittarius (10), Scorpius (12), Draco (12), Orion (13) | 47 + boss | Nebula Lord (18HP) |

**Total: 109 levels** (106 regular + 3 bosses)

### Enemy Types

| Enemy | Behaviour | Pool |
|-------|-----------|------|
| **Bounce** (Patrol Drone) | Bounces off walls randomly | Galaxy 0+ |
| **Chase** (Hunter) | Actively chases the player | Galaxy 0+ |
| **Tracer** (Serpent Drone) | Follows player trails | Galaxy 1+ |
| **Shield** (Armor Tank) | Takes 2 hits to kill | Galaxy 1+ |
| **Split** (Biomech) | Splits into 2 bouncers when killed | Galaxy 1+ |
| **Phase** (Crystal Ship) | Phases in/out — invulnerable while phased | Galaxy 2+ |
| **Orbit** (Ring Drone) | Moves in circular orbit patterns | Galaxy 2+ |

### Ships

| Ship | Cost | Speed | Trail | Shoots? | Special |
|------|------|-------|-------|---------|---------|
| Viper | FREE | 9 | 7 | ❌ | Pure speed |
| Striker | 300🪙 | 7 | 6 | ✅ (0.35s) | Standard weapons |
| Phantom | 800🪙 / 4★ | 8 | 9 | ✅ (0.6s) | Fast trail cutting |
| Titan | 2000🪙 / 10★ | 6 | 5 | ✅ (0.35s) | +1 life, 2x damage |
| Pulse | 4000🪙 / 18★ | 8 | 6 | ✅ (0.15s) | Rapid fire |
| Nova | 6000🪙 / 28★ | 10 | 8 | ✅ (0.25s) | Fast+strong, -1 life |

### Difficulty Scaling (Current)
- **Enemies:** 2→7 per level
- **Speed:** 3.5→6.5
- **Target %:** 70%→90%
- **Lives:** 3 (Galaxy 0-1), 4 (Galaxy 2), +1 bonus late in constellation

---

## 🐛 KNOWN BUGS (Open GitHub Issues)

| # | Issue | Priority |
|---|-------|----------|
| [#1](https://github.com/liteko702/zone-defence/issues/1) | Boss encounter gameplay not implemented | 🔴 High |
| [#2](https://github.com/liteko702/zone-defence/issues/2) | Shop UI not implemented (COMING SOON) | 🟡 Medium |
| [#5](https://github.com/liteko702/zone-defence/issues/5) | Ship skins not rendered in gameplay | 🟡 Cosmetic |
| [#6](https://github.com/liteko702/zone-defence/issues/6) | Trail effects not rendered from shop | 🟡 Cosmetic |
| [#7](https://github.com/liteko702/zone-defence/issues/7) | Missing audio: boss.mp3, victory.mp3, gameover.mp3 | 🟡 Audio |
| [#8](https://github.com/liteko702/zone-defence/issues/8) | PWA manifest for mobile install | 🟢 Nice-to-have |
| [#4](https://github.com/liteko702/zone-defence/issues/4) | ~~NEXT button overflow~~ | ✅ Fixed |

---

## 🚀 ROADMAP — What's Next

### Sprint 1: Restructure Levels (NEXT UP)
**Goal:** Reduce from 109 to ~63 levels. Make each level feel distinct.

- [ ] **Cap every constellation at 5 levels max** — trim star patterns or select 5 representative stars from each
- [ ] Steeper difficulty jumps between levels (each level should feel noticeably different)
- [ ] Rebalance enemy counts, speeds, and target % for fewer but punchier levels
- [ ] Update GAME_BREAKDOWN.md with new structure

### Sprint 2: Enemy Introductions
**Goal:** Players understand what each enemy does before fighting it.

- [ ] **"THREAT DETECTED" briefing screen** when a new enemy type first appears
- [ ] Show enemy name, sprite, behaviour description, and counter-strategy
- [ ] Only shows once per save (tracked in localStorage)
- [ ] Skippable with tap

### Sprint 3: Boss Overhaul ([#1](https://github.com/liteko702/zone-defence/issues/1))
**Goal:** Boss fights feel epic and memorable.

- [ ] **Unique boss music** — faster BPM, aggressive electronic, building intensity
- [ ] **Boss intro sequence** — name card, warning siren, camera zoom
- [ ] **Multi-phase fights** — behaviour changes at 50% and 25% HP
- [ ] Boss health bar UI
- [ ] Boss attack patterns (projectiles, area denial, spawning minions)
- [ ] Boss death animation (explosion cascade)
- [ ] Boss takes damage from bullets + territory capture

### Sprint 4: Map Avatar & Navigation
**Goal:** Map screen feels alive and personal.

- [ ] **Player ship avatar on map** — equipped ship appears on constellation nodes
- [ ] **Fly animation** between nodes when selecting levels
- [ ] Ship preview matches currently equipped ship
- [ ] More visual detail on constellation nodes (progress rings, glow effects)
- [ ] **Level preview panel** — shows enemies you'll face, target %, bonus timer info

### Sprint 5: Expand Content — New Galaxies
**Goal:** More galaxies with new mechanics, keeping 5 levels per constellation.

- [ ] **Galaxy 3:** New enemy types (minelayer? mirror? berserker?)
- [ ] **Galaxy 4+:** Environmental hazards (asteroid belts, gravity wells)
- [ ] Each galaxy introduces 1-2 new mechanics or enemy types
- [ ] New boss per galaxy with unique fight mechanics

### Sprint 6: Ship Upgrades & Visuals
**Goal:** Ships feel more distinct and upgradeable.

- [ ] **Improved ship sprites** — more detail, visual weapon differences
- [ ] **Ship upgrade tree** — spend coins to enhance individual ships
- [ ] Engine trail effects per ship type
- [ ] Possibly commissioned pixel art for ships
- [ ] Ship skins working in gameplay ([#5](https://github.com/liteko702/zone-defence/issues/5))

### Sprint 7: Shop & Economy ([#2](https://github.com/liteko702/zone-defence/issues/2))
- [ ] Shop screen in hangar SHOP tab
- [ ] 3 sections: Skins (8), Trails (6), Upgrades (5)
- [ ] Purchase flow with coin deduction
- [ ] Trail effects in gameplay ([#6](https://github.com/liteko702/zone-defence/issues/6))

### Sprint 8: Polish & QoL
- [ ] Interactive tutorial on first play
- [ ] Level intro cinematic (constellation draws itself)
- [ ] Win screen fireworks
- [ ] PWA manifest + offline play ([#8](https://github.com/liteko702/zone-defence/issues/8))
- [ ] Bonus timer system — time-based bonus scoring for extra challenge

### Sprint 9: Social & Replayability
- [ ] Achievements system
- [ ] Online leaderboard
- [ ] Share score card
- [ ] Endless/survival mode
- [ ] Daily challenge (procedural seed)

---

## 🎨 ART ASSETS NEEDED (Future)

| Asset | Purpose | Count |
|-------|---------|-------|
| Constellation icons | Detailed map node art | 12+ |
| Enemy portraits | Briefing/intro screens | 7 types + bosses |
| Ship artwork | Hangar detail & map avatar | 6 ships |
| Boss splash art | Boss intro sequence | 3+ bosses |
| Galaxy backgrounds | Unique per universe | 3+ |

---

## 🎵 AUDIO NEEDED ([#7](https://github.com/liteko702/zone-defence/issues/7))

| Track | Purpose | Notes |
|-------|---------|-------|
| `boss.mp3` | Boss level music | Fast electronic, building intensity |
| `victory.mp3` | Level complete sting | Short, triumphant |
| `gameover.mp3` | Game over sting | Short, dramatic |
| Per-boss themes | Unique per boss fight | Phase 2 — after boss overhaul |

---

## 📝 SESSION LOG

### 2026-02-24 — Bug Fixes & Hangar
- Fixed 3-digit hex + alpha append bug (ships crashing on non-Viper)
- Fixed d-pad disappearing on mobile (CSS class-based visibility)
- Rewrote `drawShipDetailed` as standalone renderer
- Added ship-specific trail colours + engine particles
- Reduced ship size in gameplay (1.8x → 1.2x)
- Increased early game pace (more enemies, faster base speed, 3x powerup spawns)
- Standardised hangar font sizes
- Created GitHub issues #1-#8

### 2026-02-27 — Analysis & Planning
- Created GAME_BREAKDOWN.md (full level/enemy/scoring analysis)
- Fixed hangar font scaling on wide screens
- Consolidated DESIGN.md as single source of truth
- Planned restructure: 5 levels per constellation, enemy intros, boss overhaul, map avatar
