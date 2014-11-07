
This generates a database-file todo.db with tables called todo and three columns id, task, and status. id is a unique id for each row, which is used later on to reference the rows. The column task holds the text which describes the task, it can be max 100 characters long. Finally, the column status is used to mark a task as open (value 1) or closed (value 0).
3. Using Bottle for a web-based ToDo list
Now it is time to introduce Bottle in order to create a web-based application. But first, we need to look into a basic concept of Bottle: routes.
3.1. Understanding routes
Basically, each page visible in the browser is dynamically generated when the page address is called. Thus, there is no static content. That is exactly what is called a “route” within Bottle: a certain address on the server. So, for example, when the page http://localhost:8080/todo is called from the browser, Bottle “grabs” the call and checks if there is any (Python) function defined for the route “todo”. If so, Bottle will execute the corresponding Python code and return its result: python todo.py.
3.2. First Step - Showing All Open Items
So, after understanding the concept of routes, let’s create the first one. The goal is to see all open items from the ToDo list:
￼￼
COURSE
tecnologías para la programación y el diseño web i
YEAR
2
GROUP BL
￼
￼￼
GRADE
ASSESSMENT
SURNAME
FIRSTNAME
ID
￼￼
REMARKS
Homework 2: web application basics and roles in a web team
DELIVERY DATE 09/10/2014
DUE DATE 23/10/2014
￼
import sqlite3
con = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
con.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
con.commit()
