from utils import *

bot_running = True

def check_win():
    for lst in get_current_lists():
        if all(x == 'O' for x in lst):  
            return 1
        elif all(x == 'X' for x in lst):  
            return -1
    return 0    

def is_board_full():
    if len(get_possible_moves()) == 0:
        return True
    else:
        return False

def winning_moves(c):
    wmoves = []
    available_moves = get_possible_moves()  
    
    for lst in get_current_lists():
        if lst.count(c) == 2:  # If character 'c' appears twice in this line
            for pos in lst:
                if pos in available_moves:  # Only add if position is still available
                    wmoves.append(pos)
    return wmoves

def who_won():
    if check_win() == 1:
        print("Player 1(O) won!")
    elif check_win() == -1:  # Fixed: was checking == 1 twice
        print("Player 2(X) won!")
    else:
        if is_board_full() == True:
            print("The game is tied.")

def play_bot(c):
    if c == "O":
        opponent = "X" 
    else:
        opponent = "O"
    
    # Get available moves first
    available_moves = get_possible_moves()
    
    if not available_moves:  # No moves left
        return None
    
    # Check for immediate winning moves first
    winning_positions = winning_moves(c)
    if winning_positions:
        # Make sure the winning position is actually available
        for pos in winning_positions:
            if pos in available_moves:
                return pos
    
    # Check for blocking moves
    blocking_positions = winning_moves(opponent)
    if blocking_positions:
        # Make sure the blocking position is actually available
        for pos in blocking_positions:
            if pos in available_moves:
                return pos
    
    # If no winning or blocking moves, take center, then corners, then edges
    preferred_moves = ['5', '1', '3', '7', '9', '2', '4', '6', '8']
    for move in preferred_moves:
        if move in available_moves:
            return move
    
    # Fallback: return first available move
    return available_moves[0] if available_moves else None