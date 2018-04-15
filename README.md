# Code Stats

## By Evan Perret-Timms and Ben Ripka

### Description

This is a applicton that allows users to build a simple resume on a website and
be able to view others. Like a linkedin for programmers, this site mainly focusses on connecting
programmers. When logged it, you can view other peoples profiles throught the home tab,
and edit your own settings in the profile. The site uses the Python flask framework as a backend with MySQL 
as the database. Flask is great as it is a relavility lightweight framework that supports almost all the features you could need for a web application. MySQL is great as a database sever and works great with Flasks SQL handler SQLAlchemy.

### Milestones

* Milestone 1: Basic Frontend

The first major task involed linking up the basic html outline with the  flask app to create the website skeleton. Boostrap was used for making the site look nicer that what otherwise could of been achieved with normal html and css and for a fraction of the time. No backend or database implementation at this point.

* Milestone 2: Database setup

This part of the project involved building as simple database in MySQL to eventually hold all the user data. Some of the frontend work that went in at this stage included setting up forms to register/login/logout. The library wtforms was used for this part of the project.

* Milestone 3: User Authentication

At this point the backend database had been set up. To user authentication we used some additional libraies from flask and created some session variables to make sure users that were not signed up could not access a profile by navigating directly in the brower.

* Milestone 4: Feed/Edit Profile features

Flask is great because it integrates with the Jinja2 template engine. With this engine, we were able to pull user data from the database and display it on the frontend. We were able to set up a basic feed that pulled data from the database and displayed it for the user currently logged in. This way the user would be able to view other peoples resumes provided they were logged in. This also allowed us to change the navbar depending on if the user was logged in or not.

* Milestone 5: Password Hashing, Profile Picture

As a added security feature, the Python Werkzeug module was used to encrypt and decrypt stored passwords.

#### How To Run

The following packages are required to run Code Stats:
- Flask (sudo pip3 install Flask)
-pygal (sudo pip3 install pygal)
- mysql (sudo apt-get install mysql-server libmysqlclient-dev)
- sql_alchemy (sudp pip3 install flask_sqlalchemy)
- wtforms (sudo pip3 install wtforms)
- Flask MySQLdb (sudo pip3 install Flask-mysqldb)

#### Data Base Setup
Follow the following instructions to install mysql and set up the database correctly
- mysql will prompt you for a password. Write this password down as you will be using it to log in.
- run in terminal: mysql -u root -p 
- enter the password you wrote down
- Once logged in, following the below instructions and you will be ready to go!

1. copy the code form the file database.sql into the terminal. If there are no syntax erros the database should now contain the table for users.

2. In app.py:
 app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:PASSWORDHERE@localhost/codestats' 
 change PASSWORDHERE to the password you used setting up mysql.

 You're all good to go! Run app.py and open localhost 5000 in chrome.