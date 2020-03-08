from flask import Flask, render_template, url_for
from flask import request
import urllib.request
from getImage import getImg
from addText import addT
import os
import time
app = Flask(__name__)

# starting the web app
@app.route('/')
def start():
    return render_template('index.html', hidden="hidden")

# api for searching image matching user's input
@app.route('/search', methods=['GET', 'POST'])
def search():
    if not request.form['search_input']:
        return render_template('index.html')
    if request.method == 'POST': 
        search_text = request.form['search_input']
        imgs = getImg(search_text)
        # if their are less than 4 images in result, prompt user to try another key word
        if len(imgs) < 4:
             return render_template('index.html', hidden="")
        return render_template('image_res.html', hidden="hidden", res0=imgs[0], res1=imgs[1],res2=imgs[2],res3=imgs[3])

# api for choosing an image from search result
@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        imgUrl = request.form['imgFile']
        savedImg = "input" + (str)(time.time()) + ".jpg"
        urllib.request.urlretrieve(imgUrl, "./static/" + savedImg)
        return render_template('add_text.html', inputImg=url_for('static', filename=savedImg))

# api for adding text to the chosen image
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_text = request.form['add_input']
        imgFile = request.form['imgFile']
        outFile = addT(add_text, imgFile)
        return render_template('image_text.html', img=url_for('static', filename=outFile))

# api for starting over
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', hidden="hidden")

if __name__ =="__main__":
    app.run(debug=True,port=8080)