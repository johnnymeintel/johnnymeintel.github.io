from PIL import Image, ImageDraw, ImageFont

W, H = 1584, 396

# ── Palette ────────────────────────────────────────────────────────────────
BG   = (255, 255, 255)   # white
INK  = (22,  22,  22)
DIM  = (111, 111, 111)
BLUE = (0,   67,  206)
RULE   = (198, 198, 198)
PURPLE = (105,  41, 196)   # #6929c4

# ── Fonts ──────────────────────────────────────────────────────────────────
FONTS    = "C:/Windows/Fonts/"
f_name   = ImageFont.truetype(FONTS + "consolab.ttf", 86)
f_degree = ImageFont.truetype(FONTS + "consola.ttf",  36)

# ── Canvas ─────────────────────────────────────────────────────────────────
img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

R_PAD = 80          # padding from right edge
R_X   = W - R_PAD  # right anchor for text

# Right IBM-blue accent bar
draw.rectangle([W - 8, 0, W, H], fill=PURPLE)

# ── Measure text ───────────────────────────────────────────────────────────
name_str = "Johnny Meintel"
deg1_str = "M.S. Cybersecurity & Information Assurance"
deg2_str = "B.S. Cloud Computing"

name_w = draw.textlength(name_str, font=f_name)
name_bb = draw.textbbox((0, 0), name_str, font=f_name)
deg_bb  = draw.textbbox((0, 0), deg1_str, font=f_degree)

name_h = name_bb[3] - name_bb[1]
deg_h  = deg_bb[3]  - deg_bb[1]
GAP    = 18
DGAP   = 14

block_h = name_h + GAP + 1 + GAP + deg_h + DGAP + deg_h
top_y   = (H - block_h) // 2

# ── Name (right-aligned) ───────────────────────────────────────────────────
name_x = R_X - name_w
draw.text((name_x, top_y), name_str, font=f_name, fill=INK)
name_end = top_y + name_h + GAP

# Rule flush right, same width as name
draw.rectangle([name_x, name_end, R_X, name_end + 2], fill=PURPLE)

# ── Degrees (right-aligned) ────────────────────────────────────────────────
deg_y = name_end + GAP
deg1_w = draw.textlength(deg1_str, font=f_degree)
draw.text((R_X - deg1_w, deg_y), deg1_str, font=f_degree, fill=DIM)

deg_y += deg_h + DGAP
deg2_w = draw.textlength(deg2_str, font=f_degree)
draw.text((R_X - deg2_w, deg_y), deg2_str, font=f_degree, fill=DIM)

# ── Save ───────────────────────────────────────────────────────────────────
out = "C:/portfolio/linkedin_banner.jpg"
img.save(out, "JPEG", quality=95)
print(f"Saved: {out}")
