# ------------------------------a_Get Choice-----------------------------


def getchoice(a_c_list):
    # check if c_list entries are ok
    if a_c_list == []:
        return ""
    for a_i in a_c_list:
        if (
            not isinstance(int(a_i[0]), int)
            or not isinstance(a_i[1], str)
            or not isinstance(a_i, tuple)
            or len(a_i) != 2
        ):
            print(" getchoice function input is wrong! ")
            return ""

    # search for duplicates in c_list
    a_i = 0
    a_j = 1
    while a_i < len(a_c_list):
        a_j = a_i + 1
        while a_j < len(a_c_list):
            if (
                a_c_list[a_i][0] == a_c_list[a_j][0]
                or a_c_list[a_i][1] == a_c_list[a_j][1]
            ):
                print(" duplicate entries in function input! ")
                return ""
            a_j += 1
        a_i += 1

    # get user input
    a_num_list = []

    a_chosen = None
    a_breakloop = None
    while a_breakloop == None:
        for a_i in a_c_list:
            print(a_i[0], ": ", a_i[1])
        a_gc = input("Please enter your choice... ")
        for a_i in a_c_list:
            if a_i[0] == a_gc:
                a_breakloop = 1
                a_chosen = a_i
        if a_breakloop != 1:
            print("Please enter a correct number! ")

    print("You chose ", a_chosen)
    return a_chosen


# ------------------------------b_Show Board-----------------------------
def show_board(b_b):
    screen_clear()
    print(" ", b_b[0], "  | ", b_b[1], "  | ", b_b[2])
    print("----------------")
    print(" ", b_b[3], "  | ", b_b[4], "  | ", b_b[5])
    print("----------------")
    print(" ", b_b[6], "  | ", b_b[7], "  | ", b_b[8])


# -----------------------------c_play user ---------------------
def play_user(c_board, c_xo):
    print("You are playing as    ", c_xo)
    c_move = int(input("Please enter the number of cell you want to put your mark "))
    while not c_board[c_move].isdigit():
        print("That cell is occupied !  ")
        c_move = int(
            input("Please enter the number of cell you want to put your mark ")
        )
    c_board[c_move] = c_xo
    return c_board


# -----------------------------d_play computer ---------------------


def play_comp(d_board, d_xo):
    if d_xo == "X":
        d_op_xo = "O"
    if d_xo == "O":
        d_op_xo = "X"
    d_move_found = "no"
    d_3inrow = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    # Make three if any double exist for computer to win

    for d_i in d_3inrow:
        d_occur = 0
        for d_j in d_i:
            if d_board[d_j] == d_xo:
                d_occur += 1
            if d_board[d_j].isdigit():
                d_epmty_cell = d_j
        if d_occur == 2:
            d_move = d_epmty_cell
            d_move_found = "yes"
            print(d_i)
    print("end of computer double")

    # defend if any double exist for Oponent to win
    if d_move_found == "no":
        for d_i in d_3inrow:
            d_occur = 0
            for d_j in d_i:
                if d_board[d_j] == d_op_xo:
                    d_occur += 1
                if d_board[d_j].isdigit():
                    d_epmty_cell = d_j
            if d_occur == 2:
                d_move = d_epmty_cell
                d_move_found = "yes"
        print("end of oponent double")
        # if center is empty
    if d_move_found == "no" and d_board[4].isdigit():
        d_move = 4
        d_move_found = "yes"
        print("end of center")
        # if computer has a single
    if d_move_found == "no":
        for d_i in range(0, 9):
            if d_board[d_i] == d_xo:
                for d_j in range(-4, 5):
                    if d_i + d_j < 9 and d_i + d_j > -1:
                        if d_board[d_i + d_j].isdigit():
                            d_move = d_i + d_j
                            d_move_found = "yes"
        print("end of comp single")
        # else of all
    if d_move_found == "no":
        for d_i in [0, 2, 6, 8]:
            if d_board[d_i].isdigit():
                d_move = d_i
                d_move_found = "yes"
        print("end of else of all")
    print("d_move is =  ", d_move)
    d_board[d_move] = d_xo
    return d_board


# ---------------------------e_check_win
def check_win(e_board):
    e_3inrow = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for e_i in e_3inrow:
        if e_board[e_i[0]] == e_board[e_i[1]] == e_board[e_i[2]]:
            return e_board[e_i[0]]


# ------------------------------m_Main-----------------------------
def main():
    m_win = ""
    m_board = []
    for m_i in range(9):
        m_board.append(str(m_i))

    print(
        "You can see the board below. \nEach cell has a number in it, which is its address."
    )
    show_board(m_board)

    print("\n\n\t\t -= MENU =-\n")
    m_ch = getchoice(
        [("1", "Computer plays first"), ("2", "User plays first"), ("3", "Exit")]
    )
    m_comp_played = 0
    m_user_played = 0
    if m_ch[0] == "1":
        m_comp = "X"
        m_user = "O"
    elif m_ch[0] == "2":
        m_comp = "O"
        m_user = "X"
    if m_comp == "X":
        m_comp_played = 0
        m_board = play_comp(m_board, m_comp)
        show_board(m_board)
        m_comp_played = 1
    else:
        m_user_played = 0
        m_board = play_user(m_board, m_user)
        show_board(m_board)
        m_user_played = 1

    while m_win != "O" and m_win != "X":
        if m_comp_played == 1 and m_user_played == 0:
            m_comp_played = 0
            m_board = play_user(m_board, m_user)
            show_board(m_board)
            m_win = check_win(m_board)
            m_user_played = 1
        if m_comp_played == 0 and m_user_played == 1:
            m_user_played = 0
            m_board = play_comp(m_board, m_comp)
            show_board(m_board)
            m_win = check_win(m_board)
            # print("m_win= ", m_win)
            m_comp_played = 1

    if m_comp == m_win:
        m_winner = "Computer"
    if m_user == m_win:
        m_winner = "User"
    print("The winner is ", m_winner)


# while no one won:

# show the board
# if comp's move get comps move
# if users move get users move
# show the board
# if anyone wins announce


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")


# ------------------------------r_Root-----------------------------
import os

main()
input("press enter to exit.../")
