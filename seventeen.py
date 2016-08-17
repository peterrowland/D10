#!/usr/bin/env python3
# seventeen.py

##############################################################################
# Imports


# Body
def computer_turn(m_remain, last_turn):
    ''' Returns # removed by computer.'''

    # Strategy Logic
    c_remove = min((last_turn + 1), 3)

    # Check to take all the marbles
    last_check = check_remain(m_remain, c_remove)

    if last_check == False:
        c_remove = m_remain

    return c_remove

def player_turn(m_remain):
    ''' Returns # removed by player.
        Handles input errors.'''
    p_remove = ''

    while p_remove == '':
        # Checking input
        try:
            p_remove = int(input('How Many Marbles will you remove (1-3)?'))
        except:
            print('Please enter only integers')
            p_remove = ''

        # Check number is valid or return to input
        if bool(check_remain(m_remain, p_remove)):
            return p_remove
        else:
            print('Number out of range (1-3) or greater than remaining marbles.')
            p_remove = ''


        # Checking p_remove in range and not > m_remain
        # assert p_remove in range(1,3) and (p_remove < m_remain)
        # AssertionError: "Number out of range or greater than remaining marbles."
        # Branch: Seventeen assert errors

    return p_remove

def check_remain(m_remain, remove):
    '''Simple function for both turn functions to use.'''
    in_range = bool(remove in range(1,4))
    not_negative = bool(remove <= m_remain)
    return (in_range and not_negative)

def seventeen(playlist=[]):
    '''Game Loop. Takes a play argument for v2'''

    # Variables
    marbles_remain = 17
    last_turn = 0
    player_last = False
    msg = "Let's play the game of Seventeen!"

    # main loop condition
    print(msg)
    while marbles_remain > 0:

        # Call player_turn
        if player_last == False:

            # Get player input
            print('Your turn:', end=' ')
            p_remove = player_turn(marbles_remain)
            print("You removed {} marbles.".format(p_remove))

            # Update game state
            marbles_remain = marbles_remain - p_remove
            last_turn = p_remove
            player_last = True

            # Print remaining marbles, next turn
            print("Number of marbles left in jar: {}".format(marbles_remain))
            print('')

        # Call computer_turn
        else:
            print("Computer's turn...")
            c_remove = computer_turn(marbles_remain, last_turn)
            print("Computer removed {} marbles.".format(c_remove))

            # Update game state
            marbles_remain = marbles_remain - c_remove
            last_turn = c_remove
            player_last = False

            # Print remaining marbles, next turn
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
    # seventeen()



##############################################################################
    # TESTS
    # print(player_turn(17))  # TEST1: OK
    # print(player_turn(5))  # TEST2: OK
    # print(computer_turn(1, 2)) # == 1, OK
    # print(computer_turn(5, 3)) # == 3, OK
    # print(computer_turn(2,3)) # == 2, OK

    seventeen()

if __name__ == '__main__':
    main()
