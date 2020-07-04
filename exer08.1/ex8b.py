
    ###########################################################
    #  Exercise #8B
    #
    #     Use the Deck and Card classes to play War
    #
    ###########################################################
 
# imports
import cards

# constants


# Create the deck of cards
the_deck = cards.Deck()
the_deck.shuffle()


def deal_cards(to_deal):
    '''
    Deals 26 cards to each player and displays hands to terminal
    
    Parameters
    ----------
    to_deal : int
        Number of cards to deal to each player
        
    Returns
    -------
    player1_cards : list
        List of cards in player 1's hand
        
    player2_cards : list
        List of cards in player 2's hand

    '''
    the_deck.shuffle()
  
    # Deal 26 cards to each player (alternating)
    player1_cards = []
    player2_cards = []
    for i in range(to_deal):
        player1_cards.append(the_deck.deal())
        player2_cards.append(the_deck.deal())

    # Display initial cards
    print("===== Beginning cards =====")
    print("")
    print("Player 1: ", player1_cards)
    print("")
    print("Player 2: ", player2_cards)

    return player1_cards, player2_cards


def war_round(player1_cards, player2_cards):
    '''
    Goes through a round of war. Displays results to user and updates hands

    Parameters
    ----------
    player1_cards : list
        List of cards in player 1's hand
    player2_cards : list
        List of cards in player 2's hand

    Returns
    -------
    None.

    '''
    
    # Gets top card from each deck and sets up variables for winning
    top_deck1 = player1_cards.pop(0)
    top_deck2 = player2_cards.pop(0)
    winner = ""

    # Battle display: Shows "Battle" and drawn cards
    print("""

                          -----------------
                               Battle
                          -----------------
          """)

    print("Player 1: ", top_deck1)
    print("Player 2: ", top_deck2)

    # Processing for battle
    # Handles cases for Ace on either player's side
    if top_deck1.rank() == 1 and top_deck2.rank() != 1:
        player1_cards.extend([top_deck1, top_deck2])
        winner = "Player 1"

    elif top_deck1.rank() != 1 and top_deck2.rank() == 1:
        player2_cards.extend([top_deck2, top_deck1])
        winner = "Player 2"

    # Handles normal cases (cards drawn are not aces)
    elif top_deck1.rank() > top_deck2.rank():
        player1_cards.extend([top_deck1, top_deck2])
        winner = "Player 1"

    elif top_deck1.rank() < top_deck2.rank():
        player2_cards.extend([top_deck2, top_deck1])
        winner = "Player 2"

    else:
        player1_cards.append(top_deck1)
        player2_cards.append(top_deck2)

    # Determines what to say in the results string
    if player1_cards == [] or player2_cards == []:
        won = "game!"
    else:
        won = "battle!"
        
    # Prints results of game/battle and hands
    if winner != "":
        print("{:^80}".format(winner + " wins the " + won))
    else:
        print("{:^80}".format("It's a tie!"))
    print()
    print("Player 1 hand: ", player1_cards)
    print()
    print("Player 2 hand: ", player2_cards)
        
          
def main():
    
    # Deal cards, enter number of cards to deal
    player1_cards, player2_cards = deal_cards(26)
    
    # Game loop
    end = None
    while not end:
        war_round(player1_cards, player2_cards)
        
        # User decision to continue or stop
        if player1_cards != [] and player2_cards != []:
            end = input("End game (Press Enter to continue)? ")
        else:
            break
        

if __name__ == "__main__":
    main()
    