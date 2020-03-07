from flask import Flask, render_template, url_for
from flask import request
from getImage import getImg
from addText import addT
import os
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
        getImg(search_text)
        return render_template('image_res.html')

# api for choosing an image from search result
@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        imgNum = request.form['img']
        # rename the chosen image to input.jpg for adding text
        os.rename("./static/input" + str(imgNum) + ".jpg", "./static/input.jpg")
        return render_template('add_text.html')

# api for adding text to the chosen image
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_text = request.form['add_input']
        addT(add_text)
        return render_template('image_text.html')

if __name__ =="__main__":
    app.run(debug=True,port=8080)