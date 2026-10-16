#Game guess number from 1 to 100
def guess_number():
    import random
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == 0:
                    print("Game stopped.")
                    break
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")

#If input number = 0 you will stop the game
        if guess == 0:
            print("Game stopped.")
            break


guess_number()