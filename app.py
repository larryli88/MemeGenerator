from flask import Flask, render_template, url_for
from flask import request
import urllib.request
from getImage import getImg
from addText import addT
import os
import time
app = Flask(__name__)

# debug
@app.route('/')
def hello_world():
    return 'Hello, World!'

# api for searching image matching user's input
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST': 
        search_text = request.form['search_input']
        imgs = getImg(search_text)
        return render_template('image_res.html', res0=imgs[0], res1=imgs[1],res2=imgs[2],res3=imgs[3])

# api for choosing an image from search result
@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        imgUrl = request.form['img']
        savedImg = "input" + (str)(time.time()) + ".jpg"
        urllib.request.urlretrieve(imgUrl, "./static/" + savedImg)
        # rename the chosen image to input.jpg for adding text
        #os.rename("./static/input" + str(imgNum) + ".jpg", "./static/input.jpg")
        return render_template('add_text.html', inputImg=url_for('static', filename=savedImg))

# api for adding text to the chosen image
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_text = request.form['add_input']
        imgFile = request.form['imgFile']
        #print(imgFile)
        outFile = addT(add_text, imgFile)
        return render_template('image_text.html', img=url_for('static', filename=outFile))

if __name__ =="__main__":
    app.run(debug=True,port=8080)