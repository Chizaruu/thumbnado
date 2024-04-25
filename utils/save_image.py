# save_image.py

def save_image(img, filename):
    try:
        img.save("./thumbnails/" + filename + ".png")
        print(f"Image saved successfully: {filename}.png")
    except Exception as e:
        print(f"Error saving image: {str(e)}")
