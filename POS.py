# ---------------- Imports ----------------
from PIL import Image, ImageFont, ImageDraw
from random import randint

# ---------------- Code ----------------
def generate(
        img_dir: str, 
        font: str, 
        color: tuple[int, int, int] | list[tuple[int, int, int]] = None, 
        background_color: tuple[int] = (0,0,0), 
        font_size: int = 16, 
        bright_limit: int = 0, 
        size_multiplier: int = 1,
        grad: str = " .:-=+*#%@"
        ) -> Image:
    
    img = Image.open(img_dir).convert("RGB")
    result_img = Image.new("RGB", (img.width*size_multiplier, img.height*size_multiplier), background_color)
    draw = ImageDraw.Draw(result_img)
    font = ImageFont.truetype(font, font_size)
    grad = ' '*bright_limit + grad

    if color == None: color_mode = 0
    elif type(color) == tuple: color_mode = 1
    else: color_mode = 2

    pixels = list(img.getdata())
    grad_len = len(grad) - 1
    color_len = len(color) if color_mode == 2 else 0

    for i in range(img.width):
        for j in range(img.height):
            xy = (i*size_multiplier, j*size_multiplier)
            r, g, b = pixels[j * img.width + i]
            brightness = 0.299 * r + 0.587 * g + 0.114 * b
            index = int(brightness / 255 * (grad_len - 1))
            symbol = grad[index]
            
            match color_mode:
                case 0: draw_color = img.getpixel((i,j))
                case 1: draw_color = color
                case 2: draw_color = color[randint(1, color_len)-1]
                
            if i%(font_size/2) == 0 and j%(font_size/2) == 0 and symbol != ' ':
                draw.text(xy, symbol, font=font, fill=draw_color)
                    
    result_img = result_img.crop((font_size,font_size,result_img.width, result_img.height))
    img.close()
    return result_img