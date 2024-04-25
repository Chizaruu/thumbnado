# Thumbnado 🌪️

Thumbnado is a powerful and customizable thumbnail generator that allows you to easily create stunning thumbnails. Whether you need thumbnails for your YouTube videos, social media posts, or any other purpose, Thumbnado has got you covered!

## Features ✨

- 🌈 Customizable background colors
- 🖼️ Support for logo overlays and patterns
- 📝 Customizable title and subtitle text
- 🎨 Adjustable font styles, sizes, and colours
- 🎭 Multiple text alignment options

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

4. Place your desired logo images in the `Logos` folder.

5. Place your desired font files in the `fonts` folder.

6. Update the `configuration.py` file with your desired settings, such as background colour, font sizes, and file paths.

## Usage 🚀

To generate thumbnails using Thumbnado, follow these steps:

1. Customize the settings in the `configuration.py` file according to your preferences. You can modify the background colour, image size, logo size and spacing, overlay opacity, title and subtitle text, font options, text outline settings, and alignment options.

2. Run the `main.py` script to generate the thumbnail:
   ```
   python main.py
   ```

   The generated thumbnail will be saved with the title name specified in the `configuration.py` file.

## Configuration Options 🎛️

Thumbnado provides various configuration options to customize your thumbnails. Here are some of the key options available in the `configuration.py` file:

- `BG_COLOR`: Define the background colour of the thumbnail.
- `WIDTH` and `HEIGHT`: Set the dimensions of the thumbnail image.
- `LOGO_SIZE` and `LOGO_SPACING`: Adjust the size and spacing of the logo images.
- `DIRECTION`: Choose the direction of the logo pattern (horizontal, vertical, diagonal_left, diagonal_right).
- `OVERLAY_OPACITY`: Set the opacity of the overlay rectangle.
- `TITLE_TEXT` and `SUBTITLE_TEXT`: Specify the title and subtitle text for the thumbnail.
- `MAX_TITLE_WIDTH`: Set the maximum width of the title text.
- `TITLE_FONT_SIZE` and `SUBTITLE_FONT_SIZE`: Adjust the title and subtitle text font sizes.
- `REGULAR_FONT`, `BOLD_FONT`, and `SUBTITLE_FONT`: Specify the font files for regular, bold, and subtitle text.
- `MIN_LINES`: Set the minimum number of lines for the title text.
- `FONT_OPTION`: Choose between regular and bold font options.
- `TEXT_OUTLINE_WIDTH` and `TEXT_OUTLINE_COLOR`: Customize the text outline settings.
- `ALIGNMENT`: Select the alignment option for the text (left, right, center, justified).
- `LOGO_FOLDER`: Specify the folder containing the logo images.

Feel free to explore and modify these options to achieve your desired thumbnail design.

## Contributing 🤝

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow the existing code style and guidelines.

## License 📄

This project is licensed under the [MIT License](LICENSE).
