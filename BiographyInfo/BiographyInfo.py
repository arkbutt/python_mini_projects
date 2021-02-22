import re

name =raw_input("Enter Your Name:")
# dob =raw_input("Enter Your DOB:")
# address =raw_input("Enter Your Address:")
# goals =raw_input("Enter Your Personal Goals:")



class Validator:
    def name_valid(self,user_input):
        pattern="^[a-zA-Z]([a-zA-Z]| )*$"
        if(re.findall(pattern,user_input)):
            return True
        else:
            return False


v=Validator()

print("Name: " + str(v.name_valid(name)))
# print("Date of birth: " + dob)
# print("Address: " + address)
# print("Personal Goal: " + goals)