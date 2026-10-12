"""Build raster icons of the Quests mark (requires Pillow: pip install pillow).

usage: python3 scripts/build_icons.py
Outputs:
  site:  favicon.ico (16/32/48), apple-touch-icon.png (180), images/brand/icon-192.png, icon-512.png
  brand: _sources/brand/ (logo SVG copies, transparent 2048px PNGs, LinkedIn logo and cover image)

The mark is drawn from the same geometry as images/brand/logo.svg (100-unit grid, cropped to 10..90):
circle R=40 at the center, bottom-right quadrant squared off with a corner radius of 10, and a centered hole r=20.
If you change the SVG, change GEOMETRY below to match.
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


def main():
    sizes = (16, 32, 48)
    icons = [icon(s, NAVY) for s in sizes]
    icons[-1].save(os.path.join(ROOT, "favicon.ico"), sizes=[(s, s) for s in sizes], append_images=icons[:-1])
    # iOS / Android: white mark on navy, opaque, padded to sit inside the platform's rounded mask
    icon(180, WHITE, NAVY, .6).convert("RGB").save(os.path.join(ROOT, "apple-touch-icon.png"))
    for s in (192, 512):
        icon(s, WHITE, NAVY, .56).convert("RGB").save(os.path.join(ROOT, f"images/brand/icon-{s}.png"))
    brand = os.path.join(ROOT, "_sources/brand")
    os.makedirs(brand, exist_ok=True)
    for name in ("logo.svg", "logo-white.svg"):
        shutil.copyfile(os.path.join(ROOT, "images/brand", name), os.path.join(brand, name))
    icon(2048, NAVY).save(os.path.join(brand, "logo-navy-2048.png"))
    icon(2048, WHITE).save(os.path.join(brand, "logo-white-2048.png"))
    icon(400, WHITE, NAVY, .56).convert("RGB").save(os.path.join(brand, "linkedin-logo-400.png"))
    linkedin_cover().save(os.path.join(brand, "linkedin-cover-1128x191.png"))
    print("icons written")


def linkedin_cover(size=(1128, 191)):
    """LinkedIn cover from the hero background master: a horizontal band from the vertical center."""
    src = Image.open(os.path.join(ROOT, "_sources/photos/hero/background.jpg")).convert("RGB")
    band_h = round(src.width * size[1] / size[0])
    top = (src.height - band_h) // 2
    return src.crop((0, top, src.width, top + band_h)).resize(size, Image.LANCZOS)


if __name__ == "__main__":
    main()
