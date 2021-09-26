


def tictac():


    game = [" " for x in range(0,9)]
    #Print game board
    def game_board():
        print()
        print("|{}|{}|{}|".format(game[0],game[1],game[2]).strip().lower())
        print("|{}|{}|{}|".format(game[3],game[4],game[5]).strip().lower())
        print("|{}|{}|{}|".format(game[6],game[7],game[8]).strip().lower())
        



    #Get player input and udpate the board

    def move(icon):
     if icon == "X":
        choice = int(input("Make your move player 1 from (1-9):").strip())

        if game[choice - 1] == " ":
            game[choice - 1 ] = "X"
        else :
            print("position is already take! select another one")

     elif icon == "O":
        choice = int(input("Make your move player 2 from (1-9):").strip())

        if game[choice - 1] == " ":
            game[choice - 1 ] = "O"
        else :
            print("position is already take! select another one")

    def victory(icon):
        if (game[0] ==icon and game[1] ==icon and game[2] ==icon) or \
           (game[3] ==icon and game[4] ==icon and game[5] ==icon) or \
           (game[6] ==icon and game[7] ==icon and game[8] ==icon) or \
           (game[0] ==icon and game[3] ==icon and game[6] ==icon) or \
           (game[1] ==icon and game[4] ==icon and game[7] ==icon) or \
           (game[2] ==icon and game[5] ==icon and game[8] ==icon) or \
           (game[0] ==icon and game[4] ==icon and game[8] ==icon) or \
           (game[2] ==icon and game[4] ==icon and game[6] ==icon):
            return True
        else:
            return False

    def draw(icon):       
        if  " " not in game:
          return True
        else:
          return False

    while True:
        print(game_board())
        move("X")
        if victory("X") == True:
            print(game_board())
            print("X Wins !")
            break
        elif draw("X") == True: 
            print(game_board())
            print("Its a Draw")
            break
        
       
        print(game_board())
        move("O")
        if victory("O") == True:
            print(game_board())
            print("O Wins !")
            break
        elif draw("O") == True: 
            print(game_board())
            print("Its a Draw")
            break
        
