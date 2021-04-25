import sqlite3
import re
from EmployeeInterface import EmployeeInterface


conn = sqlite3.connect('PythonProject.db')
c = conn.cursor()



def read_from_database(Email):
    c.execute("select Password from signUpEmployee where Email = ?", (Email,))
    for pwd in c.fetchone():
        print(pwd)
    return pwd



class Login_Employee:


    def LOGIN_EMPLOYEE(self):
        print("Employee Login. ")

        Email = input("Enter the Email. ")
        email_pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        while (not (re.match(email_pattern, Email))):
            Email = input("Enter the Email. ")

        Password = input("Enter the Password. ")
        password_pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        while (not (re.match(password_pattern, Password))):
            Password = input("Enter the Password. ")

        password = read_from_database(Email)
        if(password == Password):
            print("Successfully logged in. ")
            c.close()
            conn.close()
            emplyee_interface = EmployeeInterface()
            emplyee_interface.EMPLOYEE_INTERFACE(Email)

        else:
            print("Wrong email or password. ")

