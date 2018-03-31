from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
from data import personalInfo
from chartBuilder import *
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps

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
def welcome():
    #builds charts
    time_chart = build_time_chart()
    lang_chart = build_language_chart()
    skill_tree = build_skill_tree()
    #renders html web page
    return render_template('welcome.html', profile = personal_info, timechart = time_chart, langchart = lang_chart, skilltree = skill_tree)

#profile route
@app.route('/profile')
def profile():
    time_chart = build_time_chart()
    lang_chart = build_language_chart()
    skill_tree = build_skill_tree()
    return render_template('profile.html', profile = personal_info, timechart = time_chart, langchart = lang_chart, skilltree = skill_tree)

#home route
@app.route('/home')
def home():
    return render_template('home.html')

#about route
@app.route('/about')
def about():
    return render_template('about.html')

#signin route
@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        pass
        #Get form fields
        # username = request.form['username']
        # password_candidate = request.form['password']

        #TODO: create cursor and check with sql database
        #TODO: Compare passwords
        #TODO: if verified, app.logger.info('PASSWORD MATCHED)
    else:
        app.logger.info('NO USER')
        
            
        
    return render_template('signIn.html')

@app.route('/editprofile', methods=['GET', 'POST'])
def editprofile():
    return render_template('editprofile.html')

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


def check_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in', 'danger')
            return redirect(url_for('singIn'))
    return wrap

#logout
@app.route('/signOut')
def logout():
    #TODO: Finish session code
    session.clear()
    flash('Logged Out!')
    return redirect(url_for('signIn'))

if __name__ == "__main__":
    app.secret_key='cmput275'
    app.run(debug = True)