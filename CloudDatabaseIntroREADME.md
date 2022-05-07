# Overview

This is a little introduction to a Cloud Database where I have 
stored some data about the classes and specializations from the MMO World of Warcraft.

My cloud database has some stored information with some basic details about the various
classes in World of Warcraft. One storing the specializations for each class and another 
storing the roles for each class. The third is where I store data that can be manipulated
like when the damage changes or a role changes. The fourth is a log file where it will 
automatically keep a log of all of the changes to the Top DPS list.

This software is a simple way to keep track of the top dps charts as the game World of Warcraft changes. The most useful table is the Top DPS table, where I can add and change the damage and role data of the various classes. I also added some small exceptions so you can't add random stuff to the Top DPS list other than the actual classes in the game. 


[Demonstration Part 1](https://www.youtube.com/watch?v=Z7sVIE91rQo&ab_channel=GarrettStanger)
[Demonstration Part 2](https://www.youtube.com/watch?v=7QxkABtm87s&ab_channel=GarrettStanger)

# Cloud Database

I am using the Google Firestore Cloud Database system with python as the backend programming language. There are three tables that I am storing data in so far, two are more of static lists that I made while learning how to add items into my database. The Top DPS is the one that I created to be able to be manipulated more than the previous two. The fourth is a log file that stores a timestamp with the data change whenever the DPS list changes. 

# Development Environment

I used the Google Firestore or Firebase to create my cloud database. I used the python language for the backend programming and used Visual Studio Code for my editor.

# Useful Websites

* [Google Firebase Tutorials](https://firebase.google.com/docs/firestore)
* [Firestore Cloud Database Workshop](https://byui-cse.github.io/cse310-course/workshops/Cloud_DB/CSE310_Workshop_Cloud_DB.pdf)
* [Stack Overflow](https://stackoverflow.com/)

# Future Work

* I need to clean up the display interface so it doesn't display so ugly.
* I plan on designing more intricate queries for the database and having more helpful data to be able to query from.
* I also want to research into if it is possible to get a working front end interface that is more friendly to non-coders.