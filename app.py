from flask import Flask, render_template,flash, redirect, url_for, session, logging, request
from chartBuilder import *
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, SelectField, FloatField, FormField, TextField,  validators
from forms import *
from checklogin import check_login
<<<<<<< HEAD
=======
from user import *
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
from werkzeug.security import generate_password_hash, check_password_hash
import os

#initalizing application as instance of flask class
<<<<<<< HEAD
=======
'''
TODO:(Frontend)
    - Proper authentication displaying-Needs Backend, logic is there
    - Feed

TODO:(Backend)
    - login/logout 
    - User profile databases
    - Edit profile integration

TODO:(General)
    - Figure out how to encoporate some sorta algorithm
    - Idea, use huffman encoding or some variation for password encryption

    Order of things to do:
    -update profile
    -feed 
    -viewing other persons profile

'''

>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
# Create flask object to encapsulate the whole webapp
app = Flask(__name__)

# Connect the app to the SQL database "codestats" using SQLalchemy framework
# Allow transmission of signals to track when items are added, etc.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:molly101@localhost/codestats'
=======
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1271427@localhost/codestats'
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
# Create a handle for the database
db = SQLAlchemy(app)

# Designate a folder to store the profile pictures, and specify allowed file types
<<<<<<< HEAD
UPLOAD_FOLDER = os.path.basename('static') + "/"
ALLOWED_EXTENTIONS = ['jpg', 'png', 'pdf']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


=======
UPLOAD_FOLDER = os.path.basename('static')
ALLOWED_EXTENTIONS = ['jpg', 'png', 'pdf']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
# Function to create an existing user object by withdrawing their information from the batabase.
# Can select object based on ID or username.
def getUser(db, param):
    if type(param) == str:
        username = param
        user = db.session.query(User).filter_by(username = username).first()
    elif type(param) == int:
        Id = param
        user = db.session.query(User).filter_by(id = Id).first()
    return user

# User class, that contains all relevant information pertaining to a user.
class User(db.Model):
    # refer to the table 'users' within the database.
    __tablename__ = 'users'

    # Link each attribute with it's corresponding column in the table
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    username = db.Column('username', db.Unicode, unique=True)
    email = db.Column('email', db.Unicode)
    password = db.Column('password', db.Unicode)
    github = db.Column('github', db.Unicode)
    degree = db.Column('degree', db.Unicode)
    gpa = db.Column('gpa', db.Unicode)
    bio = db.Column('bio', db.Unicode)
    year = db.Column('year', db.Unicode)
    project1 = db.Column('project1', db.Unicode)
    project2= db.Column('project2', db.Unicode)
    project3= db.Column('project3', db.Unicode)
    p1desc = db.Column('p1desc', db.Unicode)
    p2desc = db.Column('p2desc', db.Unicode)
    p3desc = db.Column('p3desc', db.Unicode)
    job1 = db.Column('job1', db.Unicode)
    job2 = db.Column('job2', db.Unicode)
    job3 = db.Column('job3', db.Unicode)
    j1desc= db.Column('j1desc', db.Unicode)
    j2desc = db.Column('j2desc', db.Unicode)
    j3desc = db.Column('j3desc', db.Unicode)
    lang1 = db.Column('lang1', db.Unicode)
    lang2 = db.Column('lang2', db.Unicode)
    lang3 = db.Column('lang3', db.Unicode)
    lang4 = db.Column('lang4', db.Unicode)
    lang5 = db.Column('lang5', db.Unicode)
    lang6 = db.Column('lang6', db.Unicode)
    lang7 = db.Column('lang7', db.Unicode)
    l1skill = db.Column('l1skill', db.Unicode)
    l2skill = db.Column('l2skill', db.Unicode)
    l3skill = db.Column('l3skill', db.Unicode)
    l4skill = db.Column('l4skill', db.Unicode)
    l5skill = db.Column('l5skill', db.Unicode)
    l6skill = db.Column('l6skill', db.Unicode)
    l7skill = db.Column('l7skill', db.Unicode)
    picture = db.Column('picture', db.Unicode)

    # init method used upon registration of a new client. Only the first four attributes are necessary.
    def __init__(self, id, name, username, email, password):
        self.name = name
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.github = None
        self.degree = None
        self.gpa = None
        self.bio = None
        self.year = None
        self.project1 = None
        self.project2 = None
        self.project3 = None
        self.p1desc = None
        self.p2desc = None
        self.p3desc = None
        self.job1 = None
        self.job2 = None
        self.job3 = None
        self.j1desc = None
        self.j2desc = None
        self.j3desc = None
        self.lang1 = None
        self.lang2 = None
        self.lang3 = None
        self.lang4 = None
        self.lang5 = None
        self.lang6 = None
        self.lang7 = None
        self.l1skill = None
        self.l2skill = None
        self.l3skill = None
        self.l4skill = None
        self.l5skill = None
        self.l6skill = None
        self.l7skill = None
