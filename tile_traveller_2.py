'''Add the following functionality to tiles (1,2), (2,2), (2,3) and (3,2):

When the player enters these tiles offer them the choice to pull a lever.  
If they choose to pull the lever (answering either with ‘y’ or ‘Y’/ ‘N’ or ‘n’), 
they are to be told that they received one coin.

There is no limit on how often the player can get a coin from each lever.
 But they should only be presented with the option to pull a lever once each time they are in a particular room. 
 So if they want to be asked again, they must first go away (to another tile) and come back. 
 Picking an invalid direction (walking into a wall) does not count as leaving the room.

In addition, you need to keep track of the number of coins the player has and display that before showing the 
available actions.

When a victory has been reached, the program also prints out how many coins the player retrieved.'''




def lever_spot(col, row, coin, no_direction):
    if no_direction != False:
        if col == 1 and row == 2:
            lever = (input("Pull a lever (y/n): ").lower())
            if lever == 'y':
                coin += 1
                print ("You received 1 coin, your total is now "+str(coin)+".")
        elif col == 2 and row == 2:
            lever = (input("Pull a lever (y/n): ").lower())
            if lever == 'y':
                coin += 1
                print ("You received 1 coin, your total is now "+str(coin)+".")
        elif col == 2 and row == 3:
            lever = (input("Pull a lever (y/n): ").lower())
            if lever == 'y':
                coin += 1
                print ("You received 1 coin, your total is now "+str(coin)+".")
        elif col == 3 and row == 2:
            lever = (input("Pull a lever (y/n): ").lower())
            if lever == 'y':
                coin += 1
                print ("You received 1 coin, your total is now "+str(coin)+".")
    else:
        pass
    return coin
    
    

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'



def main():
    # The main program starts here
    victory = False
    row = 1
    col = 1
    coin = 0
    no_direction = True
    while not victory:
        valid_directions = find_directions(col, row)
        coin = lever_spot(col, row, coin, no_direction)
        print_directions(valid_directions)
        victory, col, row, no_direction = play_one_move(col, row, valid_directions, no_direction)

    print("Victory! Total coins "+str(coin)+".")

        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions


def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")


def play_one_move(col, row, valid_directions, no_direction):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    no_direction = True
    
    if not direction in valid_directions:
        print("Not a valid direction!")
        no_direction = False
        return victory, col, row, no_direction

    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row, no_direction


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)


def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)


if __name__ == "__main__":
    main()