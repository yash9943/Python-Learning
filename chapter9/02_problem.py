import random;

def game():
    print("You are playing the game...")
    score = random.randint(1,100)
    
    # fetch the score
    with open ("hiscore.txt") as f:
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Your score is {score}")
    if(score>hiscore):
        with open ("hiscore.txt", "w") as f:
            f.write(str(score))
    return score

# game()   