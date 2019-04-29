import sqlite3

with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()

    c.execute(""" create table posts (title text, post text) """)

    c.execute('insert into posts values("Good", "I\'m Good")')
    c.execute('insert into posts values("Well", "I\'m Well")')
    c.execute('insert into posts values("Excellent", "I\'m Excellent")')
    c.execute('insert into posts values("Okay", "I\'m Okay")') 

       

