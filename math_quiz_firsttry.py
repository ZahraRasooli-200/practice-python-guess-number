import random
import time
list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_functions = ['+', '-', '*', '/']   
a = random.choice(list_numbers)
b = random.choice(list_numbers)
function = random.choice(list_functions)

if function == '+':
    print(f"What is {a} + {b}?")
    c = int(input("Your answer: "))
    answer = a + b
elif function == '-':
    print(f"What is {a} - {b}?")
    c = int(input("Your answer: "))
    answer = a - b
    print(f"What is {a} - {b}?")
elif function == '*':
    print(f"What is {a} * {b}?")    
    c = int(input("Your answer: "))
    answer = a * b
elif function == '/':
    print(f"What is {a} / {b}?")
    c = int(input("Your answer: "))
    answer = a / b
else:
    print("Invalid function.")

chance = 10
while  chance > 0:
    score = 0

    if c == answer:
        print("Correct!")   
        score += 1
        print(f"Your score is: {score}")
        chance -= 1
        print(f"You have {chance} chances left.")
    else:
        print(f"Wrong! The correct answer is {answer}.")
        print(f"Your score is: {score}")
        chance -= 1
        print(f"You have {chance} chances left.")

    
    
if chance == 0 and score == 10:
    print("Congratulations! You won the game!") 
else:
    print("Game over! Better luck next time.")