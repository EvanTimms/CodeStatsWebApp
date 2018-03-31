# CodeStats

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

* Milestone 2: Database setup

This part of the project involved building as simple database in mysql to eventually hold all the user data. Some of the frontend work that
went in at this stage included setting up forms to register/login/logout. The library wtforms was used for this part of the project.

* Milestone 3: Feed/Edit Profile features

Using flasks dyanmic html features, we were able to set up a basic feed that pulled data from the database and displayed it for the user currently
logged in. This way the user would be able to view other peoples resumes provided they were logged in. This also allowed us to change the navbar 
depending on if the user was logged in or not

