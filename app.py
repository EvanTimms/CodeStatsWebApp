from flask import Flask, render_template
from data import personalInfo
from chartBuilder import *
#initalizing application as instance of flask class

app = Flask(__name__)
personal_info = personalInfo()



#adding routing decorator for intial bootup
@app.route('/')
def index():
    #builds charts
    time_chart = build_time_chart()
    lang_chart = build_language_chart()
    skill_tree = build_skill_tree()
    #renders html web page
    return render_template('index.html', profile = personal_info, timechart = time_chart, langchart = lang_chart, skilltree = skill_tree)

#home route
@app.route('/index')
def home():
    time_chart = build_time_chart()
    lang_chart = build_language_chart()
    skill_tree = build_skill_tree()
    return render_template('index.html', profile = personal_info, timechart = time_chart, langchart = lang_chart, skilltree = skill_tree)

#about route
@app.route('/about')
def about():
    return render_template('about.html')

#signin route
@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

#sign up route
@app.route('/signUp')
def singUp():
    return render_template('signUp.html')

if __name__ == "__main__":
    app.run(debug = True)