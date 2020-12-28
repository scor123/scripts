"""
Write a program that asks a user whether they want to play
a game. If the user enters y or yes, indicate that you’re
thinking of a number between 1 and 10 and ask the user to
guess the number. Your program should continue asking
the user to guess the number until they get it right. If they
get it right, print a congratulatory message and then ask if
they want to play again. This process should be repeated as
long as the user enters y or yes.
"""
guess= 10
play = True
while play:
    wan_pla=input("Enter y or yes if you wanna play").lower()
    while wan_pla == "y" or wan_pla == "yes":
        print("I'm thinking about num between 1 and 10 if you guessed it you wanna win")
        num = int(input("Guess a num"))
        while num != guess:
            print("That's Ok you can try again")
            num = int(input("Guess a num"))
        print("That's cool you are a winner")
        wan_pla = input("Enter y or yes if you wanna play again").lower()
        if wan_pla =="y" or wan_pla == "yes":
            play =True
            print("We wanna play again")
        else:
            play =False
            print("That's Ok if you don't wanna play right now!")
    print("That's Ok you can play later")

