from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    name = 'Zach'
    return render_template("index.html",name=name)
    #, name=myName

@app.route('/welcome', methods=['POST'])
def Welcome():

    return render_template("welcome.html", myName=request.form['myName'])

##added route picture
@app.route('/picture')
def picture():

    return render_template("picture.html")

@app.route('/home')
def home():

    return render_template("welcome.html")