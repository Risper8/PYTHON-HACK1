import random  ## for generating random numbers, shuffling sequences, and making random choices.

def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

## Defining a hint function to give hints to the user/player
def get_hint(number):
    num_digits = len(str(number))
    if num_digits == 1:
        return "It's a one-digit number."
    elif num_digits == 2:
        return f"It's a two-digit number and starts with {str(number)[0]} and ends with {str(number)[-1]}."
    else:
         return f"It's a three-digit number and starts with {str(number)[0]} and ends with {str(number)[-1]}."

## Defining a hint function to start a game
def play_game():
    print("Welcome to the Fibonacci Guessing Game!")
    print("I have a number in mind. Can you guess it?")

    number = random.randint(1, 1000)  # Generate a random number between 1 and 1000

## limiting the number of attempts
    attempts = 0
    while attempts < 5:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the magic number", number)
            print("It took you", attempts, "attempts to guess correctly.")
            return
        elif guess < number:
            print("Try a higher number.") ## input another number that is higher than the previous input
        else:
            print("Try a lower number.")  ## input another number that is lower than the previous input
        
        if attempts < 5:
            print("Hint:", get_hint(number))

    print("Sorry, you've used all your attempts.")
    print("The magic number was:", number)


# start the game
play_game() 