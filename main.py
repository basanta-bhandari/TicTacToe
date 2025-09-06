
import random
import os
import time
from utils import*

def main():
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

if initialize()==True:
    main()