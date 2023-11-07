# Hello here is the tic tac toe game bro

from board import draw_board, check_turn, check_win
import os

spots = {1: '1', 2: '2', 3: '3', 4: '4',
         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

playing = True

end = False
turn = 0
prev_turn = -1

while playing:
    # Clear screen after each execution
    os.system('cls')
    draw_board(spots)
    # Let the players know if an invalid spot has been selected
    if prev_turn == turn:
        print("You selected an invalid spot. Please pick another.")
    prev_turn = turn

    # Allowing player 1 and 2 to take turns in picking spots
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your sport of press q to quite. ")
    # Getting input from the players
    choice = input("Go on: ")
    if choice == "q":
        playing = False
        # Check if choice is a digit and is in spots dictionary
    elif str.isdigit(choice) and int(choice) in spots:
        # Check that both player don't override each other's choice
        if not spots[int(choice)] in {"o", "x"}:
            # Update the board if input is valid
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # Check if the game is ended and if there is a winner
    if check_win(spots):
        playing = False
        end = True
    if turn > 8:
        playing = False

# Print out the results of the game
os.system("cls")
draw_board(spots)
if end:
    if check_turn(turn) == "x":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
else:
    print("Its tie!")


