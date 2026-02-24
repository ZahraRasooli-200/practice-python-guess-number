import random

try:
    low = int(input("enter the low bound: \n"))
    high = int(input("enter the high bound: \n"))
except:
    print("please enter a valid number")

r = random.randint(low, high)
guess_count = 5

while guess_count > 0:
    try:
        guess_number = int(input(f"remaind guess: {guess_count}  please guess the number I choiced: "))

        if r==guess_number :
            print("great! your guess is correct.")
            break
        elif r > guess_number :
            print("your guess is lower than selected number")
        else:
            print("your guess is higher than selected number")

        guess_count -= 1

        if guess_count == 0 and guess_number != r :
            print("you guess five times, sorry you could not guess correctly, the correct number is:", guess_number)

    except:
        print("please enter a valid number.")

