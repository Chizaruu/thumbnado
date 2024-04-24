from PIL import ImageFont

# Define the background color
BG_COLOR = (54, 57, 63)

# Define the image size
WIDTH = 1280
HEIGHT = 720

# Define the logo size and spacing
LOGO_SIZE = 110
LOGO_SPACING = 125

# Define the logo direction
# Options: 'horizontal', 'vertical', 'diagonal_left', 'diagonal_right'
DIRECTION = 'horizontal'

# Choose the overlay opacity option (0-255)
# 0 means fully transparent, 255 means fully opaque
OVERLAY_OPACITY = 127

# Define the title text and font
TITLE_TEXT = "BUILD GAMES ON DISCORD"
# Define the subtitle text and font (Helps break the ice with humour)
SUBTITLE_TEXT = "Unity + Discord =<3"
# Maximum WIDTH of the title text (80% of the image WIDTH)
MAX_TITLE_WIDTH = WIDTH
TITLE_FONT_SIZE = 150
SUBTITLE_FONT_SIZE = 100
REGULAR_FONT = ImageFont.truetype(
    "System/Library/Fonts/impact.ttf", TITLE_FONT_SIZE)
BOLD_FONT = ImageFont.truetype(
    "System/Library/Fonts/GILLUBCD.TTF", TITLE_FONT_SIZE)  # Bold font
SUBTITLE_FONT = ImageFont.truetype(
    "System/Library/Fonts/impact.ttf", SUBTITLE_FONT_SIZE)

# Minimum number of lines for the title text
MIN_LINES = 1  # Set to 1 for no minimum

# Choose the font option
# Options: 'regular', 'bold'
FONT_OPTION = 'regular'

# Text outline settings
TEXT_OUTLINE_WIDTH = 1  # Adjust the outline WIDTH as desired
TEXT_OUTLINE_COLOR = (0, 0, 0, 255)  # Black outline color (RGBA)

# Choose the alignment option
# Options: 'left', 'right', 'center', 'justified'
ALIGNMENT = 'left'

# Specify the folder containing the logo images
LOGO_FOLDER = 'Logos'
