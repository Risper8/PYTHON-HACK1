## Applying the conditional statements and functions to simulate an election using face cards 

import random           ## for generating random numbers and making random choices.

##  Defining a function main 
def main():
    print("Welcome to the Election Card Game!")
    
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("You are eligible to vote and play the Election Card Game!")
        play_game()
    else:
        print("Sorry, you are not eligible to vote and play this game. Come back when you're older!")
 
 ## Defining a function for playing the game
def play_game():
    while True:
        deck = generate_deck()
        user_hand = deal_cards(deck, 5) 
        computer_hand = deal_cards(deck, 5)  

        ## Computer plays its card
        computer_card = random.choice(computer_hand)
        computer_hand.remove(computer_card)
        
        print("Computer plays:", computer_card)

        ## Showing the user their deck of cards
        print("Your hand:", user_hand)
        print("Let's see if you can win the election!")

        ## User plays their card
        while True:
            user_card_input = input("Choose a card from your hand to play (e.g., '10 Spades'): ").strip()
            user_rank, user_suit = user_card_input.split()
            user_card = (user_rank, user_suit)

            if user_card in user_hand:
                user_hand.remove(user_card)
                break
            else:
                print("Invalid card. Please choose a card from your hand.")

        # Simulate the election
        simulate_election(user_card, computer_card)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


##  Defining a function to generate deck for the players 
def generate_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

def simulate_election(user_card, computer_card):
    user_rank = user_rank = user_card[0]
    computer_rank = computer_card[0]

    # Define rank order for comparison
    rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

   
    
    # Get index of ranks in the rank order
    user_rank_index = rank_order.index(user_rank)
    computer_rank_index = rank_order.index(computer_rank)

    # Compare ranks to determine the winner
    if user_rank_index > computer_rank_index:
        print("Congratulations! You won the election!")
    elif user_rank_index < computer_rank_index:
        print("Sorry, you lost the election. Better luck next time!")
    else:
        print("It's a draw!")      

if __name__ == "__main__":  ## checks if the script is the main program being executed.
    main()                   ##  calls the function   

