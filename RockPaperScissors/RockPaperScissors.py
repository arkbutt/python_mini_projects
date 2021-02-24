import random

coll=["rock", "paper", "scissor"]
comp= coll[random.randint(0,2)]
def r_p_c(user_input):
    if user_input:
        if user_input== coll[0] and comp== coll[1]:
            return "You Win"
        elif user_input == coll[0] and comp== coll[2]:
            return "You Win"
        elif user_input == coll[1] and comp== coll[0]:
            return "You Lose"
        elif user_input == coll[1] and comp== coll[2]:
            return "You Lose"
        elif user_input == coll[2] and comp== coll[0]:
            return "You Lose"
        elif user_input == coll[2] and comp== coll[1]:
            return "You win"
        else:
            return "Draw"  
    else:
        return "Invalid Input"  

user_input=input("Select rock, paper or scissor:\n0:{}\n1:{}\n2:{} \n".format(coll[0],coll[1], coll[2]))
print("Result: {}".format(r_p_c(user_input)))
print("Computer selected: {}".format(comp))