from flask import Flask, render_template
import requests
import os

app = Flask('app')  # Creating Flask Instance


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/index')
def home_page_route():  # have this to route homepage from other pages. To keep tone same as last time
    return render_template('index.html')


@app.route('/webstack')
def webstack():
    return render_template('webstack.html')

@app.route('/rmarkdown')
def rmarkdown():
    return render_template('rmarkdown.html')

@app.route('/anova')
def rmarkdown2():
    return render_template('anova.html')

@app.route('/exp')
def exp():
    return render_template('exp.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/edu')
def edu():
    return render_template('edu.html')





app.run(host='0.0.0.0', port=8080)
