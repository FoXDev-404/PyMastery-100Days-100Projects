# TODO: Recreating the Hirst spot painting

import colorgram
import os

# Use absolute path to be certain of image location
image_path = os.path.join(os.path.dirname(__file__), "image.png")
colors = colorgram.extract(image_path, 20)

first_color = colors[0]
rgb = first_color.rgb
print(rgb)

rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
print(rgb_colors)