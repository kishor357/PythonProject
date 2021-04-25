from Employee_signUp import Employee
from User_signUp import User
from Employee_login import Login_Employee
from User_login import Login_User


print("Enter your choice. ")
print("1 to signup as employee. ")
print("2 to signup as user. ")
print("3 to login as employee. ")
print("4 to login as user. ")
choice = int(input("Enter the choice. "))

if(choice==1):
    employee = Employee()
    employee.EMPLOYEE_SIGNUP()
elif(choice==2):
    user = User()
    user.USER_SIGNUP()
elif(choice==3):
    login_employee = Login_Employee()
    login_employee.LOGIN_EMPLOYEE()
elif(choice==4):
    login_user = Login_User()
    login_user.LOGIN_USER()
else:
    print("Enter 1 or 2 or 3 or 4 only. ")




