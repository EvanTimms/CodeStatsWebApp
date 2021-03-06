create database codestats;

use codestats;

create table users (
    
id int(11) not null auto_increment,
password varchar(200) not null,
name varchar(100) not null,
email varchar(100) not null,
username varchar(30) not null,
github varchar(50),
degree varchar(80),
gpa varchar(5),
bio varchar(1000),
year varchar(50),
project1 varchar(50),
project2 varchar(50),
project3 varchar(50),
p1desc varchar(1000),
p2desc varchar(1000),
p3desc varchar(1000),
job1 varchar(80),
job2 varchar(80),
job3 varchar(80),
j1desc varchar(1000),
j2desc varchar(1000),
j3desc varchar(1000),
lang1 varchar(30),
lang2 varchar(30),
lang3 varchar(30),
lang4 varchar(30),
lang5 varchar(30),
lang6 varchar(30),
lang7 varchar(30),
l1skill varchar(5),
l2skill varchar(5),
l3skill varchar(5),
l4skill varchar(5),
l5skill varchar(5),
l6skill varchar(5),
l7skill varchar(5),
picture varchar(50),
primary key (id));