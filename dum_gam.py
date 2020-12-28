"""
It's just a game for user to guess a number with conditions 
"""
import math
a = True
while a:
    try1= int(input("Enter a number to start the game "))
    if (try1*try1 > 0 and try1*try1< 6) and(( math.sqrt(try1)** (try1*try1) )== try1):
        print("You Win Congrats the num is {}".format(try1))
        a=False
        pl_again= input("If you wanna play again press Yes as Y and if you wanna go out press No as N ")
        if pl_again == "Y":
            a=True
        else:
            print("Good By")
    else:
        print("You failed this time Try again if you like")