# configuration.py

import argparse
from PIL import ImageFont

parser = argparse.ArgumentParser(description='Generate thumbnails with customizable options.')

parser.add_argument('--background-color', nargs=3, type=int, default=[54, 57, 63], help='Background color (RGB)')
parser.add_argument('--image-width', type=int, default=1280, help='Image width')
parser.add_argument('--image-height', type=int, default=720, help='Image height')
parser.add_argument('--logo-size', type=int, default=110, help='Logo size')
parser.add_argument('--logo-spacing', type=int, default=125, help='Logo spacing')
parser.add_argument('--logo-direction', type=str, default='horizontal', help='Logo direction (horizontal, vertical, diagonal-left, diagonal-right)')
parser.add_argument('--overlay-opacity', type=int, default=127, help='Overlay opacity (0-255)')
parser.add_argument('--title-text', type=str, default='A Really Cool Title!', help='Title text')
parser.add_argument('--subtitle-text', type=str, default='Subtitle Text Here', help='Subtitle text')
parser.add_argument('--title-font-size', type=int, default=140, help='Title font size')
parser.add_argument('--subtitle-font-size', type=int, default=100, help='Subtitle font size')
parser.add_argument('--font-style', type=str, default='bold', help='Font style (regular, bold)')
parser.add_argument('--title-font', type=str, default="fonts/Amaranth-Regular.otf", help='Path to the title font file')
parser.add_argument('--title-font-bold', type=str, default="fonts/Amaranth-Bold.otf", help='Path to the bold title font file')
parser.add_argument('--subtitle-font', type=str, default="fonts/Amaranth-Regular.otf", help='Path to the subtitle font file')
parser.add_argument('--min-title-lines', type=int, default=1, help='Minimum number of lines for the title text')
parser.add_argument('--text-outline-width', type=int, default=1, help='Text outline width')
parser.add_argument('--text-outline-color', nargs=4, type=int, default=[0, 0, 0, 255], help='Text outline color (RGBA)')
parser.add_argument('--text-alignment', type=str, default='center', help='Text alignment (left, right, center, justified)')
parser.add_argument('--logo-directory', type=str, default='Logos', help='Directory containing logo images')

args = parser.parse_args()

BG_COLOR = tuple(args.background_color)
IMAGE_WIDTH = args.image_width
IMAGE_HEIGHT = args.image_height
LOGO_SIZE = args.logo_size
LOGO_SPACING = args.logo_spacing
LOGO_DIRECTION = args.logo_direction
OVERLAY_OPACITY = args.overlay_opacity
TITLE_TEXT = args.title_text
SUBTITLE_TEXT = args.subtitle_text
MAX_TITLE_WIDTH = IMAGE_WIDTH
TITLE_FONT_SIZE = args.title_font_size
SUBTITLE_FONT_SIZE = args.subtitle_font_size
TITLE_FONT = ImageFont.truetype(args.title_font, TITLE_FONT_SIZE)
TITLE_FONT_BOLD = ImageFont.truetype(args.title_font_bold, TITLE_FONT_SIZE)
SUBTITLE_FONT = ImageFont.truetype(args.subtitle_font, SUBTITLE_FONT_SIZE)
MIN_TITLE_LINES = args.min_title_lines
FONT_STYLE = args.font_style
TEXT_OUTLINE_WIDTH = args.text_outline_width
TEXT_OUTLINE_COLOR = tuple(args.text_outline_color)
TEXT_ALIGNMENT = args.text_alignment
LOGO_DIRECTORY = args.logo_directory