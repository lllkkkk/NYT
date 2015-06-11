__author__ = 'Aryan'

import sqlite3
conn = sqlite3.connect('Article_database1')

class MyDatabase:

    # DELETE FROM COMPANY WHERE ID = 7;
# Defined variable to be stored in the database
    # need to changed when data extraction is over
    def var_declare(self):
        self.title = ('me')
        self.date = ('me')
        self.article_story = ('me')
        self.keyword = ('me')
        self.web_url = ('me')

# Database table creation with 5 columns
    def create_table(self, title, date, article_story, keyword, web_url):
        self.c = conn.cursor()
        #c.execute(''' CREATE TABLE data1(title text,Web_url text,date text,article_story text,Keyword text )''')
        self.c.execute("DELETE FROM data1 WHERE title = 'title';")   #delete query to delete unwanted rows
        self.c.execute("DELETE FROM data1 WHERE title = 'me';")
        self.c.execute('INSERT INTO data1 VALUES(?,?,?,?,?)',(title, date, article_story, keyword, web_url))
       # Insert query to create rows of table

    def print(self):        # Print just for checking table values
        for row in self.c.execute('SELECT * FROM data1'):
            print(row)

x = MyDatabase()
x.var_declare()
x.create_table(x.title, x.date, x.article_story, x.keyword, x.web_url)
y = x.print()
conn.commit()
