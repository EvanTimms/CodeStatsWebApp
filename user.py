from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def getUser(self, db, username):
    user = db.session.query(Users).filter_by(username = username).first()
    return user

class User(db.Model):
    __tablename__ = 'Users'
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



    def __init__(self, id, name, username, email, password):
        self.name = name
        self.username = username
        self.password = password
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

    def updateUser(self, db):
        db.session.add(self)
        db.session.commit()