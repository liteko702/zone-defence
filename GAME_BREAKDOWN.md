# Zone Defence — Game Breakdown

## Current Structure

### Galaxies (Universes)

| # | Galaxy | Constellations | Total Levels | Boss | Theme |
|---|--------|---------------|-------------|------|-------|
| 0 | **ANDROMEDA** | Cassiopeia (5), Lyra (6), Cygnus (6), Aquila (7) | **24 + 1 boss = 25** | Andromeda Guardian (8HP) | Learn basics, no weapons |
| 1 | **MILKY WAY** | Perseus (8), Phoenix (8), Leo (9), Gemini (10) | **35 + 1 boss = 36** | Milky Way Wyrm (12HP) | Weapons unlock, new enemies |
| 2 | **NEBULA PRIME** | Sagittarius (10), Scorpius (12), Draco (12), Orion (13) | **47 + 1 boss = 48** | Nebula Lord (18HP) | All enemy types, hardest |

**Grand total: 109 levels** (106 regular + 3 bosses)

### Level Count per Constellation

Each constellation has **1 level per star in the star pattern**. This is why some have 5 and others have 13 — it's based on the number of points in the constellation artwork.

| Constellation | Stars/Levels | Galaxy | Nickname |
|--------------|-------------|--------|----------|
| Cassiopeia | 5 | Andromeda | The Queen |
| Lyra | 6 | Andromeda | The Harp |
| Cygnus | 6 | Andromeda | The Swan |
| Aquila | 7 | Andromeda | The Eagle |
| Perseus | 8 | Milky Way | The Hero |
| Phoenix | 8 | Milky Way | The Firebird |
| Leo | 9 | Milky Way | The Lion |
| Gemini | 10 | Milky Way | The Twins |
| Sagittarius | 10 | Nebula Prime | The Archer |
| Scorpius | 12 | Nebula Prime | The Scorpion |
| Draco | 12 | Nebula Prime | The Dragon |
| Orion | 13 | Nebula Prime | The Hunter |

---

## Enemies

### Enemy Types

| Enemy | Appearance | Behaviour | First Appears | HP |
|-------|-----------|-----------|--------------|-----|
| **Bounce** (Patrol Drone) | Blue disc with scanning beam | Bounces off walls randomly. Basic threat. | Galaxy 0 — Level 1 | 1 |
| **Chase** (Hunter) | Red interceptor with swept wings | Actively chases the player. Aggressive. | Galaxy 0 — Level 1 | 1 |
| **Tracer** (Serpent Drone) | Green segmented worm | Follows player trails/paths | Galaxy 1 (Milky Way) | 1 |
| **Shield** (Armor Tank) | Gold armoured gunship | Slow but tough — takes 2 hits to kill | Galaxy 1 (Milky Way) | 2 |
| **Split** (Biomech Entity) | Pink blob with two nuclei, dashed division line | When killed, splits into 2 smaller bouncers | Galaxy 1 (Milky Way) | 1 (then spawns 2) |
| **Phase** (Crystal Ship) | Purple translucent diamond | Phases in and out — invulnerable while phased | Galaxy 2 (Nebula Prime) | 1 |
| **Orbit** (Ring Drone) | Orange ring with spinning energy arcs | Orbits in circular patterns | Galaxy 2 (Nebula Prime) | 1 |

### Enemy Introduction by Galaxy

- **Galaxy 0 (Andromeda):** Bounce + Chase only
- **Galaxy 1 (Milky Way):** + Tracer, Shield, Split
- **Galaxy 2 (Nebula Prime):** + Phase, Orbit (all 7 types)

### Enemy Count Scaling

- Starts at **2 enemies** per level
- Scales up to **max 7** based on global progress + position within constellation
- Formula: `min(7, max(2, floor(2 + globalProgress*4 + localProgress*2)))`

### Enemy Speed Scaling

- Base speed: **3.5** at start → ramps to ~**6.5** by end
- Formula: `3.5 + globalProgress*3 + localProgress*0.8`
- Later enemies in a level are slightly slower (`-0.3 per enemy index`)

---

## Difficulty Scaling

### Territory Target (% to clear)

| Progress | Target |
|----------|--------|
| Early levels | 70% |
| Mid game | ~78% |
| Late game | up to 90% |
| Formula | `min(90, max(70, round(70 + globalProgress*15 + localProgress*5)))` |

### Lives

| Galaxy | Base Lives | Late constellation bonus |
|--------|-----------|------------------------|
| Andromeda | 3 | +1 if >70% through constellation |
| Milky Way | 3 | +1 if >70% through constellation |
| Nebula Prime | 4 | +1 if >70% through constellation |

### Star Rating (per level)

