# ---------------- Imports ----------------
from PIL import Image, ImageFont, ImageDraw
from math import floor

# ---------------- Settings ----------------
font_size = 128 # only even !!!
size_multiplier = 1 #default 1 (without changes)
color_mode = 1 # 0 - colors from the picture, 1 - your color 
your_color = (255, 255, 255) # sets the color of the symbols when color_mode == 1
img_dir = "imgs\\ava 1.png" # image directory example: "imgs\\test.png"
background_color = (0,0,0) # background color :3
your_font = "fonts\JetBrainsMono-Regular.ttf" #font
grad_mode = 1 # default = 0 - from dark to light, 1 - from light to darkness

# ---------------- !!!!! ----------------

# the larger the image size, the longer the code execution
# the smaller the font size, the longer the code execution

# result in - results\\result.png

# ---------------- !!!!! ----------------

#==========================================================================================================
#==========================================================================================================
#==========================================================================================================

# ---------------- Code ----------------
img = Image.open(img_dir)
result_img = Image.new("RGB", (img.width*size_multiplier, img.height*size_multiplier), background_color)
draw = ImageDraw.Draw(result_img)
font = ImageFont.truetype(your_font, font_size)
match grad_mode:
    case 0:
        grad = " .:!/r(l1Z4H9W8$@" #17 symbols, (255*3) 765 / 17 = 45, from dark to light
    case 1:
        grad = "@$8W9H4Z1l(r/!:. " #17 symbols, (255*3) 765 / 17 = 45, from light to darkness

for i in range(img.width):
    for j in range(img.height):
        if i%(font_size/2) == 0 and j%(font_size/2) == 0:
            if color_mode == 0:
                if floor(sum(img.getpixel((i,j))[:3]) / 45)-1 == -1:
                    draw.text((i*size_multiplier, j*size_multiplier), grad[floor(sum(img.getpixel((i,j))[:3]) / 45)], font=font, fill=(img.getpixel((i,j))))
                else:
                    draw.text((i*size_multiplier, j*size_multiplier), grad[floor(sum(img.getpixel((i,j))[:3]) / 45)-1], font=font, fill=(img.getpixel((i,j))))
            else:
                if floor(sum(img.getpixel((i,j))[:3]) / 45)-1 == -1:
                    draw.text((i*size_multiplier, j*size_multiplier), grad[floor(sum(img.getpixel((i,j))[:3]) / 45)], font=font, fill=(your_color))
                else:
                    draw.text((i*size_multiplier, j*size_multiplier), grad[floor(sum(img.getpixel((i,j))[:3]) / 45)-1], font=font, fill=(your_color))

result_img = result_img.crop((font_size,font_size,result_img.width, result_img.height))
result_img.save("results\\result.png")