import sys
import os
from PIL import Image, ImageOps, ImageDraw
import colorsys

# Calculate the average color of an image
def average_color(image):    
    width, height = image.size
    pixels = image.load()
    r, g, b = 0, 0, 0
    count = 0
    for x in range(width):
        for y in range(height):
            r_, g_, b_, a = pixels[x, y]
            if a == 0:
                continue
            r += r_
            g += g_
            b += b_
            count += 1
    return (r//count, g//count, b//count)


# Get the complement color of a color
def complement_color(color):
    return (255-color[0], 255-color[1], 255-color[2])


# Get the triadic color of a color
def triadic_color(color):
    # Find a color that is 120 degrees apart in the color wheel
    r, g, b = color
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    if max_value == r:
        return (min_value, max_value, (min_value + max_value)//2)
    elif max_value == g:
        return ((min_value + max_value)//2, min_value, max_value)
    else:
        return (max_value, (min_value + max_value)//2, min_value)


# Get the tetradic color of a color
def tetradic_color(color):
    h, s, v = colorsys.rgb_to_hsv(color[0]/255, color[1]/255, color[2]/255)
    h = (h + 0.25) % 1
    return tuple(map(lambda x: int(x*255), colorsys.hsv_to_rgb(h, s, v)))


# Get the analogous color of a color
def analogous_color(color):
    r, g, b = color
    r = (r + 85) % 256
    g = (g + 85) % 256
    b = (b + 85) % 256
    return (r, g, b)


def add_background_with_margin(image_path, output_path, color_scheme, margin=0, bg_color=None):
    # Open the image
    img = Image.open(image_path)

    # Calculate the average color of the image if no background color is provided
    if bg_color is None:
        avg_color = average_color(img)
        if color_scheme == "complement":
            bg_color = complement_color(avg_color)
        elif color_scheme == "triadic":
            bg_color = triadic_color(avg_color)
        elif color_scheme == "analogous":
            bg_color = analogous_color(avg_color)
        elif color_scheme == "tetradic":
            bg_color = tetradic_color(avg_color)

    # Create a background image with the specified color and the same size as the original image
    bg = Image.new("RGBA", img.size, (bg_color[0], bg_color[1], bg_color[2], 255))

    # Paste the original image on top of the background
    bg.paste(img, mask=img.split()[3]) # 3 is the alpha channel

    # Add a margin to the image if specified
    if margin > 0:
        bg = ImageOps.expand(bg, border=margin, fill=(bg_color[0], bg_color[1], bg_color[2], 255))

    # Save the resulting image
    bg.save(output_path)


def main():
    usage = "Usage: python add_background.py <complement|triadic|tetradic|analogous> <directory_path> <margin> [bg_color]"

    # Check if the directory path is provided
    if len(sys.argv) < 2:
        print("Error: Missing color scheme argument\n" + usage)
        sys.exit()

    # Get the color scheme from the command-line argument
    color_scheme = sys.argv[1]

    # Check if the directory path is provided
    if len(sys.argv) < 3:
        print("Error: Missing directory argument\n" + usage)
        sys.exit()

    # Get the directory path from the command-line argument
    directory_path = sys.argv[2]

    # Get the margin size and background color from the command-line arguments if provided
    margin = 0
    bg_color = None
    if len(sys.argv) > 3:
        margin = int(sys.argv[3])
    if len(sys.argv) > 4:
        bg_color = tuple(map(int, sys.argv[4].split(",")))

    # Create the output directory if it doesn't exist
    output_dir = os.path.join(directory_path, "output", color_scheme)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process all PNG files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".png"):
            image_path = os.path.join(directory_path, filename)
            output_path = os.path.join(output_dir, filename)
            add_background_with_margin(image_path, output_path, color_scheme, margin, bg_color)

if __name__ == "__main__":
    main()