import cards

import random
random.seed(90)

def setup():
    """
    paramaters: None (deck can be created within this function)
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 8 lists, the dealt cards)
    """
    game_deck = cards.Deck()
    game_deck.shuffle()
    
    # Initialize tableau and create foundation and cell
    tableau = [[],[],[],[],[],[],[],[]]
    foundation = [[],[],[],[]]
    cell = [[], [], [], []]
    
    # Creating the tableau
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
    move_card = move_from[stack].pop()
    
    # Handles if foundation is empty, triggers if card is an Ace (rank = 1)
    if move_card.rank() == 1 and foundation[f_col] == []:
        valid_move = True
        foundation[f_col].append(move_card)
        
    # Otherwise, if foundation is not empty
    else:
        # Get the top card in the foundation
        foundation_card = foundation[f_col][-1]
        
        # If the card desired is of one greater rank and is the same suit, move
        if move_card.rank() == foundation_card.rank() + 1 and move_card.suit() == foundation_card.suit():
            valid_move = True
            foundation[f_col].append(move_card)
            
        # Otherwise, put back into the tableau/cell
        else:
            move_from[stack].append(move_card)
    
    return valid_move


def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    valid_move = False
    
    # Allow the move if the cell is empty. Append to appropriate cell list
    if cell[c_col] == []:
        valid_move = True
        cell[c_col].append(tableau[t_col].pop())
        
    
    return valid_move

def move_to_tableau(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    valid_move = False
    
    # Checks if there is a card in the cell
    if cell[c_col] != []:
        
        # If the tableau column isn't empty, 
        if tableau[t_col] != []:
            cell_card = cell[c_col][-1]
            tableau_card = tableau[t_col][-1]
            
            # Check to see if the cell card is one less than the tableau card
            # And if so, add it to the tableau column
            if cell_card.rank() == tableau_card.rank() - 1:
                valid_move = True
                tableau[t_col].append(cell[c_col].pop())
                
        # If the tableau is empty, just add the card     
        else:
            valid_move = True
            tableau[t_col].append(cell[c_col].pop())
    
    return valid_move
        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    pass


def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    pass
        

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
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        if len(response_list) > 0:
            r = response_list[0]
            param_A = int(response_list[1]) - 1
            param_B = int(response_list[2]) - 1
            if r == 't2f':
                if param_A in range(len(tableau)) and param_B in range(len(foundation)):
                    valid = move_to_foundation(tableau, foundation, param_A, param_B)
                else:
                    print("Invalid input!")
                    
                if valid == False:
                    print("Invalid move!")
            elif r == 't2t':
                pass # you implement                          
            elif r == 't2c':
                valid = move_to_cell(tableau, cell, param_A, param_B)  
                if valid == False:
                    print("Invalid move!")                     
            elif r == 'c2t':
                if param_A in range(len(cell)) and param_B in range(len(tableau)):
                    valid = move_to_tableau(tableau, cell, param_B, param_A)
                else:
                    print("Invalid input!")
                    
                if valid == False:
                    print("Invalid move!")                     
            elif r == 'c2f':
                if param_A in range(len(cell)) and param_B in range(len(foundation)):
                    valid = move_to_foundation(cell, foundation, param_A, param_B)
                else:
                    print("Invalid input!")

                if valid == False:
                    print("Invalid move!")                        
            elif r == 'q':
                break
            elif r == 'h':
                show_help()
            else:
                print('Unknown command:',r)
        else:
            print("Unknown Command:",response)
    print('Thanks for playing')

play()


        
    

