from POS import generate

img = generate(
    img_dir = "img.png",
    font = "DejaVuSansMono-Bold.ttf",
    font_size = 18,
    color = (230, 230, 255),
    background_color = (10, 10, 10),
    bright_limit = 10,
    size_multiplier = 2,
)

img.save("result.png")