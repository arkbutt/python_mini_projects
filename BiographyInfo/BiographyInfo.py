import re
from typing import Pattern

name =raw_input("Enter Your Name:")
dob =raw_input("Enter Your DOB(DD/MM/YYYY):")
address =raw_input("Enter Your Address:")
goals =raw_input("Enter Your Personal Goals:")



class Validator:
    def name_valid(self,user_input):
        pattern="^[a-zA-Z]([a-zA-Z]| )*$"
        if(re.findall(pattern,user_input)):
            return user_input
        else:
            return "Invalid Syntax of Name"

    def dob_valid(self, user_input):
        pattern= "^([0-2][1-9]|[1-2]0|3[0-1]|[1-9])[\s\-\/]((1[0-2]|[1-9]|0?[1-9]))[\s\-\/]([1-2][0-9]{3})$"
        if(re.findall(pattern,user_input)):
            return user_input
        else:
            return "Invalid Syntax of Date DD/MM//YYYY"
        return user_input

    def address_valid(self, user_input):
        pattern= "^[a-zA-Z0-9]([a-zA-Z0-9]| )*$"
        if(re.findall(pattern,user_input)):
            return user_input
        else:
            return "Invalid Syntax of Address (A-Z and 0-9)"
        return user_input

    def personal_goals_valid(self, user_input):
        pattern= "^[a-zA-Z0-9]([a-zA-Z0-9]| )*$"
        if(re.findall(pattern,user_input)):
            return user_input
        else:
            return "Invalid Syntax of goals (A-Z and 0-9)"
        return user_input

v=Validator()

print("Name: " + str(v.name_valid(name)))
print("Date of birth: " + str(v.dob_valid(dob)))
print("Address: " + str(v.address_valid(address)))
print("Personal Goals: " + goals)