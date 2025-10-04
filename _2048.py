import random

GAME_STARTED = False
GAME_WON = False
NO_MORE_MOVES = False
WINNING_NUMBER = 2048

TILE_2_PROBABILITY = 0.9
TILE_4_PROBABILITY = 0.1
BOARD_GAME = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]
]

def print_board():
    for row in BOARD_GAME:
        print(row)

    return

def initialize_board():
    empty_positions = [(i, j) for i in range(4) for j in range(4)]
    for i in range(2):
        pos = random.randint(0, 15 - i)
        row, col = empty_positions.pop(pos)
        BOARD_GAME[row][col] = 2 if random.random() < TILE_2_PROBABILITY else 4

    return BOARD_GAME

def game_over():
    temp_board = [row[:] for row in BOARD_GAME]

    if merge_up(temp_board, True) != BOARD_GAME:
        return False
    if merge_down(temp_board, True) != BOARD_GAME:
        return False
    if merge_left(temp_board, True) != BOARD_GAME:
        return False
    if merge_right(temp_board, True) != BOARD_GAME:
        return False
    
    return True

def generate_new_tile():
    empty_positions = [(i, j) for i in range(4) for j in range(4) if BOARD_GAME[i][j] is None]
    pos = random.randint(0, len(empty_positions) - 1)
    row, col = empty_positions.pop(pos)
    BOARD_GAME[row][col] = 2 if random.random() < TILE_2_PROBABILITY else 4

    if game_over():
        global NO_MORE_MOVES
        NO_MORE_MOVES = True
        print_board()
        return
    
    print_board()
    return

def merge_up(BOARD_GAME, mock=False):
    for j in range(4):
        memory = None
        position = 0
        stop_merge = False
        modified_column = [None, None, None, None]

        for i in range(4):
            if BOARD_GAME[i][j] is not None:
                if BOARD_GAME[i][j] == memory and not stop_merge:
                    modified_column[position - 1] *= 2
                    memory = None
                    stop_merge = True
                else:
                    memory = BOARD_GAME[i][j]
                    stop_merge = False
                    modified_column[position] = BOARD_GAME[i][j]
                    position += 1
            else:
                stop_merge = False

        for i in range(4):
            BOARD_GAME[i][j] = modified_column[i]

        if WINNING_NUMBER in modified_column and not mock:
            global GAME_WON
            GAME_WON = True

    return BOARD_GAME

def merge_left(BOARD_GAME, mock=False):
    for i in range(4):
        memory = None
        position = 0
        stop_merge = False
        modified_row = [None, None, None, None]

        for j in range(4):
            if BOARD_GAME[i][j] is not None:
                if BOARD_GAME[i][j] == memory and not stop_merge:
                    modified_row[position - 1] *= 2
                    memory = None
                    stop_merge = True
                else:
                    memory = BOARD_GAME[i][j]
                    stop_merge = False
                    modified_row[position] = BOARD_GAME[i][j]
                    position += 1
            else:
                stop_merge = False

        BOARD_GAME[i] = modified_row

        if WINNING_NUMBER in modified_row and not mock:
            global GAME_WON
            GAME_WON = True

    return BOARD_GAME

def merge_down(BOARD_GAME, mock=False):
    for j in range(3, -1, -1):
        memory = None
        position = 3
        stop_merge = False
        modified_column = [None, None, None, None]

        for i in range(3, -1, -1):
            if BOARD_GAME[i][j] is not None:
                if BOARD_GAME[i][j] == memory and not stop_merge:
                    modified_column[position + 1] *= 2
                    memory = None
                    stop_merge = True
                else:
                    memory = BOARD_GAME[i][j]
                    stop_merge = False
                    modified_column[position] = BOARD_GAME[i][j]
                    position -= 1
            else:
                stop_merge = False

        for i in range(4):
            BOARD_GAME[i][j] = modified_column[i]

        if WINNING_NUMBER in modified_column and not mock:
            global GAME_WON
            GAME_WON = True

    return BOARD_GAME

def merge_right(BOARD_GAME, mock=False):

    for i in range(3, -1, -1):
        memory = None
        position = 3
        stop_merge = False
        modified_row = [None, None, None, None]

        for j in range(3, -1, -1):
            if BOARD_GAME[i][j] is not None:
                if BOARD_GAME[i][j] == memory and not stop_merge:
                    modified_row[position + 1] *= 2
                    memory = None
                    stop_merge = True
                else:
                    memory = BOARD_GAME[i][j]
                    stop_merge = False
                    modified_row[position] = BOARD_GAME[i][j]
                    position -= 1
            else:
                stop_merge = False

        BOARD_GAME[i] = modified_row

        if WINNING_NUMBER in modified_row and not mock:
            global GAME_WON
            GAME_WON = True

    return BOARD_GAME

def ai_help():
    prompt = (
        "Output either w (up), a (left), s (down), d (right) that will be the best move for the current board. "
        "Here is the board: " + str(BOARD_GAME)
    )
    print("AI is thinking...")
    
    # --- Replace this with real AI API call ---
    # For example:
    # import requests
    # url = "https://your-ai-url.com/api"
    # payload = {"prompt": prompt, "password": "your_password"}
    # response = requests.post(url, json=payload)
    # move = response.json()["move"]
    # ------------------------------------------

    move = "<w, a, s, or d once you have integrated the AI>"

    print(f"AI move suggestion: {move}")
    return

def start_game():
    global GAME_STARTED, GAME_WON, NO_MORE_MOVES

    while True:
        if not GAME_STARTED:
            print("Welcome to 2048. Use w, a, s, d to move the tiles. Type 'exit' to quit.")
            print("Good luck!")
            print()

            initialize_board()
            print_board()
            GAME_STARTED = True

        elif GAME_WON:
            print("\nCongratulations, You won!")
            break
        elif NO_MORE_MOVES:
            print("\nNo more moves available. You lost!")
            break
        else:
            player_input = str(input("\nMove: ")).lower()
            board_before_move = [row[:] for row in BOARD_GAME]

            match player_input:
                case "w":
                    print("Merging up...")
                    merge_up(BOARD_GAME)
                case "a":
                    print("Merging left...")
                    merge_left(BOARD_GAME)  
                case "s":
                    print("Merging down...")
                    merge_down(BOARD_GAME)
                case "d":
                    print("Merging right...")
                    merge_right(BOARD_GAME)
                case "ai":
                    ai_help()
                    continue
                case "exit":
                    print("\nBye-bye!")
                    break
                case _:
                    print("Unknown command. Valid input: w, a, s, d, ai, exit")
                    continue
            
            if board_before_move != BOARD_GAME:
                print("Adding new tile...\n")
                generate_new_tile()
            else:
                print("No change on board - try another direction.\n")
                print_board()

if __name__ == "__main__":
    start_game()