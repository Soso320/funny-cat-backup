import os
from PIL import Image, ImageDraw, ImageFont

directory = r'/home/soso/Desktop/Grabber/us/'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        funnyname = (os.path.join(directory, filename))

        image = Image.open(funnyname)
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('Prototype.ttf', size=200)

        (x, y) = (0, 0)

        message = "us"

        color = 'rgb(0, 255, 0)'  # white color

        draw.text((x, y), message, fill=color, font=font)

        image.save(f'us/kiss_{filename}.png')