<<<<<<< HEAD
        self.picture = UPLOAD_FOLDER + "blank.png"
=======
        self.picture = "/static/blank.jpg"
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
    # Method called to push new attributes into the database
    def updateUser(self, db):
        db.session.add(self)
        db.session.commit()



#adding routing decorator for intial bootup
@app.route('/')
def welcome():
    return render_template('welcome.html')

#profile route
<<<<<<< HEAD
@app.route('/profile')
@check_login
=======
# @check_login
@app.route('/profile')
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
def profile():
    username = session['username']
    # Create the user object of the user currently logged in
    user = getUser(db, username)

<<<<<<< HEAD
=======
    # Gather variables to be used in HTML template and graphs
    name = user.name
    degree = user.degree
    year = user.year
    gpa = user.gpa
    email = user.email
    github = user.github
    bio = user.bio

    job1_h = user.job1
    job2_h = user.job2
    job3_h = user.job3
    
    job1_des = user.j1desc
    job2_des = user.j2desc
    job3_des = user.j3desc

    proj1_h = user.project1
    proj2_h = user.project2
    proj3_h = user.project3

    proj1_des = user.p1desc
    proj2_des = user.p2desc
    proj3_des = user.p3desc


    lang1_l = user.lang1
    lang2_l = user.lang2
    lang3_l = user.lang3
    lang4_l = user.lang4
    lang5_l = user.lang5
    lang6_l = user.lang6
    lang7_l = user.lang7

    lang1_s = user.l1skill
    lang2_s = user.l2skill
    lang3_s = user.l3skill
    lang4_s = user.l4skill
    lang5_s = user.l5skill
    lang6_s = user.l6skill
    lang7_s = user.l7skill
    picture = user.picture
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
    languages = []

    # make a list of languages to pass to chart builder
    for i in range(1,8):
<<<<<<< HEAD
    	exec('languages.append((user.lang{}, user.l{}skill))'.format(i,i))
    
    # Create charts to display on profile page
    
    lang_chart = build_language_chart(languages)
    
    # Populate the HTML file with the user attributes
    return render_template('profile.html', langchart = lang_chart, 
        name = user.name,
        picture = user.picture,
        username = username,
        degree = user.degree,
        year = user.year,
        gpa = user.gpa,
        email = user.email,
        github = user.github,
        bio = user.bio,
        job1_h = user.job1,
        job2_h = user.job2,
        job3_h = user.job3,
        job1_des = user.j1desc,
        job2_des = user.j2desc,
        job3_des = user.j3desc,

        proj1_h = user.project1,
        proj2_h = user.project2,
        proj3_h = user.project3,

        proj1_des = user.p1desc,
        proj2_des = user.p2desc,
        proj3_des = user.p3desc
        )

