from tictac import TicGame



print("\n wellcome to the tic tac toe game \n".capitalize())
game = TicGame()
game_is_on = True

while game_is_on:
    user_row = int(input('enter a row number (1-3): ')) -1
    user_col = int(input('enter a col number (1-3): ')) -1
    if user_col > 3 or user_row > 3:
        print("\nplease enter a valid number (1,  3)")
    else:
        if game.user_move(user_index=(user_row, user_col)):
            game.computer_move()
            game.desplay()
            check = game.check_winner()
            if check:
                game_is_on = False
            elif check == False and len(game.spots_left) == 0:
                print("it's a draw please play the game again!")
        else:
            print("please enter a valid untaken index for ur Next move: ")
            continue