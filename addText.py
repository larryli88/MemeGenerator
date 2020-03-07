from PIL import Image, ImageDraw, ImageFont
import urllib.request

# add text to the input.jpg
def addT(text):
    img = Image.open('./static/input.jpg')
    # using PIL to add text
    draw = ImageDraw.Draw(img)
    draw.text((50,50), text)
    # save the image with text to output.jpg
    img.save('./static/output.jpg')