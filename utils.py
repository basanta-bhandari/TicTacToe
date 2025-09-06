import random
import os
import time

game_running=True
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
# ███████████████████████████████████████████████████████████████████████████████████
# █▌████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗▐█
# █▌╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝▐█
# █▌   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  ▐█
# █▌   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  ▐█
# █▌   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗▐█
# █▌   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝▐█
# ███████████████████████████████████████████████████████████████████████████████████
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
        
def input_manager(position, character):
    global a, b, c, d, e, f, g, h, i
    if position=='1':
        a = character
    if position=='2':
        b = character
    if position=='3':
        c = character
    if position=='4':
        d = character
    if position=='5':
        e = character
    if position=='6':
        f = character
    if position=='7':
        g = character
    if position=='8':
        h = character
    if position=='9':
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



    



    




