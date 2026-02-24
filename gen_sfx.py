#!/usr/bin/env python3
"""Generate retro/synth SFX for Zone Defence"""
import numpy as np
import wave, struct, os, subprocess

SR = 44100
OUT = 'audio/sfx_preview'
os.makedirs(OUT, exist_ok=True)

def save(name, samples):
    """Save float samples [-1,1] as WAV then convert to MP3"""
    samples = np.clip(samples, -1, 1)
    wav_path = f'{OUT}/{name}.wav'
    mp3_path = f'{OUT}/{name}.mp3'
    with wave.open(wav_path, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        data = (samples * 32767).astype(np.int16)
        w.writeframes(data.tobytes())
    subprocess.run(['ffmpeg', '-y', '-i', wav_path, '-b:a', '128k', '-af', 'afade=t=out:st=' + str(len(samples)/SR - 0.02) + ':d=0.02', mp3_path],
                   capture_output=True)
    os.remove(wav_path)
    print(f'  ✓ {name}')

def env(n, attack=0.01, decay=0.0, sustain=1.0, release=0.1):
    """ADSR envelope"""
    t = np.linspace(0, 1, n)
    total = len(t)
    a = int(attack * SR)
    r = int(release * SR)
    d = int(decay * SR)
    e = np.ones(n) * sustain
    # attack
    if a > 0: e[:min(a,n)] = np.linspace(0, 1, min(a,n))
    # decay
    if d > 0:
        ds = min(a, n)
        de = min(ds + d, n)
        e[ds:de] = np.linspace(1, sustain, de - ds)
    # release
    if r > 0: e[max(0,n-r):] = np.linspace(e[max(0,n-r-1)], 0, min(r, n))
    return e

def noise(n):
    return np.random.uniform(-1, 1, n)

def sine(freq, n):
    return np.sin(2 * np.pi * freq * np.arange(n) / SR)

def saw(freq, n):
    return 2 * (np.arange(n) * freq / SR % 1) - 1

def square(freq, n):
    return np.sign(np.sin(2 * np.pi * freq * np.arange(n) / SR))

def sweep(f0, f1, n):
    t = np.arange(n) / SR
    freqs = np.linspace(f0, f1, n)
    phase = 2 * np.pi * np.cumsum(freqs) / SR
    return np.sin(phase)

# ============ REQUIRED SFX (14) ============

print("=== Required SFX ===")

# 1. sfx_shoot — short laser pew
n = int(SR * 0.15)
s = sweep(1200, 200, n) * env(n, attack=0.005, release=0.05)
save('sfx_shoot', s * 0.7)

# 2. sfx_hit — enemy hit thud
n = int(SR * 0.2)
s = (sweep(400, 80, n) + noise(n) * 0.3) * env(n, attack=0.005, release=0.08)
save('sfx_hit', s * 0.6)

# 3. sfx_death — player death
n = int(SR * 0.5)
s = sweep(800, 60, n) * env(n, attack=0.01, release=0.15)
s += noise(n) * env(n, attack=0.1, release=0.2) * 0.2
save('sfx_death', s * 0.6)

# 4. sfx_claim — small territory claim
n = int(SR * 0.25)
s = sine(880, n) * env(n, attack=0.01, decay=0.05, sustain=0.4, release=0.1)
s += sine(1320, n) * env(n, attack=0.03, decay=0.05, sustain=0.3, release=0.1) * 0.5
save('sfx_claim', s * 0.5)

# 5. sfx_bigclaim — large territory claim (triumphant)
n = int(SR * 0.5)
# Rising arpeggio: C E G C
notes = [523, 659, 784, 1047]
s = np.zeros(n)
for i, freq in enumerate(notes):
    start = int(i * n / 5)
    dur = int(n * 0.4)
    end = min(start + dur, n)
    chunk = sine(freq, end - start) * env(end - start, attack=0.01, release=0.15)
    s[start:end] += chunk * 0.4
save('sfx_bigclaim', s * 0.7)

# 6. sfx_capture — enemy captured in zone
n = int(SR * 0.35)
s = sweep(300, 1500, n) * env(n, attack=0.01, release=0.1)
s += sine(1200, n) * env(n, attack=0.1, release=0.1) * 0.3
save('sfx_capture', s * 0.5)

# 7. sfx_powerup — power-up collect
n = int(SR * 0.3)
s = sweep(400, 1600, n) * env(n, attack=0.01, release=0.08)
s += sweep(600, 2000, n) * env(n, attack=0.02, release=0.08) * 0.4
save('sfx_powerup', s * 0.5)

# 8. sfx_shield — shield absorb hit
n = int(SR * 0.25)
s = sine(600, n) * env(n, attack=0.005, release=0.1)
s += noise(n) * env(n, attack=0.005, decay=0.05, sustain=0.1, release=0.1) * 0.4
save('sfx_shield', s * 0.6)

# 9. sfx_phase — enemy phase/teleport
n = int(SR * 0.3)
s = sweep(2000, 200, n) * env(n, attack=0.01, release=0.1) * 0.5
s += sweep(200, 2000, n) * env(n, attack=0.15, release=0.05) * 0.3
save('sfx_phase', s * 0.6)

# 10. sfx_split — enemy splits
n = int(SR * 0.25)
s = sweep(600, 1200, n//2)
s = np.concatenate([s, sweep(1200, 400, n - n//2)])
s *= env(n, attack=0.005, release=0.08)
s += noise(n) * env(n, attack=0.005, sustain=0.15, release=0.05) * 0.3
save('sfx_split', s * 0.6)

# 11. sfx_respawn — enemy respawn warning
n = int(SR * 0.4)
# Two-tone alert
half = n // 2
s1 = square(440, half) * env(half, attack=0.01, release=0.02) * 0.3
s2 = square(550, n - half) * env(n - half, attack=0.01, release=0.05) * 0.3
s = np.concatenate([s1, s2])
save('sfx_respawn', s)

# 12. sfx_select — menu select
n = int(SR * 0.12)
s = sine(800, n) * env(n, attack=0.005, release=0.04)
save('sfx_select', s * 0.5)

# 13. sfx_start — game/level start
n = int(SR * 0.4)
notes = [523, 659, 784]
s = np.zeros(n)
for i, freq in enumerate(notes):
    start = int(i * n / 4)
    dur = int(n * 0.35)
    end = min(start + dur, n)
    chunk = sine(freq, end - start) * env(end - start, attack=0.01, release=0.1)
    s[start:end] += chunk * 0.5
save('sfx_start', s * 0.6)

# 14. sfx_star — star earned
n = int(SR * 0.35)
s = sine(1047, n) * env(n, attack=0.01, decay=0.05, sustain=0.6, release=0.15)
s += sine(1568, n) * env(n, attack=0.05, sustain=0.3, release=0.15) * 0.4
save('sfx_star', s * 0.5)

# ============ BONUS SFX SUGGESTIONS ============

print("\n=== Bonus SFX Suggestions ===")

# 15. sfx_trail — continuous trail hum (short loop)
n = int(SR * 0.3)
s = saw(150, n) * 0.15 + sine(300, n) * 0.1
s *= env(n, attack=0.05, release=0.05)
save('sfx_trail', s)

# 16. sfx_countdown — 3-2-1 beep
n = int(SR * 0.12)
gap = np.zeros(int(SR * 0.08))
beep = sine(660, n) * env(n, attack=0.005, release=0.03) * 0.5
go = sine(990, int(SR * 0.2)) * env(int(SR * 0.2), attack=0.005, release=0.05) * 0.6
s = np.concatenate([beep, gap, beep, gap, beep, gap, go])
save('sfx_countdown', s)

# 17. sfx_warning — low pulsing alarm
n = int(SR * 0.6)
t = np.arange(n) / SR
pulse = (1 + np.sin(2 * np.pi * 4 * t)) / 2  # 4Hz pulse
s = square(220, n) * pulse * env(n, attack=0.02, release=0.05) * 0.3
save('sfx_warning', s)

# 18. sfx_combo — multi-kill/streak
n = int(SR * 0.35)
notes = [784, 988, 1175, 1568]
s = np.zeros(n)
for i, freq in enumerate(notes):
    start = int(i * n / 5)
    dur = int(n * 0.3)
    end = min(start + dur, n)
    chunk = sine(freq, end - start) * env(end - start, attack=0.005, release=0.08)
    s[start:end] += chunk * 0.4
save('sfx_combo', s * 0.7)

# 19. sfx_galaxy_unlock — galaxy transition fanfare
n = int(SR * 0.8)
# Rising chord: C major → octave
s = np.zeros(n)
for i, freq in enumerate([523, 659, 784, 1047, 1319]):
    start = int(i * n / 6)
    dur = int(n * 0.6)
    end = min(start + dur, n)
    chunk = (sine(freq, end-start) + sine(freq*2, end-start)*0.2) * env(end-start, attack=0.02, release=0.2)
    s[start:end] += chunk * 0.3
s += sweep(200, 2000, n) * env(n, attack=0.1, release=0.2) * 0.1
save('sfx_galaxy_unlock', s * 0.7)

# 20. sfx_border_return — safely returned to border
n = int(SR * 0.15)
s = sweep(600, 1000, n) * env(n, attack=0.005, release=0.04)
save('sfx_border_return', s * 0.5)

# 21. sfx_close_call — near miss with enemy
n = int(SR * 0.2)
s = sweep(1500, 300, n) * env(n, attack=0.005, release=0.05) * 0.4
s += noise(n) * env(n, attack=0.005, sustain=0.2, release=0.05) * 0.2
save('sfx_close_call', s)

# 22. sfx_pause — pause game
n = int(SR * 0.15)
s = sine(500, n//2)
s = np.concatenate([s, sine(400, n - n//2)])
s *= env(n, attack=0.005, release=0.04) * 0.4
save('sfx_pause', s)

# 23. sfx_unpause — resume game
n = int(SR * 0.15)
s = sine(400, n//2)
s = np.concatenate([s, sine(600, n - n//2)])
s *= env(n, attack=0.005, release=0.04) * 0.4
save('sfx_unpause', s)

# 24. sfx_ship_select — hangar ship selection
n = int(SR * 0.2)
s = sweep(500, 1200, n) * env(n, attack=0.01, release=0.06)
s += sine(1000, n) * env(n, attack=0.05, release=0.06) * 0.3
save('sfx_ship_select', s * 0.5)

print(f"\nDone! All files in {OUT}/")
