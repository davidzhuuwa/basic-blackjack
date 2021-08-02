############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

from art import logo
import random as rd 
print(logo)
game_state = True # Used to dictate if game is being played or not

def deal_card():
    card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return rd.choice(card_list)

def update_score(old_score,new_card,game_state):
    new_score = old_score + new_card
    if new_score > 21 and new_card == 11:
        new_card = 1
        new_score = old_score + new_card
    elif new_score > 21: 
        print('Bust! You lose this round!')
        game_state = False
    return new_score,new_card,game_state

user_cards = []
computer_cards = []
user_score = 0 
computer_score = 0
# Deal out two cards to user and computer
for i in range(0,2):
    new_card = deal_card() 
    user_score,new_card,game_state = update_score(user_score,new_card,game_state)
    user_cards.append(new_card)
    new_card = deal_card()
    computer_score,new_card,game_state = update_score(computer_score,new_card,game_state)
    computer_cards.append(new_card)
    i+=1

user_score = sum(user_cards)
computer_score = sum(computer_cards)

# Check if the computer has blackjack
if user_score == 21:
    print('The dealer has blackjack! You lose!')
elif computer_score == 21: 
    print('You have blackjack while the computer does not! You Win!')

# Simulating the user's turn first
user_turn = True
while user_turn:
    print(f'Your score: {user_score}.')
    print(f'Computer score: {computer_score}.')
    choice = input('Hit, or stand?: ').lower()

    if choice == 'hit':
        new_card = deal_card() 
        user_score_updated,new_card,game_state = update_score(user_score,new_card,game_state)
        user_cards.append(new_card)
    elif choice == 'stand':
        user_turn = False

    # Checking if user busted
    if not game_state:
        break

# Computer's turn now 
# The computer has to keep drawing until they hit 16. For the initial 
# version of this program, the computer will stop on soft 16, and not hard 16
# Soft 16 is when the computer has 16 or over with an ace.
while computer_score < 16:
    new_card = deal_card()
    computer_score_updated,new_card,game_state = update_score(computer_score,new_card,game_state)
    computer_cards.append(new_card)
    
    # Checking if computer busted
    if not game_state:
        break
print(f'The dealer has {computer_score} and you have {user_score}')
# Comparing computer score to user score now 
if computer_score == user_score:
    print('Push - the scores are equal')
elif computer_score > user_score:
    print('The dealer wins!')
else:
    print('You win!')








#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

