
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session, redirect
from templates import readCSV

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "thisisaveryverysecretkeywhy?becauseisaidso"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        session['mpg'] = ""
        return render_template("home.html")
    if request.method == "POST":
            session['mpg']=readCSV.findMPG(request.form["carMake"], request.form["carModel"], request.form["carYear"])
            session['info']=readCSV.findInfo()
    return render_template("home.html", mpgText=session.get('mpg'), infoText=session.get('info'))

@app.route('/route.html')
def route():
    return render_template("route.html")

@app.route('/welcome.html')
def welcome():
    return render_template("welcome.html")
