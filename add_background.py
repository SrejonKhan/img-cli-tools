import skia
import os
import sys

def add_white_background(input_path, output_path):
    # Load the original image
    image = skia.Image.open(input_path)

    # Create a white background image with the same size as the original image
    width, height = image.width(), image.height()
    surface = skia.Surface.MakeRaster(skia.ImageInfo.MakeN32Premul(width, height))
    canvas = surface.getCanvas()
    canvas.clear(skia.Color4f(1.0, 1.0, 1.0, 1.0))

    # Draw the original image on the white background
    canvas.drawImage(image, 0, 0)

    # Save the result
    surface.makeImageSnapshot().save(output_path, skia.EncodedImageFormat.kPNG)

def main():
    if len(sys.argv) != 2:
        print("Usage: python add_background.py <directory_path>")
        sys.exit(1)

    input_dir = sys.argv[1]

    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: {input_dir} is not a valid directory")
        sys.exit(1)

    output_folder = os.path.join(input_dir, "output")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all PNG files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_folder, filename)
            print(output_path)
            add_white_background(input_path, output_path)

if __name__ == "__main__":
    main()
