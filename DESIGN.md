# Zone Defence — Design Document

## Concept
Space-themed Qix-style territory capture game. Player pilots a spaceship along the border of a zone, ventures into unclaimed space to draw lines, and returns to claim territory. Enemies patrol the unclaimed area. Retro arcade feel with modern polish.

## Visual References
- **TRON arcade** — glowing neon lines, dark grid, light cycle territory claiming
- **Galaxy Attack / Space Shooter** — detailed ships, glowing engines, score popups, boss fights, power-ups
- **Bubble Bobble** — retro pixel art, arcade HUD (HI-SCORE), chunky feel
- **Candy Crush** — winding level select map with nodes, stars, progression

## Core Mechanic
1. Player moves along the border (safe zone)
2. Player ventures into unclaimed space, leaving an energy trail
3. Returning to the border claims the smaller region (no enemies inside)
4. Enemies touching the trail or player = shield damage
5. Claim X% of the zone to clear the sector

---

## PHASES

### Phase 1 — Core Game ✅ (DONE)
- [x] Grid-based Qix territory claiming mechanic
- [x] Player movement on border + cutting into empty space
- [x] Flood fill territory claiming (enemy-side exclusion)
- [x] Bouncing patrol enemies
- [x] Chaser enemies that follow player
- [x] 6 levels with increasing difficulty
- [x] Lives / shields system
- [x] Win condition (claim target %)

### Phase 2 — Space Theme & Polish ✅ (DONE)
- [x] Space-themed visuals (nebula, starfield, ships)
- [x] Detailed player ship (wings, cockpit, engine flames)
- [x] Detailed enemy ships (menacing, glowing cores)
- [x] Particle effects (explosions, engine trails, claim sparkles)
- [x] Floating score popups (GOOD! GREAT! AMAZING!)
- [x] Screen shake on damage
- [x] Chiptune SFX (Web Audio synthesis)
- [x] Retro pixel font (Press Start 2P)
- [x] CRT scanlines overlay

### Phase 3 — Progression & UI ✅ (DONE)
- [x] Level select map (winding space path, planet nodes)
- [x] Star ratings (1-3 per level)
- [x] HI-SCORE tracking (localStorage)
- [x] Level unlock progression
- [x] Pause menu (continue, retry, map, quit)
- [x] HUD (sector, score, hi-score, zone %, lives)

### Phase 4 — Power-ups ✅ (DONE)
- [x] Speed boost
- [x] Shield (survive one hit)
- [x] Extra life
- [x] Slow enemies
- [x] Power-ups spawn after claims & randomly
- [x] Visual: bobbing, glowing, sparkle particles

### Phase 5 — Onboarding & Tutorial 🔜 (NEXT)
- [ ] Interactive tutorial on first play (like Chase)
- [ ] Step-by-step: "Move along the border" → "Now venture in!" → "Return to claim!"
- [ ] Animated hand/arrow showing controls
- [ ] Practice area before level 1 (safe, no enemies)
- [ ] Tutorial for power-ups when first encountered
- [ ] Skip option for returning players
- [ ] "How to Play" accessible from pause menu
- [ ] Mobile-friendly tutorial (d-pad instructions)

### Phase 6 — Shootable Enemies & Combat
- [ ] Player can shoot while on the border (auto-fire or button)
- [ ] Small "grunt" enemies that fly in formations (Galaxy Attack style)
- [ ] Grunts drop bonus items when destroyed (score, power-ups)
- [ ] Different grunt types:
  - **Swarm bugs** — small, green, fly in V-formation
  - **Crab drones** — medium, orange, zigzag pattern
  - **Wasp fighters** — fast, dive-bomb toward player
  - **Mine layers** — drop hazards in unclaimed space
- [ ] Shooting doesn't work while cutting (vulnerability trade-off)
- [ ] Bonus waves between levels (pure shoot-em-up for extra score)

### Phase 7 — Boss Battles
- [ ] Boss enemy at end of each "world" (every 3 sectors)
- [ ] Boss occupies large area, has health bar
- [ ] Boss attacks: projectiles, area denial, spawning minions
- [ ] Claiming territory damages the boss (% claimed = boss damage)
- [ ] Boss phases (behavior changes at 50% and 25% health)
- [ ] Unique boss designs:
  - **Hive Mind** — organic blob, spawns bug swarms
  - **Dreadnought** — mechanical, laser sweeps
  - **Void Worm** — serpentine, leaves trail hazards

### Phase 8 — Enemy Variety & AI
- [ ] **Wall huggers** — enemies that follow the border edge
- [ ] **Splitters** — split into 2 smaller enemies when territory shrinks
- [ ] **Teleporters** — blink to random positions periodically
- [ ] **Shielded** — immune from front, must be flanked
- [ ] **Bombers** — periodically drop expanding hazard zones
- [ ] Enemy spawn animations (warp-in effect)
- [ ] Enemies react to territory being claimed (speed up, get angry)

### Phase 9 — Expanded Content
- [ ] 3 "worlds" of 6 sectors each (18 total levels)
  - **World 1: Outer Rim** — basic enemies, learn mechanics
  - **World 2: Nebula Core** — environmental hazards, tougher enemies
  - **World 3: Dark Sector** — all enemy types, boss gauntlet
- [ ] Each world has unique nebula colors and background art
- [ ] Unlockable player ships (different stats: speed vs. shield vs. firepower)
- [ ] Achievement system
- [ ] Daily challenge mode (random seed, leaderboard)

### Phase 10 — Audio & Music
- [ ] Suno-generated background music per world
- [ ] Music intensifies as claim % increases
- [ ] Victory fanfare
- [ ] Boss battle music
- [ ] Sound settings in pause menu
- [ ] Mute toggle

### Phase 11 — Social & Replayability
- [ ] Online leaderboard (simple backend)
- [ ] Share score card (screenshot/image generation)
- [ ] Endless mode (infinite waves, how long can you survive?)
- [ ] Speed run timer
- [ ] Ghost replay of best run

---

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
- Web Audio API for SFX
- localStorage for saves
- Static hosting (Caddy)
