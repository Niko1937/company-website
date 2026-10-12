"""Build every raster file of the Quests mark (requires Pillow: pip install pillow).

usage: python3 scripts/build_icons.py

_sources/brand/ is the single home of all logo files. This script writes the PNG / ICO files there and then
copies the ones the website uses to their public locations:
  favicon.svg, icon-192.png, icon-512.png -> images/brand/
  favicon.ico, apple-touch-icon.png      -> site root (browsers request these paths directly)

The mark is drawn from the same geometry as _sources/brand/logo.svg (100-unit grid, cropped to 10..90):
circle R=40 at the center, bottom-right quadrant squared off with a corner radius of 10, and a centered hole r=20.
If you change the SVGs, change GEOMETRY below to match.
"""
import os
import shutil
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVY, WHITE = (0x23, 0x2F, 0x3E, 255), (255, 255, 255, 255)
GEOMETRY = {"R": 40, "corner": 10, "hole": 20}  # on the 100-unit grid, center (50, 50)
SS = 16  # supersampling factor for smooth edges


def mark_mask(px):
    """Antialiased mask of the mark filling a px x px square."""
    n = px * SS
    u = n / 80  # 80 grid units (10..90) span the canvas
    g = GEOMETRY
    m = Image.new("L", (n, n), 0)
    d = ImageDraw.Draw(m)
    c, r = 40 * u, g["R"] * u
    d.ellipse((c - r, c - r, c + r, c + r), fill=255)
    d.rounded_rectangle((c, c, n - 1, n - 1), radius=g["corner"] * u, fill=255)
    d.rectangle((c, c, n - 1 - g["corner"] * u, n - 1), fill=255)
    d.rectangle((c, c, n - 1, n - 1 - g["corner"] * u), fill=255)
    h = g["hole"] * u
    d.ellipse((c - h, c - h, c + h, c + h), fill=0)
    return m.resize((px, px), Image.LANCZOS)


def icon(size, color, bg=None, scale=1.0):
    canvas = Image.new("RGBA", (size, size), bg or (0, 0, 0, 0))
    px = round(size * scale)
    mark = Image.new("RGBA", (px, px), color)
    off = (size - px) // 2
    canvas.paste(mark, (off, off), mark_mask(px))
    return canvas


BRAND = os.path.join(ROOT, "_sources/brand")
# files the website uses: brand file name -> public path
WEB = {"favicon.svg": "images/brand/favicon.svg", "icon-192.png": "images/brand/icon-192.png",
       "icon-512.png": "images/brand/icon-512.png", "favicon.ico": "favicon.ico", "apple-touch-icon.png": "apple-touch-icon.png"}


def main():
    out = lambda name: os.path.join(BRAND, name)
    sizes = (16, 32, 48)
    icons = [icon(s, NAVY) for s in sizes]
    icons[-1].save(out("favicon.ico"), sizes=[(s, s) for s in sizes], append_images=icons[:-1])
    # iOS / Android: white mark on navy, opaque, padded to sit inside the platform's rounded mask
    icon(180, WHITE, NAVY, .6).convert("RGB").save(out("apple-touch-icon.png"))
    for s in (192, 512):
        icon(s, WHITE, NAVY, .56).convert("RGB").save(out(f"icon-{s}.png"))
    # documents and social media
    icon(2048, NAVY).save(out("logo-navy-2048.png"))
    icon(2048, WHITE).save(out("logo-white-2048.png"))
    icon(400, WHITE, NAVY, .56).convert("RGB").save(out("linkedin-logo-400.png"))
    linkedin_cover().save(out("linkedin-cover-1128x191.png"))
    # publish only what the website uses
    for name, dest in WEB.items():
        os.makedirs(os.path.dirname(os.path.join(ROOT, dest)), exist_ok=True)
        shutil.copyfile(out(name), os.path.join(ROOT, dest))
    print("brand files written to _sources/brand/; website copies updated")


def linkedin_cover(size=(1128, 191)):
    """LinkedIn cover from the hero background master: a horizontal band from the vertical center."""
    src = Image.open(os.path.join(ROOT, "_sources/photos/hero/background.jpg")).convert("RGB")
    band_h = round(src.width * size[1] / size[0])
    top = (src.height - band_h) // 2
    return src.crop((0, top, src.width, top + band_h)).resize(size, Image.LANCZOS)


if __name__ == "__main__":
    main()
