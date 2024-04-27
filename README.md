# Thumbnado 🌪️

Thumbnado is a powerful and customizable thumbnail generator that allows you to easily create stunning thumbnails. Whether you need thumbnails for your YouTube videos, social media posts, or any other purpose, Thumbnado has got you covered!

## Features ✨

- 🌈 Customizable background colors
- 🖼️ Support for logo overlays and patterns
- 📝 Customizable title and subtitle text
- 🎨 Adjustable font styles, sizes, and colours
- 🎭 Multiple text alignment options
- 💾 Easy-to-use command-line interface for generating thumbnails

## Installation 💻

To use Thumbnado, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/thumbnado.git
   ```

2. Navigate to the project directory:
   ```
   cd thumbnado
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Place your desired logo images in the `Logos` folder.  (Optional)

5. Place your desired font files in the `fonts` folder.  (Optional)

6. Update the `configuration.py` file with your desired settings, such as background colour, font sizes, and file paths. (Optional)

## Usage 🚀

To generate thumbnails using Thumbnado, use the following command:
`python main.py [options]`  

Available options:
- `--background-color R G B`: Set the background color (RGB values, default: 54 57 63)
- `--image-width WIDTH`: Set the image width (default: 1280)
- `--image-height HEIGHT`: Set the image height (default: 720)
- `--logo-size SIZE`: Set the logo size (default: 110)
- `--logo-spacing SPACING`: Set the logo spacing (default: 125)
- `--logo-direction DIRECTION`: Set the logo direction (horizontal, vertical, diagonal-left, diagonal-right, default: horizontal)
- `--overlay-opacity OPACITY`: Set the overlay opacity (0-255, default: 127)
- `--title-text TEXT`: Set the title text (default: "A Really Cool Title!")
- `--subtitle-text TEXT`: Set the subtitle text (default: "Subtitle Text Here")
- `--title-font-size SIZE`: Set the title font size (default: 140)
- `--subtitle-font-size SIZE`: Set the subtitle font size (default: 100)
- `--font-style STYLE`: Set the font style (regular, bold, default: bold)
- `--title-font PATH`: Set the path to the title font file (default: "fonts/Amaranth-Regular.otf")
- `--title-font-bold PATH`: Set the path to the bold title font file (default: "fonts/Amaranth-Bold.otf")
- `--subtitle-font PATH`: Set the path to the subtitle font file (default: "fonts/Amaranth-Regular.otf")

- `--min-title-lines LINES`: Set the minimum number of lines for the title text (default: 1)
- `--text-outline-width WIDTH`: Set the text outline width (default: 1)
- `--text-outline-color R G B A`: Set the text outline color (RGBA values, default: 0 0 0 255)
- `--text-alignment ALIGNMENT`: Set the text alignment (left, right, center, justified, default: center)
- `--logo-directory DIRECTORY`: Set the directory containing logo images (default: "Logos")

Example usage:

`python main.py --background-color 255 0 0 --image-width 800 --image-height 600 --logo-size 80 --logo-spacing 100 --logo-direction vertical --overlay-opacity 200 --title-text "My Awesome Thumbnail" --subtitle-text "Check out this cool video!" --title-font-size 120 --subtitle-font-size 80 --font-style regular --min-title-lines 2 --text-outline-width 2 --text-outline-color 0 0 0 200 --text-alignment left --logo-directory "path/to/logos" --title-font "path/to/custom-title-font.ttf" --title-font-bold "path/to/custom-title-font-bold.ttf" --subtitle-font "path/to/custom-subtitle-font.ttf"`

## Contributing 🤝

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow the existing code style and guidelines.

## License 📄

This project is licensed under the [MIT License](LICENSE).