#home route
@app.route('/home', methods=['GET', "POST"])
@check_login
=======
    	exec('languages.append((lang{}_l, lang{}_s))'.format(i,i))
    
    # Create charts to display on profile page
    time_chart = build_time_chart()
    lang_chart = build_language_chart(languages)
    skill_tree = build_skill_tree()
    # Populate the HTML file with the user attributes
    return render_template('profile.html', langchart = lang_chart, skilltree = skill_tree,
    picture = picture,
    name = name,
    username = username,
    degree = degree,
    year = year,
    gpa = gpa,
    email = email,
    github = github,
    bio = bio,
    job1_h = job1_h,
    job2_h = job2_h,
    job3_h = job3_h,
    job1_des = job1_des,
    job2_des = job2_des,
    job3_des = job3_des,

    proj1_h = proj1_h,
    proj2_h = proj2_h,
    proj3_h = proj3_h,

    proj1_des = proj1_des,
    proj2_des = proj2_des,
    proj3_des = proj3_des
    )

#home(feed) route
# @check_login
@app.route('/home', methods=['GET', "POST"])
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
def home():

    # To be exectued when the user clicks on another user, to view their profile.
    if request.method == 'POST':
        # Create user object for the user who's profile is to be displayed.
        user = getUser(db, request.form['submit'])

<<<<<<< HEAD
        picture = user.picture
        languages = []

        # make a list of languages to pass to chart builder
        for i in range(1,8):
            exec('languages.append((user.lang{}, user.l{}skill))'.format(i,i))
        lang_chart = build_language_chart(languages)

        # pass the user parameters to the HTML file to be displayed
        return render_template('viewprofile.html', langchart = lang_chart, 
            name = user.name,
            picture = user.picture,
            username = username,
            degree = user.degree,
            year = user.year,
            gpa = user.gpa,
            email = user.email,
            github = user.github,
            bio = user.bio,
            job1_h = user.job1,
            job2_h = user.job2,
            job3_h = user.job3,
            job1_des = user.j1desc,
            job2_des = user.j2desc,
            job3_des = user.j3desc,

            proj1_h = user.project1,
            proj2_h = user.project2,
            proj3_h = user.project3,

            proj1_des = user.p1desc,
            proj2_des = user.p2desc,
            proj3_des = user.p3desc
            )
=======
        #profile vars
        name = user.name
        degree = user.degree
        year = user.year
        gpa = user.gpa
        email = user.email
        github = user.github
        bio = user.bio

        job1_h = user.job1
        job2_h = user.job2
        job3_h = user.job3
        
        job1_des = user.j1desc
        job2_des = user.j2desc
        job3_des = user.j3desc

        proj1_h = user.project1
        proj2_h = user.project2
        proj3_h = user.project3

        proj1_des = user.p1desc
        proj2_des = user.p2desc
        proj3_des = user.p3desc

        lang1_l = user.lang1
        lang2_l = user.lang2
        lang3_l = user.lang3
        lang4_l = user.lang4
        lang5_l = user.lang5
        lang6_l = user.lang6
        lang7_l = user.lang7

        lang1_s = user.l1skill
        lang2_s = user.l2skill
        lang3_s = user.l3skill
        lang4_s = user.l4skill
        lang5_s = user.l5skill
        lang6_s = user.l6skill
        lang7_s = user.l7skill
        picture = user.picture

        
        

        time_chart = build_time_chart()
        lang_chart = build_language_chart()
        skill_tree = build_skill_tree()
        return render_template('viewprofile.html', langchart = lang_chart, skilltree = skill_tree, picture = picture,
        name = name,
        username = username,
        degree = degree,
        year = year,
        gpa = gpa,
        email = email,
        github = github,
        bio = bio,
        interests = None,
        job1_h = job1_h,
        job2_h = job2_h,
        job3_h = job3_h,
        job1_des = job1_des,
        job2_des = job2_des,
        job3_des = job3_des,

        proj1_h = proj1_h,
        proj2_h = proj2_h,
        proj3_h = proj3_h,

        proj1_des = proj1_des,
        proj2_des = proj2_des,
        proj3_des = proj3_des
        )
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
    else:
        # Gather all users from the database, and create a list of them
        users = User.query.all()

        # Pass the users to the corresponding template to be displayed.
        return render_template('home.html', users=users)

#viewProfile route
@app.route('/viewprofile')
<<<<<<< HEAD
@check_login
=======
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
def viewprofile():

    # Create a user object for the profile to be viewed
    username = request.args['username']
    user = getUser(db, username)