| Stars | Requirement |
|-------|------------|
| ★ | Clear the target % |
| ★★ | Clear target + 5% |
| ★★★ | Clear target + 15% |

### Coins Per Level

- Formula: `round(50 + globalProgress*150 + localProgress*50) × star_count`
- Early levels: ~50 coins × stars
- Late levels: ~250 coins × stars

---

## Boss Levels

| Boss | Galaxy | HP | Speed | Escort Enemies | Lives | Target |
|------|--------|----|-------|----------------|-------|--------|
| Andromeda Guardian | 0 | 8 | 2.0 | 1 Bouncer (spd 3) | 3 | 75% |
| Milky Way Wyrm | 1 | 12 | 2.5 | 1 Bouncer (spd 4) + 1 Chaser (spd 3.5) | 4 | 80% |
| Nebula Lord | 2 | 18 | 3.0 | 1 Bouncer (spd 5) + 1 Chaser (spd 4.5) + 1 Phase (spd 3) + 1 Orbit (spd 2.5) | 5 | 85% |

Boss coins: 200 / 400 / 600

---

## Ships

| Ship | Cost | Stars Needed | Speed | Trail | Fire Rate | Damage | Special |
|------|------|-------------|-------|-------|-----------|--------|---------|
| Viper | FREE | 0 | 9 | 7 | — | — | No weapons, pure speed |
| Striker | 300🪙 | 0 | 7 | 6 | 0.35 | 1 | Standard weapons |
| Phantom | 800🪙 | 4★ | 8 | 9 | 0.6 | 1 | Fast trail cutting |
| Titan | 2000🪙 | 10★ | 6 | 5 | 0.35 | 2 | +1 life, double damage |
| Pulse | 4000🪙 | 18★ | 8 | 6 | 0.15 | 1 | Rapid fire cannon |
| Nova | 6000🪙 | 28★ | 10 | 8 | 0.25 | 2 | Fast+strong, -1 life |

---

## Issues & Proposals

### 🔴 Problem: Too Many Levels (109 total)

Many constellations have 8-13 levels that feel repetitive with no meaningful progression between them. The difficulty ramp within a single constellation is subtle.

### 🟡 Problem: No Enemy Introductions

New enemy types appear without explanation. Players don't know what a Phase or Split enemy does until they die to it.

### 🟡 Problem: Boss Levels Feel Flat

Same music as regular gameplay (or basic boss track). No unique mechanics, no phases, no intro sequence.

### 🟡 Problem: Map Navigation Feels Static

Clicking constellation nodes lacks personality. No avatar, no sense of journey.

---

## Proposed Changes

### 1. Reduce to 5 Levels per Constellation (MAX)

Trim every constellation to **max 5 stars**. This gives:
- Galaxy 0: 4 constellations × 5 = **20 + 1 boss = 21**
- Galaxy 1: 4 constellations × 5 = **20 + 1 boss = 21**
- Galaxy 2: 4 constellations × 5 = **20 + 1 boss = 21**
- **Total: 63 levels** (down from 109)

Each level needs to feel more distinct — bigger difficulty jumps, enemy introductions, etc.

### 2. Enemy Introduction Screens

When a new enemy type first appears, show a **briefing screen** before the level starts:
- Enemy name + artwork
- Behaviour description
- How to deal with it
- "THREAT DETECTED" style UI

### 3. Boss Overhaul

- **Unique procedural boss music** — faster BPM, more aggressive synths
- **Boss intro sequence** with name card + warning
- **Boss phases** (e.g., changes behaviour at 50% HP, 25% HP)
- Screen shake, flash effects on hit

### 4. Animated Map Avatar

- Player ship appears on the map and **flies between constellation nodes**
- Smooth animation when selecting levels
- Ship preview matches currently equipped ship

### 5. Add More Galaxies

With 5 levels per constellation, we have room to add:
- **Galaxy 3** and beyond with new enemy types
- Each galaxy introduces 1-2 new mechanics

### 6. Constellation Node Detail

- Larger node artwork with constellation imagery
- Completion percentage visible on each node
- Visual distinction between completed/current/locked
- Possibly commissioned pixel art for each constellation

### 7. Ship Visual Upgrades

- More detailed ship sprites
- Visual weapon differences
- Engine trail effects per ship
- Possible commissioned ship artwork

---

## Art Assets Needed (Future)

| Asset | Purpose | Count |
|-------|---------|-------|
| Constellation icons | Map node detail | 12 (one per constellation) |
| Enemy portraits | Intro/briefing screens | 7 enemy types + 3 bosses |
| Ship artwork | Hangar detail view | 6 ships |
| Boss splash art | Boss intro sequence | 3 bosses |
| Galaxy backgrounds | Unique per universe | 3+ |
