from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
from data import personalInfo
from chartBuilder import *
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, SelectField, FloatField, FormField, TextField,  validators
from functools import wraps

#initalizing application as instance of flask class

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1271427@localhost/CodeApp'
db = SQLAlchemy(app)
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

class MultiForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    description = TextField('Description')

class LangForm(Form):
    lang = SelectField('Language', choices = [
        ('cpp','C'), 
        ('c','C++'), 
        ('py','Python'),
        ('java','Java'),
        ('js','JavaScript'),
        ('rb','Ruby'),
        ('go','Go'),
        ('s','Assemby'),
        ('mat','Matlab'),
        ('na','None')
        ])
        
    skill = SelectField('Skill Level', choices = [
        ('0', 'No Experiance'),
        ('1', 'Beginner'),
        ('2', 'Advancing'),
        ('3', 'Intermediate'),
        ('4', 'Advanced'),
        ('5', 'Expert')
        ])
    

class EditProfile(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    degree = SelectField('Degree', choices = [('compe','Computer Engineering'), 
    ('softeng','Software Engineering'), 
    ('compsci','Computer Science')])

    year = SelectField('Degree', choices = [('1st','First Year'), 
    ('2nd','Second Year'), 
    ('3rd','Third Year'), 
    ('4th','Fourth Year'), 
    ('5th','Fifth Year+'), 
    ('gd','Graduated')])

    gpa = FloatField('GPA', [validators.Length(min=2, max=2)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    github = StringField('Email', [validators.Length(min=6, max=50)])
    bio = TextField('Bio')

    #projects field
    project1 = FormField(MultiForm)
    project2 = FormField(MultiForm)
    project3 = FormField(MultiForm)
    #work experiance field
    work1 = FormField(MultiForm)
    work2 = FormField(MultiForm)
    work3 = FormField(MultiForm)
    #languages field
    lang1 = FormField(LangForm)
    lang2 = FormField(LangForm)
    lang3 = FormField(LangForm)
    lang4 = FormField(LangForm)
    lang5 = FormField(LangForm)
    lang6 = FormField(LangForm)
    lang7 = FormField(LangForm)
    #skill tree




def check_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in', 'danger')
            return redirect(url_for('singIn'))
    return wrap

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