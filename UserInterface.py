import sqlite3
import re
from datetime import date

conn = sqlite3.connect('PythonProject.db')
c = conn.cursor()


def create_table():
    c.execute('drop table if exists UserInterface')
    c.execute('Create table if not exists UserInterface(Added_date Date, User_Email text , Book_Name text)')


def dynamic_data_entry(Email):


    Added_date = date.today()

    BookName = input("Enter the Book Name. ")
    bookname_pattern = r'^[a-zA-Z ]+$'
    while (not (re.match(bookname_pattern, BookName))):
        BookName = input("Enter the Book Name. ")


    c.execute("insert into UserInterface(Added_date, User_Email, Book_Name) values(?,?,?)",
              (Added_date, Email, BookName))

    conn.commit()

def read_from_database1():
    c.execute("select * from UserInterface")
    for row in c.fetchall():
        print(row)

def read_from_database():
    c.execute("select Book_Name, Author_Name, Publisher_Name, Price  from EmployeeInterface")
    for row in c.fetchall():
        print(row)

class UserInterface:

    def USER_INTERFACE(self, Email):
        print("THESE ARE THE BOOKS AVAILABLE WITH US. ")
        print("Book Name, Author Name, Publisher Name, Price.")
        read_from_database()
        create_table()
        dynamic_data_entry(Email)
        read_from_database1()
        c.close()
        conn.close()



