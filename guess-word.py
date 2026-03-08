import random

# List of words to choose from
#select one name randomly from the list
#get user input and check if it is correct
#keep track of the number of attempts
#decide if the user wins or loses based on the number of attempts

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

selected_name = random.choice(names).lower()  # Convert to lowercase for easier comparison
guess_count = len(selected_name) + 3  # Allow a few extra attempts
guessed_list = ['-'] * len(selected_name)
current_guess = ''.join(guessed_list)
print(current_guess)

while guess_count > 0:
    guessed_char = input("Guess a character: ")

    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("You already guessed that character.")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                print("Correct guess!")
                print("Current guess: " + ''.join(guessed_list))

                if '-' not in guessed_list:
                    print("Congratulations! You've guessed the word!")
                    break

        else:
            guess_count -= 1
            print(f"Wrong guess. You have {guess_count} attempts left.")

    else:
        print("Please enter a valid character.")
