import random
def pick_low_high_random():
    low = int(input("Choose a lower number please "))
    high = int(input("Choose a high number please "))
    comp_num = random.randint(low,high)
    print(comp_num)
    return comp_num
def pick_num():
    num= int(input("I am thinking of a number…"))
    return num
def main():
    random = pick_low_high_random()
    num = pick_num()
    again = True
    while again:

        if num == random:
            print("Correct you win!")
            again= False
        elif num > random:
            print("You are too high")
            num = pick_num()

        elif num < random:
            print("You are too low")
            num = pick_num()
main()