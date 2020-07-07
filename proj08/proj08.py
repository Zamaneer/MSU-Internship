
    ###########################################################
    #  Project #8
    #
    #     A game of FreeCell using the Card and Deck classes
    #
    ###########################################################

# imports
import cards

# constants

def setup():
    """
    paramaters: None
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 8 lists, the dealt cards)
    """
    game_deck = cards.Deck()
    game_deck.shuffle()
    
    # Initialize tableau, foundation, and cell
    tableau = [[],[],[],[],[],[],[],[]]
    foundation = [[],[],[],[]]
    cell = [[],[],[],[]]
    
    # Create the tableau with eight columns, four of 7 cards, four of 6
    column = 0
    while not game_deck.is_empty():
        tableau[column].append(game_deck.deal())
        column += 1
        if column % 8 == 0: # Resets to column 0 after column 8
            column = 0
    
    return foundation,tableau,cell


def move_to_foundation(move_from,foundation,stack,f_col):
    '''
    parameters: move_from (a tableau or cell), a foundation, stack (column
    of tableau or card from cell), a foundation column
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    valid_move = False
    
    # Make sure that the card to be moved exists
    if move_from[stack] != []:
        move_card = move_from[stack][-1]
    else:
        return valid_move
    
    # If foundation is empty and the card is an Ace, put into foundation
    if foundation[f_col] == []: # Ace is rank 1
        if move_card.rank() == 1:
            valid_move = True
            foundation[f_col].append(move_from[stack].pop())
        
    # Otherwise, if foundation is not empty
    else:
        # Get the top card in the foundation
        foundation_card = foundation[f_col][-1]
        
        # If the card desired is of one greater rank and is the same suit, move
        if move_card.rank() == foundation_card.rank() + 1 and\
            move_card.suit() == foundation_card.suit():
            valid_move = True
            foundation[f_col].append(move_from[stack].pop())
            
        # Otherwise, put back into the tableau/cell
        else:
            move_from[stack].append(move_from[stack].pop())
    
    return valid_move


def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    valid_move = False
    
    # Allow the move if the cell is empty and tableau column is not empty. 
    # Append to appropriate cell list
    if cell[c_col] == [] and tableau[t_col] != []:
        valid_move = True
        cell[c_col].append(tableau[t_col].pop())
        
    
    return valid_move

def move_to_tableau(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    '''
    valid_move = False
    black = (1, 4) # Clubs and spades are black (Suits 1 and 4)
    red = (2, 3) # Diamonds and hearts are red (Suits 2 and 3)
    
    # If there is a card in the cell
    if cell[c_col] != []:
        
        # And if the tableau column isn't empty, 
        if tableau[t_col] != []:
            cell_card = cell[c_col][-1]
            tableau_card = tableau[t_col][-1]
            t_card_suit = tableau_card.suit()
            c_card_suit = cell_card.suit()
            
            # And the colors on the cards alternate
            if (t_card_suit in black and c_card_suit in red)\
                or (t_card_suit in red and c_card_suit in black):
                    
                # And the cell card is one less rank than the tableau card, move
                if cell_card.rank() == tableau_card.rank() - 1:
                    valid_move = True
                    tableau[t_col].append(cell[c_col].pop())
                
        # Otherwise, if the tableau is empty, just add the card     
        else:
            valid_move = True
            tableau[t_col].append(cell[c_col].pop())
    
    return valid_move
        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    determines if the player has won the game and gives encouraging messages
    '''
    suits_solved = 0
    
    # See how many suits are solved
    for column in foundation:
        if len(column) == 13:
            suits_solved += 1
        
    if suits_solved == 2:
        print("Halfway! Good work!")
    elif suits_solved == 3:
        print("Almost there! You're doing great!")
    elif suits_solved == 4: 
        print("You won!")
        return True # Break out of the loop and end game
    
    return False
    


def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    '''
    valid_move = False
    black = (1, 4) # Clubs and spades are black (Suits 1 and 4)
    red = (2, 3) # Diamonds and hearts are red (Suits 2 and 3)
    
    # If there is a card in the source column
    if tableau[t_col_source] != []:
        
        # And the destination column isn't empty, 
        if tableau[t_col_dest] != []:
            source_card = tableau[t_col_source][-1]
            dest_card = tableau[t_col_dest][-1]
            t_source_suit = source_card.suit()
            t_dest_suit = dest_card.suit()
            
            # And if the colors on the cards alternate
            if (t_source_suit in black and t_dest_suit in red)\
                or (t_source_suit in red and t_dest_suit in black):

                # And if the cell card is one less than the tableau card, move
                if source_card.rank() == dest_card.rank() - 1:
                    valid_move = True
                    tableau[t_col_dest].append(tableau[t_col_source].pop())
                
        # Otherwise, if the destination is empty, just add the card     
        else:
            valid_move = True
            tableau[t_col_dest].append(tableau[t_col_source].pop())
    
    return valid_move
        

