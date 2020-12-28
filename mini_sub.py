import random
def addition():
    val1 = random.randint(5,20)
    val2 = random.randint(5,20)
    print(val1 , " + ", val2 ," =")
    user_answer= int(input("enter the answer"))
    correct= val1+val2
    answers=(user_answer,correct)
    return answers


def subm():
    val1 = random.randint(25,50)
    val2 = random.randint(1,25)
    print(val1 , " - ", val2 ," =")
    user_answer = int(input("Enter the user answer"))
    correct= val1-val2
    answers = (user_answer,correct)
    return answers
def check(add=False,sub=False):
    if add==True:
        user_answer, correct=addition()
        if user_answer ==  correct:
            print("Correct")
        else:
            print("Incorrect")
            print("The correct answer is ", correct)
    if sub==True:
        user_answer, correct=subm()
        if user_answer ==  correct:
            print("Correct")
        else:
            print("Incorrect")
            print("The correct answer is ", correct)
def main():
    add= False
    sub= False
    coices= int(input("Enter 1 to add, 2 to sub, enter only one of them please "))
    if coices ==  1:
        add=True
        sub= False
        check(add,sub)
    elif coices == 2:
        add=False
        sub= True
        check(add,sub)
main()



