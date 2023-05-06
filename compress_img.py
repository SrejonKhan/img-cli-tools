import os
import tinify
import argparse
import api_key_management

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("image_path", help="path to the image file")
args = parser.parse_args()

api_key = api_key_management.get_api_key("tinify")

if api_key == "":
    print("TinyPNG API Key - ")
    api_key_management.set_api_key("tinify", input())
    api_key = api_key_management.get_api_key("tinify")

tinify.key = api_key

dirname = os.path.dirname(args.image_path)
basename = os.path.basename(args.image_path)
source = tinify.from_file(args.image_path)
source.to_file(os.path.join(dirname, "optimized_" + basename))
