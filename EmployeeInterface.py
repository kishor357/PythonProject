import sqlite3
import re
from datetime import date

conn = sqlite3.connect('PythonProject.db')
c = conn.cursor()


def create_table():
    c.execute('drop table if exists EmployeeInterface')
    c.execute('Create table if not exists EmployeeInterface(Added_date Date, Employee_Email text , Book_Name text, '
              'Author_Name text, '
              'Publisher_Name text, Price int)')



def dynamic_data_entry(Email):

    Added_date = date.today()

    BookName = input("Enter the Book Name. ")
    bookname_pattern = r'^[a-zA-Z ]+$'
    while (not (re.match(bookname_pattern, BookName))):
        BookName = input("Enter the Book Name. ")

    AuthorName = input("Enter the Author Name. ")
    authorname_pattern = r'^[a-zA-Z ]+$'
    while (not (re.match(authorname_pattern, AuthorName))):
        AuthorName = input("Enter the Author Name. ")

    PublisherName = input("Enter the Publisher Name. ")
    publisher_pattern = r'^[a-zA-Z ]+$'
    while (not (re.match(publisher_pattern, PublisherName))):
        BookName = input("Enter the Publisher Name. ")

    Price = int(input("Enter the price of book. "))

    c.execute("insert into EmployeeInterface(Added_date, Employee_Email, Book_Name, Author_Name, Publisher_Name, "
              "Price) values(?,?,?,?,?,?)",
              (Added_date, Email, BookName, AuthorName, PublisherName, Price))

    conn.commit()

def read_from_database():
    c.execute("select * from EmployeeInterface")
    for row in c.fetchall():
        print(row)

class EmployeeInterface:

    def EMPLOYEE_INTERFACE(self, Email):
        create_table()
        dynamic_data_entry(Email)
        read_from_database()
        c.close()
        conn.close()



