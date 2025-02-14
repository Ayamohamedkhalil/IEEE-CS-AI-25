import random

low = 1
high = 100
num_guesses = 0
max_tries = 5
number = random.randint(low, high)

print(f"Guess the number between {low} and {high}. You have {max_tries} tries.")

while num_guesses < max_tries:
    guess_num = input("Enter your number: ")
    
    if guess_num.isdigit():
        guess_num = int(guess_num)
        num_guesses += 1

        if guess_num < low or guess_num > high:
            print("Out of range! Try again.")
        elif guess_num > number:
            print("Too high! Try again.")
        elif guess_num < number:
            print("Too low! Try again.")
        else:
            print("IT IS THE CORRECT NUMBER! Congratulations!")
            break
    else:
        print(f"Invalid input! Please enter a number between {low} and {high}.")
    
    remaining_attempts = max_tries - num_guesses
    if remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts left.")
    
if num_guesses == max_tries and guess_num != number:
    print(f"Game over! The correct number was {number}.")
