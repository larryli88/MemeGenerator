from PIL import Image, ImageDraw, ImageFont
import urllib.request
import time

# add text to the input.jpg
def addT(text, imgFile):
    img = Image.open("." + imgFile)
    # using PIL to add text
    draw = ImageDraw.Draw(img)
    draw.text((50,50), text)
    # save the image with text to output.jpg
    outFile = 'output' + (str)(time.time()) + '.jpg'
    img.save('./static/' + outFile)
    return outFile