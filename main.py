
import random
import os
import time
from comp_bot import*
from utils import*
 
current_turn = "player" 
def switch_turn():
    global current_turn
    if current_turn == "player":
        current_turn = "bot"
    else:
        current_turn = "player"

def main():
    if ask_mode() == -1:
        IvI_manual() 
    else:
        print(tic_tac_toe)
        while game_running:
            print_grid()
            
            if current_turn == "player":
                player_move = input("Your move: ")
                input_manager(player_move, "X")
                print(get_possible_moves())
                if check_win():
                    print("Player wins!")
                    break
                    
            else:  
                bot_move = play_bot("O") 
                if bot_move:
                    input_manager(bot_move, "O")
                    print(f"Bot played position {bot_move}")
                    print(get_possible_moves())
                if check_win():
                    print("Bot wins!")
                    break
            
            switch_turn()

if initialize():
    main()


       