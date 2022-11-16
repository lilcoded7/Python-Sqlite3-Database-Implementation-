# importing time and date
from datetime import datetime 
# importing database 
from database import Database
# importing random
import random 




class Employees:
    

    #   REGISTER METHOD
    def register(self):
        firstname = input('Enter name: ')
        email     = input('email: ')
        password  = input('password: ')
        date      = datetime.now()

        # saving details to database 
        items    = (1,firstname,email,password,date)
        database = Database()
        database.insert(items)

    #   DISPLAY DETAILS METHOD
    def displaydatabase(self):
        employee = Database() # fetching form detabase 
        details  = employee.read()
        for name in details:
            print(name)

    #   DISPLAY EMPLOYEE USERNAME
    def get_username(self):
        employees = Database() 
        username  = employees.read() 
        for names in username: # getting employees name
            print(names[0])

    #   UPDATE DABSE METHOD
    def update(self):
        employee = Database()
        email    = input('Enter username: ')
        id       = input('enter id: ')
        employee.update(email,id)

   
        
        




employees = Employees()
employees.register()
employees.displaydatabase()
print('=====================================================')
employees.get_username()
userIput = input('press 1.update detail: ')
if userIput == '1':
    employees.update()
