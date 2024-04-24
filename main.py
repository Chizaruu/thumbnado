from PIL import Image, ImageDraw
from config import *
from utils import draw_logos, load_logos
from utils import draw_title_text, draw_subtitle_text
from utils import save_image

# Create a new image with the Discord background color
img = Image.new('RGBA', (WIDTH, HEIGHT), BG_COLOR)

# Load the logo images
logos = load_logos(LOGO_FOLDER, LOGO_SIZE)

# Draw the logos in a repeating pattern
img = draw_logos(img, logos, DIRECTION, LOGO_SPACING, BG_COLOR)

# Create a black overlay
overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)

# Draw the overlay rectangle with the chosen opacity
overlay_draw.rectangle((0, 0, WIDTH, HEIGHT),
                       fill=(0, 0, 0, OVERLAY_OPACITY))

# Draw the title text on the overlay
overlay = draw_title_text(overlay, TITLE_TEXT, FONT_OPTION, MAX_TITLE_WIDTH,
                          MIN_LINES, ALIGNMENT, TEXT_OUTLINE_WIDTH, TEXT_OUTLINE_COLOR)

# Draw the subtitle text on the overlay
overlay = draw_subtitle_text(overlay, SUBTITLE_TEXT, MAX_TITLE_WIDTH, ALIGNMENT)

# Blend the overlay with the main image
img = Image.alpha_composite(img, overlay)

# Save the image with the title name
save_image(img, TITLE_TEXT)
