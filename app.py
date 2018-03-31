from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
from data import personalInfo
from chartBuilder import *
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, SelectField, FloatField, FormField, TextField,  validators
from forms import *
from checklogin import check_login

#initalizing application as instance of flask class
'''
TODO:(Frontend)
    - Finish edit profile page-DONE
    - Style
    - Proper authentication displaying-Needs Backend, logic is there
    - Feed
    - Documentation

TODO:(Backend)
    - login/logout 
    - User profile databases
    - Edit profile integration

TODO:(General)
    - Refactor
    - Comment/Update Readme
    - Figure out how to encoporate some sorta algorithm
    - Idea, use huffman encoding or some variation for password encryption

'''

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1271427@localhost/CodeApp'
db = SQLAlchemy(app)

#outdated
personal_info = personalInfo()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    username = db.Column('username', db.Unicode, unique=True)
    email = db.Column('email', db.Unicode)
    password = db.Column('password', db.Unicode)


    def __init__(self, id, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password



#adding routing decorator for intial bootup
@app.route('/')
def welcome():
    return render_template('welcome.html')

#profile route
# @check_login
@app.route('/profile')
def profile():
    #TODO: pull user data from database, and construct charts from data
    time_chart = build_time_chart()
    lang_chart = build_language_chart()
    skill_tree = build_skill_tree()
    return render_template('profile.html', profile = personal_info, timechart = time_chart, langchart = lang_chart, skilltree = skill_tree)

#home(feed) route
# @check_login
@app.route('/home')
def home():
    #TODO: Pull user data, build profiles off it
    return render_template('home.html')

#about route
@app.route('/about')
def about():
    return render_template('about.html')

#signin route
@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
       #get form fields
       username = request.form['username']
       password_candidate = request.form['password']

       #TODO: create cursor
       #TODO: get user by username
       #TODO: if rows found, get stored password and check with candidate
       #TODO: implement logic below once password has been returned from database
        # if(password matched):
        #    session['logged_in'] = True
        #    session['username'] = username

        #    flash('You are now logged in!', 'success')
        #    return redirect(url_for('profile'))
        # else:
        #     error = 'Invalid Login'
        #     return render_template('signIn.html', error=error)
        #TODO: Close connection


    else:
        error = 'Username not found'        
        return render_template('signIn.html', error=error)


#edit profile route
# @check_login
@app.route('/editprofile', methods=['GET', 'POST'])
def editprofile():
    form = EditProfile(request.form)
    if request.method == 'POST' and form.validate():
        #personal info variables
        name = form.name.data
        degree = form.degree.data
        year = form.year.data
        gpa = form.gpa.data
        email = form.email.data
        bio = form.bio.data


        #project variables
        project1_n = form.First_Project.name.data
        project1_d = form.First_Project.description.data

        project2_n = form.Second_Project.name.data
        project2_d = form.Second_Project.description.data

        project3_n = form.Third_Project.name.data
        project3_d = form.Third_Project.description.data

        #work variables
        job1_n = form.Work_Experience_One.name.data
        job1_d = form.Work_Experience_One.description.data

        job2_n = form.Work_Experience_Two.name.data
        job2_d = form.Work_Experience_Two.description.data

        job3_n = form.Work_Experience_Three.name.data
        job3_d = form.Work_Experience_Three.description.data


        #language variables
        lang1_l = form.Language_1.lang.data
        lang1_s = form.Language_1.skill.data

        lang2_l = form.Language_2.lang.data
        lang2_s = form.Language_2.skill.data

        lang3_l = form.Language_3.lang.data
        lang3_s = form.Language_3.skill.data

        lang4_l = form.Language_4.lang.data
        lang4_s = form.Language_4.skill.data

        lang5_l = form.Language_5.skill.data
        lang5_s = form.Language_5.lang.data

        lang6_l = form.Language_6.skill.data
        lang6_s = form.Language_6.lang.data

        lang7_l = form.Language_7.lang.data
        lang7_s = form.Language_7.skill.data

        #TODO: create cursor, access and add this to the database
        #TODO: commit to db
        #TODO: close connection to db
        

        flash('Profile Updated', 'success')
        redirect(url_for('profile'))

    return render_template('editprofile.html', form=form)

#sign up route
@app.route('/signUp', methods=['GET', "POST"])
def signUp():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        #data user has entered
       name = form.name.data
       email = form.email.data
       username = form.username.data
       password = form.password.data

       #TODO: create cursor, access and add this to the database
       #TODO: commit to db
       #TODO: close connection to db

       flash('You are now registered!', 'success')
       return redirect(url_for('signIn'))

    return render_template('signUp.html', form=form)

#logout
@app.route('/signOut')
def logout():
    #TODO: Finish session code
    session.clear()
    flash('Logged Out!')
    return redirect(url_for('signIn'))


@app.route('/viewprofile', methods=['GET', 'POST'])
def view_profile():
    #TODO: read fetch request, pull user data on the requested user
    #TODO: create class that displays other users data
    
    return render_template('viewprofile.html')


if __name__ == "__main__":
    app.secret_key='cmput275'
    app.run(debug = True)