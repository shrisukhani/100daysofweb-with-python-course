from flask import render_template
from program import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/bombay')
def bombay():
    return render_template('bombay.html')

@app.route('/college')
def college():
    return render_template('college.html')

@app.route('/work')
def work():
    return render_template('work.html')