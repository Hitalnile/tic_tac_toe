import tic_tac.win
import tic_tac.conditions
import tic_tac.board


def player_input():
    player1 = input("Please pick a marker 'X' or 'O' : ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Please pick a marker 'X' or 'O' ")

def player_choice(board):
	choice = input("Please select an empty space between 1 and 9 : ")
	while not tic_tac.conditions.space_check(board, int(choice)):
		choice = input("This space isn't free. Please choose again between 1 and 9 : ")
	return choice

def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    i = 1
    # Choose your side
    players=player_input()
    # Empty board init
    board = ['#'] * 10
    while True:
        # Set the game up here
        game_on=tic_tac.conditions.full_board_check(board)
        while not game_on:
            # Player to choose where to put the mark
            position = player_choice(board)
            # Who's playin ?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play !
            tic_tac.conditions.place_marker(board, marker, int(position))
            # Check the board
            tic_tac.board.display_board(board)
            i += 1
            if tic_tac.win.win_check(board, marker):
                print(marker ,' : whoooh you won!!!')
                break
            game_on=tic_tac.conditions.full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # Choose your side
            players=player_input()
            # Empty board init
board = ['#'] * 10