def print_game(foundation, tableau,cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    print()
    print('{:^40}{:^40}'.format("Cells:", "Foundations:"))
    # print cell and foundation labels in one line
    print("      ", end = '')
    for i in range(4):
        print('{:^7d}'.format(i+1), end = '')
    print('            ', end = '')
    for i in range(4):
        print('{:^7d}'.format(i+1), end = '')
    print()  # carriage return at the end of the line

    print("       ", end = '')
    # print cell and foundation cards in one line; foundation is only top card
    for c in cell:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:^7s}'.format(str(c[0])), end = '')
        except IndexError:
            print('{:8s}'.format('  '), end = '')
            
    print('          ', end = '')
    for stack in foundation:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:<7s}'.format(str(stack[-1])), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')

    print()  # carriage return at the end of the line
    print('----------')

    print("Tableau")
    for i in range(len(tableau)):  # print tableau headers
        
        print('{:^10d}'.format((i + 1)), end = '')
    print()  # carriage return at the end of the line

    # Find the length of the longest stack
    max_length = max([len(stack) for stack in tableau])
    # print tableau stacks row by row
    for i in range(max_length):  # for each row
        for stack in tableau:
            # print if there is a card there; if not, exception prints spaces.
            try:
                print('{:^10s}'.format(str(stack[i])), end= '')
            except IndexError:
                print('{:10s}'.format('  '), end = '')
        print()  # carriage return at the end of the line
    print('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print("Rules of FreeCell")

    print("Goal")
    print("\tMove all the cards to the Foundations")

    print("Foundation")
    print("\tBuilt up by rank and by suit from Ace to King")

    print("Tableau")
    print("\tBuilt down by rank and by alternating color")
    print("\tThe bottom card of any column may be moved")
    print("\tAn empty spot may be filled with any card ")

    print("Cell")
    print("\tCan only contain 1 card")
    print("\tThe card may be moved")

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("Responses are: ")
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau column to another")
    print("\t t2c #T #C - move from Tableau to Cell")
    print("\t c2t #C #T - move from Cell to Tableau")
    print("\t c2f #C #F - move from Cell to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")
    
    
def play():
    ''' 
    Main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup() 
       
    show_help()
    while True:
        
        # Print display, get user input and split into parts
        print_game(foundation, tableau, cell)
        win = is_winner(foundation)
        if win == True: break  # Check to see if player is winner, breaks out of the loop
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        
        # Categorizing and error checking
        if len(response_list) > 0: # Finds the command 
            r = response_list[0]
            
            # Find additional fields if available and process into ints
            if len(response_list) == 3 and\
                response_list[1].isdigit() and response_list[2].isdigit(): 
                param_A = int(response_list[1]) - 1
                param_B = int(response_list[2]) - 1
                valid = True
                
            # Move: Tableau to foundation
            if r == 't2f':
                if param_A in range(len(tableau)) and param_B in range(len(foundation)):
                    valid = move_to_foundation(tableau, foundation, param_A, param_B)
                else:
                    print("Invalid input!")
                    
                if valid == False:
                    print("Invalid move!")
                    
            # Move: Tableau to tableau
            elif r == 't2t':
                if param_A in range(len(tableau)) and param_B in range(len(tableau)):
                    valid = move_in_tableau(tableau, param_A, param_B)
                else:
                    print("Invalid input!")
                    
                if valid == False:
                    print("Invalid move!")      
                    
            # Move: Tableau to cell
            elif r == 't2c':
                if param_A in range(len(tableau)) and param_B in range(len(cell)):
                    valid = move_to_cell(tableau, cell, param_A, param_B)
                else:
                    print("Invalid input!")
                    
                if valid == False:
                    print("Invalid move!")  
                    
            # Move: Cell to tableau
            elif r == 'c2t':
                if param_A in range(len(cell)) and param_B in range(len(tableau)):
                    valid = move_to_tableau(tableau, cell, param_B, param_A)
                else:
                    print("Invalid input!")
                    
                if valid == False:
                    print("Invalid move!")   
                    
            # Move: Cell to foundation
            elif r == 'c2f':
                if param_A in range(len(cell)) and param_B in range(len(foundation)):
                    valid = move_to_foundation(cell, foundation, param_A, param_B)
                else:
                    print("Invalid input!")

                if valid == False:
                    print("Invalid move!")      
                    
            # Quit game
            elif r == 'q':
                break
            
            # Show help menu
            elif r == 'h':
                show_help()
                
            # Bad input catcher if command is entered
            else:
                print('Unknown command:',r)
                
        # Bad input if nothing is entered
        else:
            print("Unknown Command:",response)

    print('Thanks for playing')




def main():
    play()


if __name__ == "__main__":
    main()
        
    