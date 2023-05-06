# img-cli-tools

I've developed this handy toolbox for [GoodWords](https://play.google.com/store/apps/details?id=com.primalproductions.goodwords), because I had to do some works with images, that could be boring if I had to do it manually.

## Available tools

### Add background color to image(s):

```shell
python add_background.py <complement|triadic|tetradic|analogous> <directory_path> [margin] [bg_color]
```

**Syntax:**

- `<complement|triadic|tetradic|analogous>` - Required: Choose a color scheme to generate a background color.
- `<directory_path>` - Required: The path to the directory containing the images to add a background to.
- `[margin]` - Required: The margin (in pixels) between the image and the background.
- `[bg_color]` - Optional: The background color to use (in hex format). If not provided, a random color will be generated.

---

### Blur image(s)

```bash
python blur_images.py <input_dir> <output_dir> [--blur-radius <blur_radius> --append-to-filename <append_to_filename>]
```

**Syntax:**

- `<input_dir>` - Required: The path to the directory containing the images to blur.
- `<output_dir>` - Required: The path to the directory where the blurred images will be saved.
- `--blur-radius <blur_radius>` - Optional: The radius of the Gaussian blur filter to apply (in pixels).
- `--append-to-filename <append_to_filename>` - Optional: A string to append to the filename of the blurred image.

---

### Compress Image

```bash
python compress_image.py <image_path>
```

**Syntax:**

- `<image_path>` - Required: The path to the image file to compress using the TinyPNG API.

**API:**

Get your TinyPNG API Key [here](https://tinypng.com/developers).
