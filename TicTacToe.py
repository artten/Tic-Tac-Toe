board = "     |   |     \n" \
        "     |   |     \n" \
        "_____|___|_____\n" \
        "     |   |     \n" \
        "     |   |     \n" \
        "_____|___|_____\n" \
        "     |   |     \n" \
        "     |   |     \n" \
        "     |   |     \n"

regular = "     |   |     \n"
spacial = "_____|___|_____\n"

# this is the row of each chosen number inside the board
locations = {"1": 2, "2": 7, "3": 12, "4": 2, "5": 7, "6": 12, "7": 2, "8": 7, "9": 12}

player_1 = "X"
player_2 = "0"


def edit_line(number, player, line):
    # editing the line by players moves
    change = locations[number]
    edit_regular = line[0:change]+player+line[change+1:]
    return edit_regular


def select_player_figure():
    # configure players Figures
    choosed = ''
    choosed = input("Player 1 will play with X or 0?")
    while choosed != 'X' and choosed != '0':
        choosed = input("Sorry incorrect\n"
                        f" you choosed {choosed}\n"
                       "please try again and remember only X or 0")
    return choosed



def print_board(x=[], o=[]):
    # drawing a board by the players moves
    for i in range(1, 9):
        if i == 3 or i == 6:
            print(spacial)

        elif i == 2:
            new_line = regular
            numpads = ["7", "8", "9"]
            for xlocation in x:
                if xlocation == numpads[0]:
                    new_line = edit_line(numpads[0], player_1, new_line)
                elif xlocation == numpads[1]:
                    new_line = edit_line(numpads[1], player_1, new_line)
                elif xlocation == numpads[2]:
                    new_line = edit_line(numpads[2], player_1, new_line)
            for xlocation in o:
                if xlocation == numpads[0]:
                    new_line = edit_line(numpads[0], player_2, new_line)
                elif xlocation == numpads[1]:
                    new_line = edit_line(numpads[1], player_2, new_line)
                elif xlocation == numpads[2]:
                    new_line = edit_line(numpads[2], player_2, new_line)
            print(new_line)

        elif i == 5:
            new_line = regular
            numpads = ["4", "5", "6"]
            for xlocation in x:
                if xlocation == numpads[0]:
                    new_line = edit_line(numpads[0], player_1, new_line)
                elif xlocation == numpads[1]:
                    new_line = edit_line(numpads[1], player_1, new_line)
                elif xlocation == numpads[2]:
                    new_line = edit_line(numpads[2], player_1, new_line)
            for xlocation in o:
                if xlocation == numpads[0]:
                    new_line = edit_line(numpads[0], player_2, new_line)
                elif xlocation == numpads[1]:
                    new_line = edit_line(numpads[1], player_2, new_line)
                elif xlocation == numpads[2]:
                    new_line = edit_line(numpads[2], player_2, new_line)
            print(new_line)

        elif i == 7:
            new_line = regular
            numpads = ["1", "2", "3"]
            for xlocation in x:
                if xlocation == numpads[0]:
                    new_line = edit_line(numpads[0], player_1, new_line)
                elif xlocation == numpads[1]:
                    new_line = edit_line(numpads[1], player_1, new_line)
                elif xlocation == numpads[2]:
                    new_line = edit_line(numpads[2], player_1, new_line)
            for xlocation in o:
                if xlocation == numpads[0]:
                    new_line = edit_line(numpads[0], player_2, new_line)
                elif xlocation == numpads[1]:
                    new_line = edit_line(numpads[1], player_2, new_line)
                elif xlocation == numpads[2]:
                    new_line = edit_line(numpads[2], player_2, new_line)
            print(new_line)

        else:
            print(regular)


def winner(moves_1, moves_2):
    # checking if someone is a winner
    print(moves_2)
    for i in moves_1:
        for l in range(1, 5):
            if str(int(i) - l) in moves_1 and str(int(i) + l) in moves_1:
                return "player 1"
    for i in moves_2:
        for l in range(1, 5):
            if str(int(i) - l) in moves_2 and str(int(i) + l) in moves_2:
                return "player 2"

    if len(moves_1) + len(moves_2) == 9:
        return "tie"

    return ""


player_1_moves = []
player_2_moves = []


def play():
    # the main loop
    global player_1
    global player_2
    player_1 = select_player_figure()
    if player_1 is "X":
        player_2 = "0"
    else:
        player_2 = "X"
    player_turn = 1
    while winner(player_1_moves,player_2_moves) != "player 1" \
           and winner(player_1_moves,player_2_moves) != "tie"\
            and winner(player_1_moves, player_2_moves) != "player 2":
        print_board(player_1_moves, player_2_moves)
        selected_number = input(f"Player number {player_turn} its your turn\n"
                                f"please select number between 1-9")

        while not (int(selected_number) in range(1, 10)) \
                or str(selected_number) in player_2_moves \
                or str(selected_number) in player_1_moves:
            selected_number = input(f"Sorry please try again\n"
                                    f"Player number {player_turn} its your turn\n"
                                    f"please select number between 1-9")

        if player_turn == 1:
            player_1_moves.append(str(selected_number))
            player_turn = 2
        else:
            player_2_moves.append(str(selected_number))
            player_turn = 1

    winnig_player = winner(player_1_moves, player_2_moves)
    if winnig_player != "tie":
        print(f"Congratulations {winnig_player} won")

    else:
        print("It's a tie")

# main
print("Welcome to my Tic Tac Toe")
play()

