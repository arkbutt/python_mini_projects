import random
import re
from typing import Pattern

coll=["rock", "paper", "scissor"]
comp= coll[random.randint(0,2)]

#Without condition
def play_rock_paper_scissor(c,p):
    y = (c+p)
    a = y&1
    return ((y>>a)+a)*a
    

def r_p_c(user_input):
    if user_input>=0 and user_input<=2:
        if coll[user_input]== coll[0] and comp == coll[1]:
            return "You Win"
        elif coll[user_input] == coll[0] and comp == coll[2]:
            return "You Win"
        elif coll[user_input] == coll[1] and comp == coll[0]:
            return "You Lose"
        elif coll[user_input] == coll[1] and comp == coll[2]:
            return "You Lose"
        elif coll[user_input] == coll[2] and comp == coll[0]:
            return "You Lose"
        elif coll[user_input] == coll[2] and comp == coll[1]:
            return "You win"
        else:
            return "Draw"  
    else:
        return "Invalid Input"
        
def validation(user_input):
    pattern="^[0-2]$"
    if(re.findall(pattern,user_input)):
        return user_input
    else:
        return "Invalid Syntax (0-2)"
    return user_input

user_input=input("Select rock, paper or scissor:\n0:{}\n1:{}\n2:{} \n".format(coll[0],coll[1], coll[2]))



# print(play_rock_paper_scissor(comp,user_input))
print("You selected: {}".format(validation(user_input)))
print("Computer selected: {}".format(comp))
print("Result: {}".format(r_p_c(user_input)))
