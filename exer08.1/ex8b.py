
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


def deal_cards():
    '''
    Deals 26 cards to each player and displays hands to terminal

    Returns
    -------
    player1_cards : list
        List of cards in player 1's hand
        
    player2_cards : list
        List of cards in player 2's hand

    '''
    the_deck.shuffle()
    
    
    # Deal 26 cards to each player (alternating)
    player1_cards=[]
    player2_cards=[]
    for i in range(5):
        player1_cards.append(the_deck.deal())
        player2_cards.append(the_deck.deal())
    
    # Display initial cards
    print( "===== Beginning cards =====" )
    print("")
    print("Player 1: ", player1_cards)
    print("")
    print("Player 2: ", player2_cards)
    
    
    return player1_cards, player2_cards



def war(player1_cards, player2_cards):
    '''
    Goes through the entire game of war 

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
    end = None
    
    while not end: 
        
        # Gets top card from each deck and sets up variables for winning
        top_deck1 = player1_cards.pop(0)
        top_deck2 = player2_cards.pop(0)
        one_winnings = [top_deck1, top_deck2]
        two_winnings = [top_deck2, top_deck1]
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
            player1_cards.extend(one_winnings)
            winner = "Player 1"
            
        elif top_deck1.rank() != 1 and top_deck2.rank() == 1: 
            player2_cards.extend(two_winnings)
            winner = "Player 2"
        
        # Handles normal cases (cards drawn are not aces)
        elif top_deck1.rank() > top_deck2.rank():
            player1_cards.extend(one_winnings)
            winner = "Player 1"
            
        elif top_deck1.rank() < top_deck2.rank():
            player2_cards.extend(two_winnings)
            winner = "Player 2"
            
        else:
            player1_cards.append(top_deck1)
            player2_cards.append(top_deck2)
        
        
        # Determines if game is finished
        if player1_cards == []:
            end = "Yes"
            won = "game!"
        elif player2_cards == []:
            end = "Yes"
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
        
        
        
        # User decision to continue or stop
        end = input("Keep going (Anything other than return to stop)? ")
          



def main():
    player1_cards, player2_cards = deal_cards()
    war(player1_cards,player2_cards)
    
    
    
    

if __name__ == "__main__":
    main()

