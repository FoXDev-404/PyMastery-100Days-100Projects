# TODO: Recareating the Hirst spot penting

import colorgram


colors = colorgram.extract('./image.png', 6)

first_color = colors[0]
rgb = first_color.rgb
print(colors)