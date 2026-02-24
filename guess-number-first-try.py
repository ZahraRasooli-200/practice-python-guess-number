import random
a = eval(input("please enter the first number: "))
b = eval(input("and the second number:"))
n = random.randint(a, b)

chance = 0
while chance < 5:
    c = eval(input("please guess the number i choiced: "))
    chance += 1

    if c==n :
        print("good job your guess is true.")
        break
    elif c > n :
        print("the number is bigger")
    else:
        print("the number is smaller")
    if chance == 5 and c != n :
        print("you guess five times, sorry you could not guess correctly, the correct number is:", n)