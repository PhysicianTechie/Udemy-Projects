# tictacTOe game , sOlve it step by step

# step 1 - create the 3 by 3 bOard - basically create a functiOn there are many ways but easiest tO start with is take a indeX pOsitiOn and cOncatante it with single straigh dash

# step 1 -- first print the board
import random
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
print(display_board(test_board))

# step2 -get the player input


def player_input():
    marker = ""  # placeholder

    while marker != 'X' and marker != 'O':
        marker = input(" Player 1, Please choose either X or O : ").upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')
player1_marker , player2_marker = player_input()


print(player_input())



# step 3 -
def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, '$', 8)
#display_board(test_board)




# step 4 - run the win check condition

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
      # across the bottom
      (board[1] == mark and board[2] == mark and board[3] == mark) or
      # down the middle
      (board[7] == mark and board[4] == mark and board[1] == mark) or
      # down the middle
      (board[8] == mark and board[5] == mark and board[2] == mark) or
      # down the right side
      (board[9] == mark and board[6] == mark and board[3] == mark) or
      (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
      (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


display_board(test_board)
print(win_check(test_board, 'X'))

# step 5 - random func
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# step 6 -
def space_check(board, position):
    return board[position] == ""

    

# step 7 - full board check function
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# step 8 - ask for a next position and use it from step 6


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) : '))

    return position

# step 9ask player if they want to plya again?


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')







# step 10 -last part to use above function in logical way
print('welcome to the GAME!')

while True:
    # reset the board
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')



play_game = input("Are you ready to play ? enter yes or no.")

if play_game.lower()[0] == 'y':
    game_on = True
else:
    game_on = False




while game_on:
    if turn == 'Player 1':

        display_board(theBoard)
        position = player_choice(theBoard)
        place_marker(theBoard, player1_marker, position)

        if win_check(theBoard, player1_marker):
            display_board(theBoard)
            print('Congratulations! You have won the game!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break
            else:
                turn = 'Player 2'

    else:
        display_board(theBoard)
        position = player_choice(theBoard)
        place_marker(theBoard, player2_marker, position)

        if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
        else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

        if not replay():
            break