<<<<<<< HEAD
=======

    #profile vars
    name = user.name
    degree = user.degree
    year = user.year
    gpa = user.gpa
    email = user.email
    github = user.github
    bio = user.bio

    job1_h = user.job1
    job2_h = user.job2
    job3_h = user.job3
    
    job1_des = user.j1desc
    job2_des = user.j2desc
    job3_des = user.j3desc

    proj1_h = user.project1
    proj2_h = user.project2
    proj3_h = user.project3

    proj1_des = user.p1desc
    proj2_des = user.p2desc
    proj3_des = user.p3desc


    lang1_l = user.lang1
    lang2_l = user.lang2
    lang3_l = user.lang3
    lang4_l = user.lang4
    lang5_l = user.lang5
    lang6_l = user.lang6
    lang7_l = user.lang7

    lang1_s = user.l1skill
    lang2_s = user.l2skill
    lang3_s = user.l3skill
    lang4_s = user.l4skill
    lang5_s = user.l5skill
    lang6_s = user.l6skill
    lang7_s = user.l7skill
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
    picture = user.picture

    #create a language lsit to pass to chart builder.
    languages = []
    for i in range(1,8):
<<<<<<< HEAD
        exec('languages.append((user.lang{}, user.l{}skill))'.format(i,i))
    

    lang_chart = build_language_chart(languages)

    # pass the user parameters to the HTML file to be displayed
    return render_template('viewprofile.html', langchart = lang_chart, 
    name = user.name,
    picture = user.picture,
    username = username,
    degree = user.degree,
    year = user.year,
    gpa = user.gpa,
    email = user.email,
    github = user.github,
    bio = user.bio,
    job1_h = user.job1,
    job2_h = user.job2,
    job3_h = user.job3,
    job1_des = user.j1desc,
    job2_des = user.j2desc,
    job3_des = user.j3desc,

    proj1_h = user.project1,
    proj2_h = user.project2,
    proj3_h = user.project3,

    proj1_des = user.p1desc,
    proj2_des = user.p2desc,
    proj3_des = user.p3desc
=======
        exec('languages.append((lang{}_l, lang{}_s))'.format(i,i))
    

    time_chart = build_time_chart()
    lang_chart = build_language_chart(languages)
    skill_tree = build_skill_tree()

    # pass the user parameters to the HTML file to be displayed
    return render_template('viewprofile.html', langchart = lang_chart, skilltree = skill_tree,
    name = name,
    picture = picture,
    username = username,
    degree = degree,
    year = year,
    gpa = gpa,
    email = email,
    github = github,
    bio = bio,
    job1_h = job1_h,
    job2_h = job2_h,
    job3_h = job3_h,
    job1_des = job1_des,
    job2_des = job2_des,
    job3_des = job3_des,

    proj1_h = proj1_h,
    proj2_h = proj2_h,
    proj3_h = proj3_h,

    proj1_des = proj1_des,
    proj2_des = proj2_des,
    proj3_des = proj3_des
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
    )

#about route
@app.route('/about')
def about():

    # display the about page.
    return render_template('about.html')


#edit profile route
<<<<<<< HEAD

@app.route('/editprofile', methods=['GET', 'POST'])
@check_login
=======
# @check_login
@app.route('/editprofile', methods=['GET', 'POST'])
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
def editprofile():
    form = EditProfile(request.form)
    if request.method == 'POST':
        username = session['username']
        user = getUser(db, username)

        #personal info variables
<<<<<<< HEAD
=======
        user.name = form.name.data
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
        user.degree = form.degree.data
        user.year = form.year.data
        user.gpa = form.gpa.data
        user.email = form.email.data
<<<<<<< HEAD
        user.github = form.github.data
=======
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
        user.bio = form.bio.data
        #project variables
        user.project1 = form.First_Project.data['name']
        user.project2 = form.Second_Project.data['name']
        user.project3 = form.Third_Project.data['name']
        user.p1desc = form.First_Project.data['description']
        user.p2desc = form.Second_Project.data['description']
        user.p3desc = form.Third_Project.data['description']
        #work variables
        user.job1 = form.Work_Experience_One.data['name']
        user.job2 = form.Work_Experience_Two.data['name']
        user.job3 = form.Work_Experience_Three.data['name']
<<<<<<< HEAD
        user.j1desc = form.Work_Experience_One.data['description']
        user.j2desc = form.Work_Experience_Two.data['description']
=======
        user.j1desc = form.Work_Experience_Three.data['description']
        user.j2desc = form.Work_Experience_Three.data['description']
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
        user.j3desc = form.Work_Experience_Three.data['description']

        #language variables
        user.lang1 = form.Language_1.lang.data
        user.lang2 = form.Language_2.lang.data
        user.lang3 = form.Language_3.lang.data
        user.lang4 = form.Language_4.lang.data
        user.lang5 = form.Language_5.lang.data
        user.lang6 = form.Language_6.lang.data
        user.lang7 = form.Language_7.lang.data
        user.l1skill = form.Language_1.skill.data
        user.l2skill = form.Language_2.skill.data
        user.l3skill = form.Language_3.skill.data
        user.l4skill = form.Language_4.skill.data
        user.l5skill = form.Language_5.skill.data
        user.l6skill = form.Language_6.skill.data
        user.l7skill = form.Language_7.skill.data

        # commit the changes to the database
        user.updateUser(db)

        flash('Profile Updated', 'success')
        return redirect(url_for('profile'))

    return render_template('editprofile.html', form=form)

# for uploading photos
@app.route('/upload', methods=['POST'])
def uploadPhoto():

    # get the current user's username.
    username = session['username']
    user = getUser(db, username)

    # get the uploaded file and check if the file is of exepted type (in ALLOWED_EXTENTIONS)
    file = request.files['image']
    name = file.filename
    extention = name.split('.')[-1]

    if extention in ALLOWED_EXTENTIONS:
        # The file is valid, so change it's name to username.extention and save it in the deignated folder
        file.filename = username+'.'+extention
<<<<<<< HEAD
        user.picture = UPLOAD_FOLDER +  file.filename
=======
        user.picture = "/static/" + file.filename
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
        user.updateUser(db)
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)

        flash("Upload Successful")
        return redirect(url_for("editprofile"))
    else:
        flash('Not a valid file type. Please use jpg, pnj, or pdf.')
        return redirect(url_for("editprofile"))

