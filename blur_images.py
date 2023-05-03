import os
import argparse
from PIL import Image, ImageFilter

# Define the argument parser
parser = argparse.ArgumentParser(description="Add blur to all images in a directory")
parser.add_argument("input_dir", type=str, help="the input directory containing images")
parser.add_argument(
    "output_dir", type=str, help="the output directory to save blurred images"
)
parser.add_argument(
    "--blur-radius", type=int, default=10, help="the radius of the blur effect"
)
parser.add_argument(
    "--append-to-filename",
    type=str,
    default="",
    help="prefix that will be added to all output files",
)

# Parse the arguments
args = parser.parse_args()

# Create the output directory if it doesn't exist
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

# Iterate over all images in the input directory
for filename in os.listdir(args.input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image and apply the blur effect
        image_path = os.path.join(args.input_dir, filename)
        image = Image.open(image_path)
        blurred_image = image.filter(ImageFilter.GaussianBlur(args.blur_radius))

        # Save the blurred image to the output directory
        output_path = os.path.join(args.output_dir, args.append_to_filename + filename)
        blurred_image.save(output_path)

        print(f"Saved blurred image: {output_path}")
