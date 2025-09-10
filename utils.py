import random
import os
import time


game_running = True


a="1"
b="2"
c="3"
d="4"
e="5"
f="6"
g="7"
h="8"
i="9"
tic_tac_toe="""
  XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX
  XO████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗XO
  XO╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝XO
  XO   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  XO
  XO   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  XO
  XO   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗XO
  XO   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝XO
  XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX
"""
def get_current_lists():
    listh1=[a, b, c]
    listh2=[d, e, f]
    listh3=[g, h, i]
    listv1=[a, d, g]
    listv2=[b, e, h]
    listv3=[c, f, i]
    listd1=[a, e, i]
    listd2=[c, e, g]
    return [listh1, listh2, listh3, listv1, listv2, listv3, listd1, listd2]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def initialize():
    clear()
    time.sleep(1)
    print("Initializing....")
    time.sleep(1)
    print("Loading packadges...")
    time.sleep(1)
    ipt_initialize=input("shall we start?(y/n):")
    if ipt_initialize.lower()=="y":
        return True
    else:  
        return False
clear()

def print_symbol(a):
    if (a=='X' or  a=='x'):
        a=0
    else:
        a=1
    x="X"
    o="O"
    lst=[x,o]
    print(lst[a])

def check_win_position(tlist):
    if tlist and all(x == tlist[0] for x in tlist):
        return True
    else:
        return False
     
def check_win():
    current_lists = get_current_lists()
    for i in current_lists:
        if check_win_position(i)==True:
            return True
    return False

def get_possible_moves():
    pmoves = []
    for pos in [a, b, c, d, e, f, g, h, i]:
        if pos != "X" and pos != "O":
            pmoves.append(pos)
    return pmoves

def input_manager(position, character):
    if position  in  get_possible_moves():
        global a, b, c, d, e, f, g, h, i
        if "1" in position:
            a = character
        if "2" in position:
            b = character
        if "3" in position:
            c = character
        if "4" in position:
            d = character
        if "5" in position:
            e = character
        if "6" in position:
            f = character
        if "7" in position:
            g = character
        if "8" in position:
            h = character
        if "9" in position:
            i = character

def print_grid():
    print(f"""
    ________________
    ( {a})| ( {b}) |( {c})
    ---|-----|----
    ( {d})| ( {e}) |( {f})
    ---|-----|---
    ( {g})| ( {h}) |( {i})
    """)

def IvI_manual():
    clear()
    print(tic_tac_toe)
    game_running = True
    while game_running :
        print_grid()
        p1_xy=input("Player 1:\n character:O \n position:")
        p1_xo='O'
        input_manager(p1_xy, p1_xo)
        print_grid()
        if check_win():
            print("Player 1 (O) wins!")
            game_running = False
            break
        p2_xy=input("Player 2:\n character:X \n position:")
        p2_xo='X'
        input_manager(p2_xy, p2_xo)
        print_grid()
        if check_win():
            print("Player 2 (X) wins!")
            game_running = False
            break

def ask_mode():
    ask =  input("Which mode would you like to play?(1/2):\n 1.Against computer, \n 2.1v1 against friends \n")
    if ask == "1":
        return 1
    if ask == "2":
        return -1
    return 0

def start_game():
        print("Starting game.....")
        time.sleep(1)
        print("Loading logo......")
        time.sleep(1)
        print("Creating grid.....")
        time.sleep(1)
        clear()
        print(tic_tac_toe)
        print(grid)