#sign up route
@app.route('/signUp', methods=['GET', "POST"])
def signUp():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        form.init_user(db)
        #data user has entered
        flash('You are now registered!', 'success')
        return redirect(url_for('editprofile'))

    return render_template('signUp.html', form=form)


#signin route
@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        # get the entered username and password
        username = request.form['username']
        password_candidate = request.form['password']
<<<<<<< HEAD
        potential_user = getUser(db, username)
        # get the password hash that corresponds to the entered username, from the database
        try:
            match = check_password_hash(potential_user.password, password_candidate)
        except AttributeError:
            flash('No username associated with  user', 'danger')
            return redirect(url_for('signIn'))
        # check that the entered password would create the correct hash
        
=======

        # get the password hash that corresponds to the entered username, from the database
        potential_user = getUser(db, username)

        # check that the entered password would create the correct hash
        match = check_password_hash(potential_user.password, password_candidate)
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7

        if match:
            # if password is correct, log the person in and go to their profile.
            session['logged_in'] = True
            session['username'] = username
            flash('You are now logged in!', 'success')
            return redirect(url_for('profile'))

        # If not correct, display error message and ask again
        else:
            error = 'Username not found'        
            return render_template('signIn.html', error=error)

    return render_template('signIn.html')

#logout
@app.route('/signOut')
def logout():
<<<<<<< HEAD
    session.clear()#remove session variables
=======
    session.clear()
>>>>>>> 389f1e44bb21faadd31c559c04c999c4ba9488e7
    flash('Logged Out!', 'success')
    return redirect(url_for('welcome'))



if __name__ == "__main__":
    app.secret_key='cmput275'
    print('Booting Up')
    app.run(debug = True)