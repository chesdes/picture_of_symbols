from POS import generate

img = generate(
    img_dir = "imgs/img.png",
    font="fonts/JetBrainsMono-Bold.ttf",
    font_size=16,
    size_multiplier=2,
    bright_limit=1,
    color=(255,255,255),
    background_color=(10,10,10),
    grad=".√:-=+*#%@  "
)    
img.save("results/result.png")