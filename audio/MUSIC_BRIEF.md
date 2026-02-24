# Zone Defence — Music & SFX Generation Brief

Use this guide to generate tracks on **Suno** (suno.com) or similar AI music tools.
Drop the generated files into this `/audio` folder as `.mp3` files with the exact filenames listed below.

---

## 🎵 MUSIC TRACKS

All tracks should **loop cleanly** — ask Suno for "seamless loop" or "loopable" in the prompt.
Target length: **60-90 seconds** (they'll loop in-game).

### 1. `theme.mp3` — Main Title Theme
**Suno prompt idea:**
> Epic synth-wave space theme, heroic and exciting, retro arcade meets modern electronic, driving beat, bright synth leads, 130 BPM, cinematic, loopable, no vocals

**Where it plays:** Title screen, first impression of the game

---

### 2. `menu.mp3` — Star Chart / Menu
**Suno prompt idea:**
> Ambient space exploration music, gentle pads, soft arpeggios, mysterious and hopeful, floating in space, 80 BPM, atmospheric electronic, loopable, no vocals

**Where it plays:** Star chart (level select), hangar screen

---

### 3. `galaxy1.mp3` — Inner Rim Gameplay (Levels 1-4)
**Suno prompt idea:**
> Chill electronic game music, steady pulse, bright synth pads, light tension, space exploration vibes, 110 BPM, retro gaming, loopable, no vocals

**Where it plays:** Orion, Lyra, Cassiopeia, Cygnus levels

---

### 4. `galaxy2.mp3` — Deep Void Gameplay (Levels 5-8)
**Suno prompt idea:**
> Dark electronic game music, minor key, pulsing bass, tense arpeggios, cyberpunk space combat, 125 BPM, urgent but controlled, loopable, no vocals

**Where it plays:** Scorpius, Leo, Gemini, Draco levels (shooting unlocked!)

---

### 5. `galaxy3.mp3` — Outer Reach Gameplay (Levels 9-12)
**Suno prompt idea:**
> Intense electronic game music, aggressive synth, fast arpeggios, epic and dangerous, deep space battle, 140 BPM, high energy, loopable, no vocals

**Where it plays:** Perseus, Aquila, Sagittarius, Phoenix levels

---

### 6. `boss.mp3` — Boss Level (Phoenix)
**Suno prompt idea:**
> Epic boss battle music, intense electronic, dramatic builds, heavy bass drops, relentless energy, dark and powerful, 150 BPM, final confrontation, loopable, no vocals

**Where it plays:** Phoenix (level 12) — the final challenge

---

### 7. `victory.mp3` — Level Complete
**Suno prompt idea:**
> Short triumphant electronic fanfare, victorious synth chords, celebratory, bright and rewarding, 8-12 seconds, no loop needed, no vocals

**Where it plays:** After clearing a constellation (doesn't loop)

---

### 8. `gameover.mp3` — Game Over
**Suno prompt idea:**
> Short melancholic electronic sting, descending synths, disappointment but with hope, 6-10 seconds, no loop needed, no vocals

**Where it plays:** Game over screen (doesn't loop)

---

### 9. `pause.mp3` — Paused
**Suno prompt idea:**
> Ambient drone, low filtered pads, suspended in time, very quiet and atmospheric, 60 BPM, loopable, no vocals

**Where it plays:** Pause screen overlay

---

## 🔊 SOUND EFFECTS

These should be **short** (0.1-2 seconds). Generate on Suno with "sound effect" style, or use sfxr/jsfxr.

### Gameplay SFX
| File | Description | Suno/JSFXR prompt |
|------|-------------|-------------------|
| `sfx_claim.mp3` | Territory claimed | Short satisfying whoosh + sparkle, digital confirmation |
| `sfx_bigclaim.mp3` | Large territory claim (>20%) | Epic whoosh + rising chime cascade, rewarding |
| `sfx_death.mp3` | Player dies | Explosion + descending tone, digital destruction |
| `sfx_shoot.mp3` | Bullet fired | Quick laser zap, sci-fi blaster, very short |
| `sfx_hit.mp3` | Bullet hits enemy | Impact thud + digital crunch |
| `sfx_capture.mp3` | Enemy captured in zone | Satisfying containment sound, energy field closing |
| `sfx_powerup.mp3` | Power-up collected | Rising chime, magical pickup sound |
| `sfx_shield.mp3` | Shield activates | Energy shield hum, protective bubble |
| `sfx_phase.mp3` | Phase enemy teleports | Warp/teleport whoosh |
| `sfx_split.mp3` | Split enemy divides | Organic splitting/dividing sound |
| `sfx_respawn.mp3` | Enemy respawns | Warning alarm + materialise |

### UI SFX
| File | Description | Suno/JSFXR prompt |
|------|-------------|-------------------|
| `sfx_select.mp3` | Menu button select | Clean UI click/blip |
| `sfx_navigate.mp3` | Menu navigation | Soft UI tick |
| `sfx_start.mp3` | Level start / engage button | Dramatic whoosh, engines firing |
| `sfx_star.mp3` | Star earned | Bright chime, achievement sound |

---

## 📋 INTEGRATION CHECKLIST

Once you have the files, drop them in `/audio/` and the game will auto-detect and use them.
The game falls back to procedural synth if any file is missing.

Priority order for generation:
1. `theme.mp3` (first impression!)
2. `galaxy1.mp3` + `galaxy2.mp3` + `galaxy3.mp3` (core gameplay)
3. `menu.mp3` (star chart)
4. `boss.mp3` (epic finale)
5. `victory.mp3` + `gameover.mp3` (feedback)
6. SFX (gameplay feel)
7. `pause.mp3` (nice-to-have)

---

## 🎛️ TECHNICAL NOTES

- Format: **MP3** (best browser compatibility) or **OGG** (smaller)
- Keep files under **500KB** each for fast loading (compress/trim as needed)
- Music tracks: mono or stereo, 128-192kbps
- SFX: mono, 96-128kbps
- The game preloads all audio on first user interaction
