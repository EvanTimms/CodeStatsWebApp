# Code Stats

## By Evan Perret-Timms and Ben Ripka

### Description

This is a applicaiton that allows users to build a simple resume on a website and
be able to view others. Like a linkedin for programmers, this site mainly focusses on connecting
programmers. When logged it, you can view other peoples profiles throught the home tab,
and edit your own settings in the profile.

### Milestones

* Milestone 1: Basic Frontend

Linked up basic html with flask app to create website skeleton. Boostrap was used for making the site look nicer
that what otherwise could of been achieved with normal html and css. No backend or database implementation at this point.

* Milestone 2: User Authentication

At this point the backend database had been set up. To user authentication we used some additional libraies from flask and created some session variables to make sure users that were not signed up could not access a profile.

* Milestone 3: Database setup

This part of the project involved building as simple database in mysql to eventually hold all the user data. Some of the frontend work that
went in at this stage included setting up forms to register/login/logout. The library wtforms was used for this part of the project.

* Milestone 4: Feed/Edit Profile features

Using flasks dyanmic html features, we were able to set up a basic feed that pulled data from the database and displayed it for the user currently
logged in. This way the user would be able to view other peoples resumes provided they were logged in. This also allowed us to change the navbar 
depending on if the user was logged in or not

#### How To Run

The following packages are required to run Code Stats:
- Flask (sudo pip3 install Flask)
-pygal (sudo pip3 install pygal)
- mysql (sudo apt-get install mysql-server mysqlclient-dev)
- sql_alchemy (sudp pip3 install flask_sqlalchemy)
- wtforms (sudo pip3 install wtforms)
- Flask MySQLdb (sudo pip3 install Flask-mysqldb)

#### Data Base Setup
Follow the following instructions to install mysql and set up the database correctly
- Installing: sudo apt-get install mysql-server libsqlclient-dev
- mysql will prompt you for a password. Write this password down as you will be using it to log in.
- run in terminal: mysql -u root -p 
- enter the password you wrote down
- Once logged in, following the below instructions and you will be ready to go!

1. copy the code form the file database.sql into the terminal. If there are no syntax erros the database should now contain the table for users.

2. In app.py:
 app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:PASSWORDHERE@localhost/codestats' 
 change PASSWORD here to the password you used setting up mysql.

 You're all good to go!