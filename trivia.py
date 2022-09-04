# ---------------------------plot-----------------------------------------------------------------------
# show the menu: which game? and exit
# for any game go to file and load

# ---------------------------a_get choice-----------------------------------------------
def getchoice(a_c_list):
    """Show the menu and return users choice
    argument is a list consisting of double tuples
    the type of the members of the tuple are all strings"""

    # check if c_list entries are ok
    if a_c_list == []:
        return ""
    for a_i in a_c_list:
        if (
            not isinstance(a_i[0], str)
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
    a_chosen = None
    a_breakloop = None
    while a_breakloop == None:
        for a_i in a_c_list:
            print(a_i[0], "-", a_i[1])
        a_gc = input("please enter your choice and press Enter... ")
        for a_i in a_c_list:
            if a_i[0] == a_gc:
                a_breakloop = 1
                a_chosen = a_i
        if a_breakloop != 1:
            print("Please enter a correct number! ")
    screen_clear()
    print("You chose ", " <  ", a_chosen[1], " >  ")
    return a_chosen


# ---------------------------b_fill----------------------------------------------
"""fill the database for the first time"""


def fill():

    import shelve

    b_s = shelve.open("game_database")

    for b_i in range(102, 122):
        b_s[str(b_i)] = ["", [("", ""), ("", ""), ("", ""), ("", "")], "", "", ""]
    b_s["101"] = ["This game is about Movies. "]
    b_s["102"] = [
        "1. Who was the director of 'The birds'?",
        [("a", "Hitchcock"), ("b", "Soderberg"), ("c", "Spilberg"), ("d", "Eastwood")],
        ("a", "Hitchcock"),
        "It was a horror film by Horror King Mr. Hitchcock",
        "10",
    ]
    b_s["103"] = [
        "2. Who played the 'Raging Bull?",
        [("a", "Cruze"), ("b", "Deniro"), ("c", "Schwartzeneger"), ("d", "Stalone")],
        ("b", "Deniro"),
        "The film was in black and white",
        "15",
    ]
    b_s["122"] = ["Thank you for playing this game"]

    for b_i in range(202, 222):
        b_s[str(b_i)] = ["", [("", ""), ("", ""), ("", ""), ("", "")], "", "", ""]
    b_s["201"] = ["This game is about Computers. "]
    b_s["202"] = [
        "1. Which was introduced after Windows95?",
        [("a", "Win98"), ("b", "Win7"), ("c", "Win_XP"), ("d", "WinNT")],
        ("d", "WinNT"),
        "It was intended for servers",
        "11",
    ]
    b_s["203"] = [
        "2. How many cores a PentiumII consists of?",
        [("a", "1"), ("b", "2"), ("c", "4"), ("d", "6")],
        ("a", "1"),
        "It was introduced in 90's",
        "12",
    ]
    b_s["222"] = ["Well,  these belong to the past!"]
    b_s.close()


# ---------------------------c_play game--------------------------------------------
def play_game(c_game):
    c_user_score = 0
    import shelve

    c_s = shelve.open("game_database")
    print(c_s[c_game + "01"])
    for c_i in range(2, 22):
        if c_i < 10:
            c_i_st = "0" + str(c_i)
        else:
            c_i_st = str(c_i)
        c_index = c_game + c_i_st
        if not c_s[c_index][0] == "":
            screen_clear()
            print(c_s[c_index][0])
            c_user_ans = getchoice(c_s[c_index][1])
            if c_user_ans[0] == c_s[c_index][2][0]:
                print("You were correct !")
                print(c_s[c_index][4], " was added to your score")
                c_user_score += int(c_s[c_index][4])
            else:
                print("You were wrong !")
                print(c_s[c_index][2], "was correct ")
            print(c_s[c_index][3])
            input(" press Enter to continue")

    # print("c_game+'22' is", c_game+"22")
    screen_clear()
    print(c_s[c_game + "22"][0])
    print("You earned ", c_user_score, " from this part")
    input(" press Enter to continue")
    c_s.close()
    return c_user_score


# ---------------------------d_edit database(under construction!!)--------------------------------------------


# ---------------------------e_high_score-----------------------------------------
def high_score(e_score):
    try:
        e_file = open("score_file.txt", "r")
        e_file.close()
    except FileNotFoundError:
        e_file = open("score_file.txt", "w")
        e_file.write("-,0\n")
        e_file.close()

    e_file = open("score_file.txt", "r")
    e_len = 0
    for e_l in e_file:
        e_len += 1
    e_file.close()
    e_file = open("score_file.txt", "r+")
    # for e_l in range(1, e_len):
    #     print(e_file.readline())
    e_char = ""
    e_prev_high_name = ""
    e_prev_high_score = ""

    while e_char != ",":
        e_char = e_file.read(1)
        if e_char != ",":
            e_prev_high_name += e_char
    while e_char != "\n":
        e_char = e_file.read(1)
        if e_char != "\n":
            e_prev_high_score += e_char
    # print(
    #    "e_prev_high_name=", e_prev_high_name, "e_prev_high_score=", e_prev_high_score
    # )
    print("Your total score is: ", e_score)
    if e_score > int(e_prev_high_score):
        print("You have brocken the record!")
        e_name = input("Enter your name... ")
        e_file.write(e_name)
        e_file.write(",")
        e_file.write(str(e_score))
        e_file.write("\n")
    e_file.close()


# ---------------------------m_main-----------------------------------------
def main():
    screen_clear()
    print("          -= Welcome to Trivia Game =-  \n\n")
    input("Please press Enter to start the game...")
    m_user_score = 0
    m_played = []
    fill()
    m_menu = [
        ("1", "Movie Game"),
        ("2", "Computer Game"),
        ("3", "Edit Database"),
        ("4", "Reset high scores"),
        ("5", "Show high scores"),
        ("6", "Exit"),
    ]
    m_choice = "1"
    while m_choice[0] in ["1", "2", "3", "4", "5"]:
        screen_clear()
        print("\tMAIN MENU\n")
        m_choice = getchoice(m_menu)
        if m_choice[0] == "1":
            if "1" in m_played:
                print("you have played this game before, please choose another game")

            else:
                m_user_score += play_game("1")
                m_played += "1"
                # print("You score is ", m_user_score)
                high_score(m_user_score)
            input("Please press Enter to continue...")

        if m_choice[0] == "2":
            if "2" in m_played:
                print("you have played this game before, please choose another game")
            else:
                m_user_score += play_game("2")
                m_played += "2"
                # print("You score is ", m_user_score)
                high_score(m_user_score)
            input("Please press Enter to continue...")
        if m_choice[0] == "3":
            print("This feature is not implemented yet")
            input("Please press Enter to continue...")

        if m_choice[0] == "4":
            m_file = open("score_file.txt", "w")
            m_file.write("")
            m_file.close()
            print("High score list was reset")
            input("Please press Enter to continue...")
        if m_choice[0] == "5":
            m_file = open("score_file.txt", "r")
            m_len = 0
            for m_l in m_file:
                m_len += 1
            m_file.close()
            m_file = open("score_file.txt", "r")
            for m_l in range(1, m_len):
                m_file.readline()
            print("Highest record is:  ", m_file.readline())
            m_file.close()
            input("Please press Enter to continue...")


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")


# ---------------------------r_root-----------------------------------------
import os

main()
input("press enter to exit...")
