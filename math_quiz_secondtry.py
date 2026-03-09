import random
import time 
def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    operation = random.choice(['+', '-', '*', '/'])

    print(f"What is {a} {operation} {b}?")

    if operation == '+':
        return a + b    
    elif operation == '-':
        return a - b    
    elif operation == '*':
        return a * b    
    else:
        return a / b    

question_number_limit = 10
question_number = 0
score = 0
time_limit = 10  # seconds

while question_number < question_number_limit:
    result = str(generate_question())
    start_time = time.time()
    user_answer = input("Your answer: ")
    end_time = time.time()
    time_difference = end_time - start_time
    if time_difference > time_limit:
        print("Time's up! You took too long to answer.")
    else:
        if user_answer == result:
            score += 1
            print(f"Correct! your score is: {score}")
        else:
            print(f"Wrong! The correct answer is {result}")
    question_number += 1

print(f"Game over! Your final score is: {score} out of {question_number_limit}.")