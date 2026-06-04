#!/usr/bin/env python3
"""Generate a fresh, harmonious, randomized color palette for a dashboard.

Run with no args for a random palette, or pass an integer seed for a
reproducible one:  python palette.py [seed]

Prints CSS-ready hex values: three accent pairs (deep + soft tint), a hero
gradient triple, plus the matching Chart.js COL values. Drop these into the
:root block, the header.hero gradient, and the JS COL object.
"""
import sys, random, colorsys


def hexc(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h % 1, l, s)
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))


def main():
    if len(sys.argv) > 1:
        random.seed(int(sys.argv[1]))
    base = random.random()
    # three hues spaced around the wheel so accents stay distinct
    h1 = base
    h2 = base + random.uniform(0.28, 0.40)
    h3 = base + random.uniform(0.55, 0.70)
    primary = hexc(h1, 0.62, 0.36)
    secondary = hexc(h2, 0.66, 0.42)
    tertiary = hexc(h3, 0.60, 0.32)
    p_soft = hexc(h1, 0.55, 0.92)
    s_soft = hexc(h2, 0.55, 0.92)
    t_soft = hexc(h3, 0.55, 0.92)
    g1, g2, g3 = hexc(h1, 0.45, 0.20), hexc(h1, 0.55, 0.34), hexc(h3, 0.50, 0.40)

    print("/* --- randomized palette (paste into :root) --- */")
    print(f"--proton:{primary}; --proton-soft:{p_soft};")
    print(f"--anti:{secondary}; --anti-soft:{s_soft};")
    print(f"--he:{tertiary}; --he-soft:{t_soft};")
    print(f"\n/* header.hero gradient */")
    print(f"background:linear-gradient(135deg,{g1} 0%,{g2} 55%,{g3} 130%);")
    print(f"\n/* JS Chart.js COL */")
    print(f"const COL = {{proton:'{primary}', anti:'{secondary}', "
          f"he:'{tertiary}', gold:'#b8860b', muted:'#5a6478'}};")


if __name__ == "__main__":
    main()
