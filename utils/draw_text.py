# draw_text.py

from PIL import ImageDraw
from configuration import *

def draw_title_text(overlay, TITLE_TEXT, FONT_STYLE, MAX_TITLE_WIDTH, min_lines, alignment, text_outline_width, text_outline_color):
    overlay_draw = ImageDraw.Draw(overlay)
    font = TITLE_FONT if FONT_STYLE == 'regular' else TITLE_FONT_BOLD

    title_lines = wrap_title_text(overlay_draw, TITLE_TEXT, MAX_TITLE_WIDTH, min_lines, font)
    title_y = calculate_title_position(overlay_draw, title_lines, FONT_STYLE)

    for line in title_lines:
        draw_outlined_text(overlay_draw, line, title_y, FONT_STYLE, alignment, text_outline_width, text_outline_color)
        title_y += get_line_height(overlay_draw, line, FONT_STYLE) + 10  # Adjust the spacing between lines

    return overlay

def draw_subtitle_text(overlay, SUBTITLE_TEXT, MAX_TITLE_WIDTH, alignment):
    overlay_draw = ImageDraw.Draw(overlay)

    subtitle_lines = wrap_subtitle_text(overlay_draw, SUBTITLE_TEXT, MAX_TITLE_WIDTH)
    subtitle_y = calculate_subtitle_position(overlay_draw, subtitle_lines)

    for line in subtitle_lines:
        draw_text(overlay_draw, line, subtitle_y, SUBTITLE_FONT, alignment)
        subtitle_y += get_line_height(overlay_draw, line, SUBTITLE_FONT) + 5  # Adjust the spacing between lines

    return overlay


def wrap_title_text(draw, text, max_width, min_lines=1, font=TITLE_FONT):
    lines = []
    current_line = ""
    words = text.split()

    for word in words:
        if word == words[-1] and len(lines) + 1 < min_lines:
            continue
        if draw.textbbox((0, 0), current_line + " " + word, font)[2] <= max_width:
            current_line += " " + word
        else:
            lines.append(current_line.strip())
            current_line = word

    if current_line:
        lines.append(current_line.strip())

    while len(lines) < min_lines:
        if not words:
            lines.append("")
        else:
            next_word = words.pop(-1)
            lines.append(next_word)

    return lines

def wrap_subtitle_text(draw, text, max_width, font=SUBTITLE_FONT):
    lines = []
    current_line = ""
    words = text.split()

    for word in words:
        if draw.textbbox((0, 0), current_line + " " + word, font)[2] <= max_width:
            current_line += " " + word
        else:
            lines.append(current_line.strip())
            current_line = word

    if current_line:
        lines.append(current_line.strip())

    return lines

def calculate_title_position(draw, title_lines, FONT_STYLE):
    title_height = sum(get_line_height(draw, line, FONT_STYLE) for line in title_lines)
    title_spacing = 10  # Spacing between title lines
    total_title_height = title_height + (len(title_lines) - 1) * title_spacing
    subtitle_height = get_line_height(draw, SUBTITLE_TEXT, SUBTITLE_FONT)
    total_text_height = total_title_height + subtitle_height + 30  # Spacing between title and subtitle
    title_y = (IMAGE_HEIGHT - total_text_height) // 2
    return title_y

def calculate_subtitle_position(draw, subtitle_lines):
    title_height = sum(get_line_height(draw, line, FONT_STYLE) for line in TITLE_TEXT.split())
    title_spacing = 10  # Spacing between title lines
    total_title_height = title_height + (len(TITLE_TEXT.split()) - 1) * title_spacing
    subtitle_height = sum(get_line_height(draw, line, SUBTITLE_FONT) for line in subtitle_lines)
    subtitle_spacing = 5  # Spacing between subtitle lines
    total_subtitle_height = subtitle_height + (len(subtitle_lines) - 1) * subtitle_spacing
    total_text_height = total_title_height + total_subtitle_height + 30  # Spacing between title and subtitle
    subtitle_y = (IMAGE_HEIGHT - total_text_height) // 2 + total_title_height + 30
    return subtitle_y

def draw_outlined_text(draw, text, y, FONT_STYLE, alignment, outline_width, outline_color):
    font = TITLE_FONT if FONT_STYLE == 'regular' else TITLE_FONT_BOLD 
    line_bbox = draw.textbbox((0, 0), text, font)
    line_width = line_bbox[2] - line_bbox[0]

    if alignment == 'left':
        x = 20  # Adjust this value to change the left margin
    elif alignment == 'right':
        x = IMAGE_WIDTH - MAX_TITLE_WIDTH - 20  # Adjust the value 20 to change the right margin
    elif alignment == 'center':
        x = (IMAGE_WIDTH - line_width) // 2
    else:
        raise ValueError(f"Invalid alignment option: {alignment}")

    for offset_x in range(-outline_width, outline_width + 1):
        for offset_y in range(-outline_width, outline_width + 1):
            if offset_x == 0 and offset_y == 0:
                continue
            draw.text((x + offset_x, y + offset_y), text, font=font, fill=outline_color)
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

def draw_text(draw, text, y, font, alignment):
    line_bbox = draw.textbbox((0, 0), text, font)
    line_width = line_bbox[2] - line_bbox[0]

    if alignment == 'left':
        x = 20  # Adjust this value to change the left margin
    elif alignment == 'right':
        x = IMAGE_WIDTH - line_width - 20  # Adjust the value 20 to change the right margin
    elif alignment == 'center':
        x = (IMAGE_WIDTH - line_width) // 2
    else:
        raise ValueError(f"Invalid alignment option: {alignment}")

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

def get_line_height(draw, line, font_option):
    font = TITLE_FONT  if font_option == 'regular' else TITLE_FONT_BOLD 
    line_bbox = draw.textbbox((0, 0), line, font)
    return line_bbox[3] - line_bbox[1]