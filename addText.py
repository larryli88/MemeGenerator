from PIL import Image, ImageDraw, ImageFont
import urllib.request
import time

# add text to the input.jpg
def addT(text, imgFile):
    # open image
    img = Image.open("." + imgFile)
    # get image size
    W, H = img.size
    # using PIL to add text
    draw = ImageDraw.Draw(img)
    # include font
    myFont = ImageFont.truetype("impact.ttf", 30)
    # centering text
    w, h = draw.textsize(text, font=myFont)
    draw.text(((W-w)/2,(H-h)/2), text, fill="white", font=myFont)
    # save the image with text to output.jpg
    outFile = 'output' + (str)(time.time()) + '.jpg'
    img.save('./static/' + outFile)
    return outFile