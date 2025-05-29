import random

def game():
    comp = random.randint(1, 10)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    guesses = 0
    while True:
        try:
            user = int(input("Guess the number: "))
        except:
            print("Please enter a valid integer.")
            continue

        guesses += 1

        if user < comp:
            print("Too low! Try a higher number.")
        elif user > comp:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {guesses} tries.")
            break

game()