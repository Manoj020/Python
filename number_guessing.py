import random

random_number = random.randint(1,100)
while True:
    try:
        number = int(input("Guess a number Between 1 and 100: "))

        if number > random_number:
            print("Too High")
        elif number < random_number:
            print("Too Low")
        else:
            print("You Guessed It")
            break
    except ValueError:
        print("Please Enter a Number")
    
