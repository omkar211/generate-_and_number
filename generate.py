import random

def generate():
    gen=random.randint(1,15)
    user=int(raw_input("guess the right answer"))
    if user==gen:
        print("You got it")
    else:
        while user!=gen:
            print("try again")
            if user > gen:
                print("guess lower")
            elif user<gen:
                print("guess Higher")
            user=int(raw_input("guess right number"))
            if(user==gen):
                print("you got it!")
generate()