from flask import Flask, render_template, url_for
from flask import request
from getImage import getImg
from addText import addT
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        search_text = request.form['search_input']
        getImg(search_text)
        return render_template('image_res.html')

@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        imgNum = request.form['img']
        os.rename("./static/input" + str(imgNum) + ".jpg", "./static/input.jpg")
        return render_template('add_text.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_text = request.form['add_input']
        addT(add_text)
        return render_template('image_text.html')

if __name__ =="__main__":
    app.run(debug=True,port=8080)