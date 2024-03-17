## Basic Structure of the use case of conditional Statement

## Defining a function main 
def main():
    age = int(input("Please enter your age: "))

    if age < 0:                                       ## It prevents a user from entering a -ve number
        print("Invalid age. Age cannot be negative.")

    elif age >= 18:
        print(" You are eligible to vote")
    else:
        print("You are not eligible to vote.")


if __name__ == "__main__":           ## checks if the script is the main program being executed.
    main()                           ##  calls the function
