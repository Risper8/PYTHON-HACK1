## fibonacci_sequence: Each number is equal to the sum of the preceding two numbers

## defining the fibonacci_sequence function
def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

def main():
    print("Welcome to the Fibonacci Sequence Generator!")
    print("This program generates the Fibonacci sequence up to a specified term.")

    while True:
        try:
            n = int(input("Enter the number of terms in the Fibonacci sequence (0 to quit): "))
            if n == 0:
                print("Thank you for using the Fibonacci Sequence Generator. Goodbye!")
                break
            elif n < 0:
                print("Please enter a positive integer.")
                continue

            fibonacci_sequence = generate_fibonacci_sequence(n)
            print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
