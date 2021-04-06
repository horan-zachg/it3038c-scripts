from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    name = 'Zach'
    return render_template("index.html",name=name)
    #, name=myName

@app.route('/welcome', methods=['POST'])
def Welcome():
    return render_template("Welcome.html", myName=request.form['myName'])