from PIL import Image, ImageDraw, ImageFont
import urllib.request

#URL = 'https://farm66.staticflickr.com/65535/49626114092_75a34b9cbb.jpg'

def addT(text):
    #with urllib.request.urlopen(URL) as url:
    #    with open('input.jpg', 'wb') as f:
    #        f.write(url.read())
    img = Image.open('./static/input.jpg')
    draw = ImageDraw.Draw(img)
    draw.text((50,50), text)
    #img.show()
    img.save('./static/output.jpg')