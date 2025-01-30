'''
rock = -1
paper = 0
scissor = 1
'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"R": -1, "P": 0, "S": 1}
reverseDict = {-1: "Rock", 0: "Paper", 1: "Scissor"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# if(computer == you):
#     print("Its a draw")
# else:
#     if(computer == -1 and you == 0): #-1
#         print("You Win!")
#     elif(computer == 1 and you == -1): #2
#         print("You Win!")
#     elif(computer == 0 and you == 1): #-1
#         print("You Win!")
#     elif((computer == 0 and you == -1)): #1
#         print("You Lose!")
#     elif((computer == -1 and you == 1)): #-2
#         print("You Lose!")
#     elif((computer == 1 and you == 0)): #1
#         print("You Lose!")
if(computer == you):
     print("Its a draw")
else:
    if((computer - you == -1) or (computer - you == 2)):
        print("Yeeeeee!!! You Won!")
    elif (computer - you == 1 or computer - you == -2):
        print("Boooooo!? You Lose!")
    else:
        print("Something is wrong")