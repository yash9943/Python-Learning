import random

n = random.randint(1,100)
a = -1
gusses = 0

while(a != n):
    gusses += 1
    a = int(input("Guess The Number : "))
    if(a>n):
        print("Lower number please.")
    else:
        print("Higher number please.")
        
print(f"You guessed the number {n} in {gusses} attempts.")