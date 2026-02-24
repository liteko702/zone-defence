#!/usr/bin/env python3
"""Generate futuristic/dynamic SFX for Zone Defence v2"""
import numpy as np
import wave, os, subprocess

SR = 44100
OUT = 'audio/sfx_preview'
os.makedirs(OUT, exist_ok=True)

def save(name, samples):
    samples = np.clip(samples, -1, 1)
    wav_path = f'{OUT}/{name}.wav'
    mp3_path = f'{OUT}/{name}.mp3'
    with wave.open(wav_path, 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((samples * 32767).astype(np.int16).tobytes())
    subprocess.run(['ffmpeg', '-y', '-i', wav_path, '-b:a', '128k', mp3_path], capture_output=True)
    os.remove(wav_path)
    print(f'  ✓ {name}')

def t(n): return np.arange(n) / SR
def sine(f, n): return np.sin(2*np.pi*f*t(n))
def saw(f, n): return 2*(t(n)*f % 1)-1
def square(f, n): return np.sign(np.sin(2*np.pi*f*t(n)))
def noise(n): return np.random.uniform(-1,1,n)

def sweep(f0, f1, n):
    freqs = np.linspace(f0, f1, n)
    return np.sin(2*np.pi*np.cumsum(freqs)/SR)

def exp_sweep(f0, f1, n):
    """Exponential frequency sweep — sounds more natural"""
    freqs = f0 * (f1/f0) ** (np.arange(n)/n)
    return np.sin(2*np.pi*np.cumsum(freqs)/SR)

def env(n, a=0.005, d=0, s=1.0, r=0.05):
    e = np.ones(n)*s
    ai = min(int(a*SR), n)
    di = min(int(d*SR), n)
    ri = min(int(r*SR), n)
    if ai>0: e[:ai] = np.linspace(0,1,ai)
    if di>0:
        ds,de = ai, min(ai+di,n)
        e[ds:de] = np.linspace(1,s,de-ds)
    if ri>0: e[max(0,n-ri):] *= np.linspace(1,0,min(ri,n))
    return e

def distort(s, amount=0.7):
    """Soft clipping distortion"""
    return np.tanh(s * (1 + amount * 3))

def bitcrush(s, bits=6):
    """Reduce bit depth for retro-digital feel"""
    levels = 2**bits
    return np.round(s * levels) / levels

def flanger(s, depth=0.003, rate=3):
    """Simple flanger effect"""
    n = len(s)
    tt = np.arange(n)/SR
    delay_samples = (depth * SR * (1 + np.sin(2*np.pi*rate*tt)) / 2).astype(int)
    out = s.copy()
    for i in range(n):
        d = delay_samples[i]
        if i - d >= 0:
            out[i] = s[i] + s[i-d] * 0.5
    return out * 0.67

def reverb(s, decay=0.3, delays=[1557, 2311, 3571]):
    """Simple comb filter reverb"""
    out = s.copy()
    for d in delays:
        padded = np.zeros(len(s))
        if d < len(s):
            padded[d:] = s[:-d] * decay
        out += padded
    return out / (1 + len(delays)*decay)

def ring_mod(s, freq=150):
    """Ring modulation — alien/robotic feel"""
    return s * sine(freq, len(s))

print("=== Futuristic SFX v2 ===")

# 1. sfx_shoot — punchy plasma bolt with ring mod
n = int(SR * 0.18)
s = exp_sweep(3000, 150, n) * 0.6
s += exp_sweep(1800, 80, n) * 0.3  # sub layer
s = ring_mod(s, 180)
s *= env(n, a=0.002, r=0.04)
s = distort(s, 0.4)
save('sfx_shoot', s * 0.7)

# 2. sfx_hit — metallic crunch impact
n = int(SR * 0.2)
s = noise(n) * env(n, a=0.001, d=0.02, s=0.3, r=0.06) * 0.5
s += exp_sweep(500, 60, n) * env(n, a=0.001, r=0.08) * 0.6
s += sine(120, n) * env(n, a=0.002, d=0.05, s=0.2, r=0.05) * 0.4  # sub thump
s = distort(s, 0.6)
save('sfx_hit', s * 0.65)

# 3. sfx_death — dramatic descending warble + explosion
n = int(SR * 0.6)
# Warbling descent
tt = t(n)
warble = np.sin(2*np.pi*12*tt) * 200  # vibrato
freqs = np.linspace(900, 50, n) + warble
phase = 2*np.pi*np.cumsum(freqs)/SR
s = np.sin(phase) * env(n, a=0.005, r=0.15) * 0.5
# Explosion burst
burst_n = int(SR * 0.25)
burst = noise(burst_n) * env(burst_n, a=0.001, d=0.03, s=0.3, r=0.1)
burst = distort(burst, 0.8) * 0.4
s[:burst_n] += burst
# Sub bass thump
s += sine(55, n) * env(n, a=0.01, d=0.1, s=0.15, r=0.1) * 0.35
s = reverb(s, 0.25)
save('sfx_death', s * 0.6)

# 4. sfx_claim — digital zone lock with glitch texture
n = int(SR * 0.2)
s = sweep(400, 1800, n) * env(n, a=0.002, r=0.06) * 0.4
s += square(900, n) * env(n, a=0.01, d=0.03, s=0.15, r=0.04) * 0.2
# Digital glitch burst
glitch = bitcrush(noise(n), 4) * env(n, a=0.001, d=0.02, s=0.05, r=0.03) * 0.15
s += glitch
s = distort(s, 0.3)
save('sfx_claim', s * 0.6)

# 5. sfx_bigclaim — massive zone capture: layered synth rise + impact
n = int(SR * 0.55)
# Rising synth sweep
s = exp_sweep(200, 3000, n) * env(n, a=0.01, r=0.1) * 0.3
# Parallel detuned sweep
s += exp_sweep(205, 3050, n) * env(n, a=0.01, r=0.1) * 0.25
# Digital shimmer
shimmer = bitcrush(sweep(1000, 4000, n), 6) * env(n, a=0.1, r=0.15) * 0.15
s += shimmer
# Impact at ~60%
impact_start = int(n * 0.6)
impact_n = n - impact_start
impact = noise(impact_n) * env(impact_n, a=0.001, d=0.02, s=0.2, r=0.08) * 0.3
impact += sine(80, impact_n) * env(impact_n, a=0.002, r=0.1) * 0.3
s[impact_start:] += impact
s = reverb(s, 0.3)
save('sfx_bigclaim', s * 0.65)

# 6. sfx_capture — enemy trapped: compression + zap
n = int(SR * 0.35)
# Closing-in sweep from both ends
s = exp_sweep(2500, 400, n) * 0.3
s += exp_sweep(100, 800, n) * 0.25
s *= env(n, a=0.005, r=0.08)
# Electric zap texture
zap_n = int(SR * 0.1)
zap = ring_mod(noise(zap_n), 300) * env(zap_n, a=0.001, r=0.03) * 0.3
s[:zap_n] += zap
s = distort(s, 0.5)
save('sfx_capture', s * 0.6)

# 7. sfx_powerup — energy absorption whoosh
n = int(SR * 0.35)
s = exp_sweep(150, 3500, n) * env(n, a=0.01, r=0.08) * 0.35
s += exp_sweep(200, 4000, n) * env(n, a=0.02, r=0.08) * 0.2  # detuned layer
# Sparkle overlay
sparkle_n = int(SR * 0.15)
sparkle = ring_mod(sweep(2000, 5000, sparkle_n), 400) * env(sparkle_n, a=0.01, r=0.05) * 0.2
s[n-sparkle_n:] += sparkle
s = flanger(s, depth=0.002, rate=6)
save('sfx_powerup', s * 0.6)

# 8. sfx_shield — force field deflection
n = int(SR * 0.25)
# Metallic resonance
s = ring_mod(sine(800, n), 250) * env(n, a=0.002, d=0.03, s=0.4, r=0.08) * 0.4
# Electric crackle
crackle = bitcrush(noise(n), 3) * env(n, a=0.001, d=0.02, s=0.1, r=0.05) * 0.2
s += crackle
# Sub resonance
s += sine(200, n) * env(n, a=0.005, r=0.1) * 0.25
s = reverb(s, 0.2, [800, 1200])
save('sfx_shield', s * 0.65)

# 9. sfx_phase — dimensional rift / teleport
n = int(SR * 0.35)
# Phase sweep down then up
half = n // 2
down = exp_sweep(4000, 100, half) * env(half, a=0.005, r=0.02)
up = exp_sweep(100, 3500, n-half) * env(n-half, a=0.005, r=0.08)
s = np.concatenate([down, up]) * 0.3
# Flanged noise burst
burst = flanger(noise(n), depth=0.004, rate=8) * env(n, a=0.01, d=0.05, s=0.15, r=0.1) * 0.2
s += burst
# Ring mod alien texture
s = s * 0.7 + ring_mod(s, 120) * 0.3
save('sfx_phase', s * 0.6)

# 10. sfx_split — cell division: twin diverging tones
n = int(SR * 0.3)
tt = t(n)
# Two tones splitting apart
f_center = 600
spread = np.linspace(0, 500, n)
s1 = np.sin(2*np.pi*(f_center + spread)*tt) * 0.3
s2 = np.sin(2*np.pi*(f_center - spread)*tt) * 0.3
s = (s1 + s2) * env(n, a=0.002, r=0.06)
# Glitch burst at start
glitch_n = int(SR * 0.04)
glitch = bitcrush(noise(glitch_n), 3) * env(glitch_n, a=0.001, r=0.01) * 0.4
s[:glitch_n] += glitch
s = distort(s, 0.3)
save('sfx_split', s * 0.6)

# 11. sfx_respawn — ominous digital alert
n = int(SR * 0.45)
# Pulsing square wave with pitch bend
pulses = 3
pulse_n = n // pulses
s = np.zeros(n)
for i in range(pulses):
    start = i * pulse_n
    end = start + pulse_n
    freq = 300 + i * 80
    chunk = square(freq, pulse_n) * 0.2
    chunk += saw(freq * 1.5, pulse_n) * 0.1
    chunk *= env(pulse_n, a=0.005, d=0.02, s=0.6, r=0.03)
    s[start:end] = chunk
s = ring_mod(s, 60)  # dark undertone
s = distort(s, 0.3)
save('sfx_respawn', s * 0.55)

# 12. sfx_select — quick digital confirm blip
n = int(SR * 0.1)
s = exp_sweep(600, 1400, n) * env(n, a=0.002, r=0.03) * 0.4
s += square(1000, n) * env(n, a=0.003, d=0.01, s=0.15, r=0.02) * 0.15
s = bitcrush(s, 8)  # slight digital texture
save('sfx_select', s * 0.6)

# 13. sfx_start — engine ignition sequence
n = int(SR * 0.5)
# Low rumble building up
rumble = saw(60, n) * env(n, a=0.1, d=0, s=0.3, r=0.05) * 0.2
rumble += noise(n) * env(n, a=0.15, d=0.05, s=0.1, r=0.05) * 0.15
# Rising synth
rise = exp_sweep(200, 2000, n) * env(n, a=0.05, r=0.1) * 0.3
rise += exp_sweep(210, 2100, n) * env(n, a=0.06, r=0.1) * 0.2
s = rumble + rise
# Final burst
burst_start = int(n * 0.75)
burst_n = n - burst_start
burst = (sweep(1500, 3000, burst_n) + noise(burst_n)*0.2) * env(burst_n, a=0.005, r=0.08) * 0.25
s[burst_start:] += burst
s = distort(s, 0.3)
save('sfx_start', s * 0.6)

# 14. sfx_star — data crystal collect: shimmering digital
n = int(SR * 0.35)
# Fast arpeggio with digital texture
notes_hz = [1200, 1600, 2000, 2400]
s = np.zeros(n)
for i, f in enumerate(notes_hz):
    start = int(i * n / 6)
    dur = int(n * 0.35)
    end = min(start + dur, n)
    chunk = sine(f, end-start) * 0.25
    chunk += sine(f*2.01, end-start) * 0.1  # detuned harmonic
    chunk *= env(end-start, a=0.003, r=0.1)
    s[start:end] += chunk
s = flanger(s, depth=0.002, rate=5)
s = bitcrush(s * 0.8 + s, 10)  # subtle digital
save('sfx_star', s * 0.55)

# ============ BONUS ============
print("\n=== Bonus SFX v2 ===")

# sfx_trail — electric hum with movement feel
n = int(SR * 0.3)
s = saw(120, n) * 0.15
s += sine(240, n) * 0.1
s = ring_mod(s, 80)
s *= env(n, a=0.03, r=0.03)
s = flanger(s, depth=0.003, rate=4)
save('sfx_trail', s * 0.5)

# sfx_countdown — digital countdown pulses
n_beep = int(SR * 0.1)
gap = np.zeros(int(SR * 0.1))
beep = square(500, n_beep) * 0.15 + sine(500, n_beep) * 0.2
beep *= env(n_beep, a=0.002, r=0.02)
beep = bitcrush(beep, 8)
go_n = int(SR * 0.25)
go = exp_sweep(500, 1500, go_n) * env(go_n, a=0.005, r=0.06) * 0.4
go += sine(1000, go_n) * env(go_n, a=0.02, r=0.06) * 0.2
go = distort(go, 0.3)
s = np.concatenate([beep, gap, beep, gap, beep, gap, go])
save('sfx_countdown', s)

# sfx_warning — deep pulsing threat alarm
n = int(SR * 0.6)
tt = t(n)
pulse = (1 + np.sin(2*np.pi*3*tt)) / 2
s = saw(140, n) * pulse * 0.2
s += sine(70, n) * pulse * 0.15
s *= env(n, a=0.02, r=0.05)
s = distort(s, 0.5)
s = ring_mod(s, 30)
save('sfx_warning', s * 0.6)

# sfx_combo — escalating power surge
n = int(SR * 0.4)
freqs = [600, 900, 1350, 2000, 3000]
s = np.zeros(n)
for i, f in enumerate(freqs):
    start = int(i * n / 6)
    dur = int(n * 0.3)
    end = min(start + dur, n)
    chunk = sine(f, end-start) * 0.2
    chunk += saw(f, end-start) * 0.08
    chunk *= env(end-start, a=0.003, r=0.06)
    s[start:end] += chunk
s = flanger(s, depth=0.003, rate=4)
s = distort(s, 0.3)
save('sfx_combo', s * 0.6)

# sfx_galaxy_unlock — epic warp gate opening
n = int(SR * 1.0)
# Deep sub rumble
s = sine(40, n) * env(n, a=0.1, d=0.1, s=0.3, r=0.2) * 0.3
# Rising synth layers
s += exp_sweep(100, 2000, n) * env(n, a=0.05, r=0.15) * 0.25
s += exp_sweep(105, 2050, n) * env(n, a=0.06, r=0.15) * 0.2
# Warp burst at 70%
burst_start = int(n * 0.7)
burst_n = n - burst_start
burst = noise(burst_n) * env(burst_n, a=0.005, d=0.03, s=0.2, r=0.1) * 0.2
burst += exp_sweep(2000, 5000, burst_n) * env(burst_n, a=0.01, r=0.1) * 0.2
s[burst_start:] += burst
s = reverb(s, 0.35)
save('sfx_galaxy_unlock', s * 0.6)

# sfx_border_return — quick safe-zone confirmation
n = int(SR * 0.12)
s = exp_sweep(800, 1800, n) * env(n, a=0.002, r=0.03) * 0.35
s += sine(1400, n) * env(n, a=0.01, r=0.03) * 0.15
s = bitcrush(s, 10)
save('sfx_border_return', s * 0.6)

# sfx_close_call — proximity warning buzz
n = int(SR * 0.2)
s = ring_mod(exp_sweep(2000, 200, n), 200) * env(n, a=0.002, r=0.04) * 0.35
s += noise(n) * env(n, a=0.002, d=0.02, s=0.1, r=0.03) * 0.2
s = distort(s, 0.5)
save('sfx_close_call', s * 0.55)

# sfx_ship_select — hangar confirmation with weight
n = int(SR * 0.25)
s = exp_sweep(300, 1200, n) * env(n, a=0.005, r=0.08) * 0.3
s += sine(800, n) * env(n, a=0.03, d=0.02, s=0.3, r=0.06) * 0.2
s += saw(600, n) * env(n, a=0.01, d=0.03, s=0.1, r=0.06) * 0.1
s = flanger(s, depth=0.002, rate=3)
save('sfx_ship_select', s * 0.6)

print("\nDone! Pause/unpause kept from v1.")
