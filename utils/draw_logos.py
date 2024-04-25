# draw_logos.py

import os
from PIL import Image

def draw_logos(img, logos, direction, logo_spacing, bg_color):
    logo_index = 0
    if direction == 'horizontal':
        for y in range(0, img.height, logo_spacing):
            for x in range(0, img.width, logo_spacing):
                if x < img.width:
                    bg_image = Image.new('RGBA', (logos[0].width, logos[0].height), bg_color)
                    bg_image.paste(logos[logo_index], (0, 0), mask=logos[logo_index])
                    img.paste(bg_image, (x, y))
                    logo_index = (logo_index + 1) % len(logos)
    elif direction == 'vertical':
        for x in range(0, img.width, logo_spacing):
            for y in range(0, img.height, logo_spacing):
                if y < img.height:
                    bg_image = Image.new('RGBA', (logos[0].width, logos[0].height), bg_color)
                    bg_image.paste(logos[logo_index], (0, 0), mask=logos[logo_index])
                    img.paste(bg_image, (x, y))
                    logo_index = (logo_index + 1) % len(logos)
    elif direction == 'diagonal_left':
        for y in range(0, img.height + logo_spacing, logo_spacing - 5):
            for x in range(0, img.width + logo_spacing, logo_spacing - 15):
                if x < img.width and y < img.height:
                    bg_image = Image.new('RGBA', (logos[0].width, logos[0].height), bg_color)
                    bg_image.paste(logos[logo_index], (0, 0), mask=logos[logo_index])
                    img.paste(bg_image, (x, y))
                    logo_index = (logo_index + 1) % len(logos)
    elif direction == 'diagonal_right':
        for y in range(0, img.height + logo_spacing, logo_spacing + 5):
            for x in range(0, img.width + logo_spacing, logo_spacing + 15):
                if x < img.width and y < img.height:
                    bg_image = Image.new('RGBA', (logos[0].width, logos[0].height), bg_color)
                    bg_image.paste(logos[logo_index], (0, 0), mask=logos[logo_index])
                    img.paste(bg_image, (x, y))
                    logo_index = (logo_index + 1) % len(logos)

    return img

def load_logos(logo_folder, logo_size):
    logo_files = [file for file in os.listdir(logo_folder) if file.endswith('.png') or file.endswith('.jpg')]
    logos = []
    for file in logo_files:
        logo = Image.open(os.path.join(logo_folder, file))
        logo.thumbnail((logo_size, logo_size))
        logos.append(logo)
    return logos