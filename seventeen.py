#!/usr/bin/env python3
# seventeen.py

##############################################################################
# Imports


# Body
def computer_turn(m_remain, last_turn):
    ''' Returns # removed by computer. '''
    c_remove = last_turn + 1

    return c_remove

def player_turn(marbles_remain):
    ''' Returns # removed by player.
        Handles input errors.'''
    p_remove = int(input('How Many Marbles will you remove (1-3)?'))

    return p_remove

def seventeen(playlist=[]):
    '''Game Loop. Takes a play argument for v2'''

    # Variables
    marbles_remain = 17
    last_turn = 16 # TEST.
    player_last = False
    msg = "Let's play the game of Seventeen!"

    # main loop condition
    print(msg)
    while marbles_remain > 17:

        # Call player_turn
        if player_last == False:
            print('Your turn:', end=' ')
            p_remove = player_turn(marbles_remain)

            print(p_remove)
            break

            # Update game state
            marbles_removed = marbles_removed - p_remove
            last_turn = p_remove
            player_last = True

        # Call computer_turn
        else:
            print("Computer's turn...")
            c_remove = computer_turn(marbles_remain, last_turn)
            print("Computer removed {} marbles.".format(c_remove))

            # Update game state
            marbles_removed = marbles_removed - c_remove
            last_turn = c_remove
            player_last = False

            # Print remaining marbles
            print("Number of marbles left in jar: {}".format(marbles_remain))
            print('')

    # Game Over, determine winner
    winner = ''
    if player_last == True:
        winner = 'Computer'
    else:
        winner = 'Player'

    # Print message and exit
    msg = "There are no marbles left. {} wins!".format(winner)
    print(msg)
##############################################################################
def main():
    seventeen()

if __name__ == '__main__':
    main()
