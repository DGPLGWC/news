import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/environment')
def environment():
    return render_template(
        'environment.html',
        topic = 'Environment'
    )

@app.route('/equality')
def equality():
    return render_template(
        'equality.html',
        topic = 'Equality'
    )

@app.route('/education')
def education():
    return render_template(
        'education.html',
        topic = 'Education'
    )

@app.route('/feminism')
def feminism():
    return render_template(
        'feminism.html',
        topic = 'Feminism'
    )

@app.route('/science')
def science():
    return render_template(
        'science.html',
        topic = 'Science'
    )
# app.run(host = os.getenv('IP','0.0.0.0'), port = int(os.getenv('PORT',8080)))

