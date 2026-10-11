"""Create the web-ready variants of a site photo (JPEG + WebP, one per width).

usage: python3 scripts/optimize_images.py <source-image> <dest-without-extension> [--widths 600,1200]

The largest width is written as <dest>.jpg / <dest>.webp; smaller widths get a -<width> suffix,
e.g. images/cases/voice.jpg, images/cases/voice-600.jpg, images/cases/voice.webp, images/cases/voice-600.webp.
Requires Pillow (pip install pillow). Widths larger than the source are skipped (no upscaling).
"""
import argparse
import os

from PIL import Image

JPEG_QUALITY = 80
WEBP_QUALITY = 78


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("dest")
    ap.add_argument("--widths", default="600,1200")
    args = ap.parse_args()

    src = Image.open(args.source).convert("RGB")
    widths = sorted({min(int(w), src.width) for w in args.widths.split(",")})
    os.makedirs(os.path.dirname(args.dest) or ".", exist_ok=True)
    for w in widths:
        img = src if w == src.width else src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
        base = args.dest if w == widths[-1] else f"{args.dest}-{w}"
        img.save(f"{base}.jpg", "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
        img.save(f"{base}.webp", "WEBP", quality=WEBP_QUALITY, method=6)
        print(f"{base}.jpg / .webp  {img.width}x{img.height}")


if __name__ == "__main__":
    main()
