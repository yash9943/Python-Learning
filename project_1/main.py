import random

computer = random.choice([1,-1,0])
youstr = input("Enter Your choice : ")
youDict = {"s":1,"w":-1,"g":0}
revDict = {1: "Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"You chose : {revDict[you]} \n Computer chose : {revDict[computer]}")

if(computer == you):
    print("It's a Draw")
else:
    if(computer == 1 or you == -1):
        print("You lose")
    elif(computer == 1 or you == 0):
        print("You win")
    elif(computer == -1 or you == 1):
        print("You win")
    elif(computer == -1 or you == 0):
        print("You lose")
    elif(computer == 0 or you == -1):
        print("You win")
    elif(computer == 0 or you == 1):
        print("You lose")
    else:
        print("Something Went Wrong !")