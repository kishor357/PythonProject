import sqlite3
import re
from Employee_login import Login_Employee


conn = sqlite3.connect('PythonProject.db')
c = conn.cursor()


def create_table():
    c.execute('drop table if exists signUpEmployee')
    c.execute('Create table if not exists signUpEmployee(Name text, Email text primary key, Phone text, Password text)')



def dynamic_data_entry():

    Name = input("Enter the Name. ")
    name_pattern = r'^[a-zA-Z ]+$'
    while(not(re.match(name_pattern, Name))):
        Name = input("Enter the Name. ")


    Email = input("Enter the Email. ")
    email_pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    while(not(re.match(email_pattern, Email))):
        Email = input("Enter the Email. ")

    Phone = input("Enter the Phone Number. ")
    phone_pattern = '^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
    while(not(re.match(phone_pattern, Phone))):
        Phone = input("Enter the Phone Number. ")

    Password = input("Enter the Password. ")
    password_pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    while(not(re.match(password_pattern, Password))):
        Password = input("Enter the Password. ")

    c.execute("insert into signUpEmployee(Name, Email, Phone, Password) values(?,?,?,?)", (Name, Email, Phone, Password))
    conn.commit()

def read_from_database():
    c.execute("select * from signUpEmployee")
    for row in c.fetchall():
        print(row)

class Employee:

    def EMPLOYEE_SIGNUP(self):
        create_table()
        dynamic_data_entry()
        read_from_database()
        c.close()
        conn.close()
        login_employee = Login_Employee()
        login_employee.LOGIN_EMPLOYEE()

