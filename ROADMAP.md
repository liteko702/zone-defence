# Zone Defence — Development Roadmap

**Last updated:** 2026-02-24
**Live:** https://zone-defence.kbot.uk
**GitHub:** https://github.com/liteko702/zone-defence
**Lines:** ~3200 (single file: index.html)

---

## ✅ COMPLETED

### Phase 1: Zoomable Star Chart ✓
- [x] Two-level zoom: galaxy view → constellation view
- [x] Galaxy ◄ ► navigation + swipe between galaxies
- [x] Galaxy dot indicators, boss ⚠ markers
- [x] Constellation view with enemy info panel (types, target %, lives)
- [x] Smooth animated zoom transitions (~0.25s)
- [x] Instant touch response (touchend handlers)
- [x] Tap-to-select, tap-again-to-play (prevents accidental starts)

### Phase 2: Multi-Level Constellations ✓
- [x] ~75 regular levels + 3 boss levels generated programmatically
- [x] 9 real constellations across 3 universes (Andromeda/Milky Way/Nebula Prime)
- [x] Progressive difficulty curve per constellation
- [x] Save bumped to `zd6` with coins, purchases, levelScores
- [x] Coin economy (earned per level × star rating)

### Phase 4: Enemy Sprites ✓
- [x] Unique sprite per enemy type (patrol/hunter/phase/tracer/armor/orbit/split/boss)
- [x] Size variation per type (boss=3x scale)
- [x] Glow outlines, HP bars on multi-HP enemies
- [x] Enhanced bullet trails with streaks

### Audio System ✓
- [x] External MP3 music (menu, theme, galaxy1-3) + synth fallback
- [x] Music crossfading between scenes (~400ms)
- [x] 24 synthesized SFX (futuristic v2)
- [x] Per-SFX volume control
- [x] Music/SFX toggles + volume sliders in settings

### Core Game ✓
- [x] Qix gameplay (border movement, trail cutting, flood-fill)
- [x] 7 enemy types with unique behaviors
- [x] 5 unlockable ships (Viper/Phantom/Titan/Pulse/Nova)
- [x] Auto-shooting (Galaxy 2+ only, per ship `canShoot`)
- [x] Capture kills (+500), power-ups (Speed/Shield/Life/Slow)
- [x] Efficiency ranking (S/A/B/C), smooth interpolation
- [x] Fullscreen landscape lock, auto-pause, moveable d-pad
- [x] Settings cog (⚙) with all options
- [x] Sandbox mode (test all enemies/ships/power-ups)
- [x] Canvas-rendered hangar with ship stats + purchase flow
- [x] Animated background (shooting stars + debris)

---

## 🎯 CURRENT SPRINT: Boss Encounters + Shop

### Phase 3: Boss Encounters — [Issue #1](https://github.com/liteko702/zone-defence/issues/1)
- [ ] Boss health bar UI
- [ ] Boss attack patterns (dodge → rockets → phase-shift+split)
- [ ] Boss takes damage from player bullets
- [ ] Victory = defeat boss (not just claim %)
- [ ] Boss death animation
- [ ] Boss music (needs `boss.mp3`)

### Shop System — [Issue #2](https://github.com/liteko702/zone-defence/issues/2)
- [ ] Shop screen in hangar SHOP tab (replace COMING SOON)
- [ ] 3 sections: Skins (8), Trails (6), Upgrades (5)
- [ ] Purchase flow with coin deduction
- [ ] Active skin/trail rendering in gameplay — [#5](https://github.com/liteko702/zone-defence/issues/5), [#6](https://github.com/liteko702/zone-defence/issues/6)

---

## 🐛 KNOWN BUGS

- [ ] **NEXT button overflow** — clicking NEXT after last level crashes ([#4](https://github.com/liteko702/zone-defence/issues/4))
- [ ] Ship skins not visually applied in gameplay ([#5](https://github.com/liteko702/zone-defence/issues/5))
- [ ] Trail effects not rendered from shop purchases ([#6](https://github.com/liteko702/zone-defence/issues/6))

---

## 📋 UPCOMING

### Phase 5: Polish & Content
- [ ] Ship skins rendering in gameplay
- [ ] Trail effects rendering (including rainbow)
- [ ] Level intro cinematic (constellation draws itself)
- [ ] Win screen fireworks/celebration
- [ ] Animated score counter
- [ ] PWA manifest + service worker ([#8](https://github.com/liteko702/zone-defence/issues/8))

### Phase 6: Advanced Enemies
- [ ] Snake/formation enemies (fly in patterns)
- [ ] Minelayer, Mirror, Berserker, Healer types
- [ ] Enemy death animations

### Phase 7: Meta-Game
- [ ] Achievements system
- [ ] Per-level high scores / leaderboard
- [ ] Daily challenge (procedural seed)
- [ ] Ship upgrade trees

---

## 🎵 AUDIO STILL NEEDED — [Issue #7](https://github.com/liteko702/zone-defence/issues/7)
- [ ] `boss.mp3` — boss level music
- [ ] `victory.mp3` — level complete sting
- [ ] `gameover.mp3` — game over sting
- [ ] `pause.mp3` — pause ambient (optional)

Suno reminder: Feb 25 10am UTC

---

## 📊 STATS
- **Levels:** ~78 (75 regular + 3 bosses)
- **Ships:** 5 (+ shop skins defined)
- **Enemy types:** 7 regular + boss
- **Power-ups:** 4
- **Save key:** `zd6`
- **Universes:** Andromeda (17+boss) → Milky Way (23+boss) → Nebula Prime (32+boss)
