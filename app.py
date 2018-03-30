from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
from data import personalInfo
from chartBuilder import *
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

#initalizing application as instance of flask class

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
personal_info = personalInfo()

#registration class that takes form data from html
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email= StringField('Email', [validators.Length(min=6, max=50)])
    password  =PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

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
@app.route('/signUp', methods=['GET', "POST"])
def signUp():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        #TODO: Access database and input user values
        pass
        #flash('You are now registered and can log in')

        # return redirect(url_for('signIn'))
    return render_template('signUp.html', form=form)

if __name__ == "__main__":
    app.secret_key='cmput275'
    app.run(debug = True)