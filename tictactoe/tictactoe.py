# write your code here

#Functions
def show(field):
    # prints Playing field
    # no Return
    print("---------")
    print("| "+ field[0] + " "+ field[1] + " " + field[2] + " |")
    print("| "+ field[3] + " "+ field[4] + " " + field[5] + " |")
    print("| "+ field[6] + " "+ field[7] + " " + field[8] + " |")
    print("---------")

def analyze(field):
    # analyzes field
    # prints Errors, Winners, Draws
    # Returns BOOL (Game still running)
    count_x = 0
    count_o = 0
    count_spc = 0
    x3 = 0
    o3 = 0

    for i in range(3):
        #vertical
        chk = field[i] + field[i + 3] + field[i + 6]
        if chk == "XXX":
           x3 += 1
        if chk == "OOO":
           o3 += 1

        #horizontal
        chk = field[3 * i] + field[3 * i + 1] + field[3 * i + 2]
        if chk == "XXX":
            x3 += 1
        if chk == "OOO":
            o3 += 1

        #counting
        for j in range(3):
             if field[i * 3 + j] == "X":
                 count_x += 1
             elif field[i * 3 + j] == "O":
                 count_o += 1
             else:
                 count_spc += 1

        # diagonally
        chk = field[0] + field[4] + field[8]
        if chk == "XXX":
                x3 += 1
        if chk == "OOO":
                o3 += 1

        chk = field[2] + field[4] + field[6]
        if chk == "XXX":
                x3 += 1
        if chk == "OOO":
                o3 += 1

    if not -1 <= count_x - count_o <= 1:
        print("Impossible")
    elif x3 > 0 and o3 > 0:
        print("Impossible")
    elif x3 == 0 and o3 == 0 and count_spc > 0:
        #print("Game not finished")
        #print("Space:",count_spc)
        return(True)
    elif x3 > 0:
        print("X wins")
    elif o3 > 0:
        print("O wins")
        return(False)
    elif x3 == 0 and o3 == 0 and count_spc == 0:
        print("Draw")
    else:
        print("Impossible")
    return(False)

def player_move(field, player):
    # get board and "X" or "O"
    # prints Error if invalid input
    # returns board after entering players move
    while True:
        move = input("Enter the coordinates:").split()
        # Error checking
        if len(move) != 2:       # Exactly 2 Coordinates
            print("You should enter numbers!")
        elif move[0] not in numbers or move[1] not in numbers:  #Coordinates are numbers?
            print("You should enter numbers!")
        elif not 0 < int(move[0]) < 4 or not 0 < int(move[1]) < 4:  # Coordinates in range?
            print("Coordinates should be from 1 to 3!")
        else:
            y = 3 - int(move[1])
            x = int(move[0]) - 1
            cell = y*3+x
            # print(y, x, cell)

            if field[cell] == "X" or field[cell] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                field[cell] = player
                return(field)


# Main
#Initialize

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
board = [cell for cell in "         "]
game_running = True
show(board)
player = "X"


#Game Loop
while game_running:
    board = player_move(board, player)
    show(board)
    game_running = analyze(board)
    if player == "X":
        player = "O"
    else:
        player = "X"
