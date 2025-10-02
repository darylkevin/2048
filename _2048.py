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
NUMBERS = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

def initialize_board():
    empty_positions = [(i, j) for i in range(4) for j in range(4)]
    for i in range(2):
        pos = random.randint(0, 15 - i)
        row, col = empty_positions.pop(pos)
        BOARD_GAME[row][col] = 2 if random.random() < TILE_2_PROBABILITY else 4

    return BOARD_GAME

def generate_new_tile():
    empty_positions = [(i, j) for i in range(4) for j in range(4) if BOARD_GAME[i][j] is None]
    if not empty_positions:
        global NO_MORE_MOVES
        NO_MORE_MOVES = True
        return

    pos = random.randint(0, len(empty_positions) - 1)
    row, col = empty_positions.pop(pos)
    BOARD_GAME[row][col] = 2 if random.random() < TILE_2_PROBABILITY else 4

    return BOARD_GAME

def merge_up():
    return BOARD_GAME

def merge_left(BOARD_GAME):
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

    return BOARD_GAME

def merge_down():
    return BOARD_GAME

def merge_right(BOARD_GAME):

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

    return BOARD_GAME


def start_game():
    global GAME_STARTED, GAME_WON, NO_MORE_MOVES

    while True:
        if not GAME_STARTED:
            print("Welcome to 2048. Use w, a, s, d to move the tiles. Type 'exit' to quit.")
            print("Good luck!")
            print()

            initialize_board()
            GAME_STARTED = True

        elif GAME_WON:
            print("You won!")
            break
        elif NO_MORE_MOVES:
            print("No more moves available. You lost!")
            break
        else:
            print("Current board:")
            for row in BOARD_GAME:
                print(row)
            player_input = str(input("\nMove: ")).lower()

            match player_input:
                case "w":
                    print("Merging up...\n")
                    merge_up(BOARD_GAME)
                    print("Adding new tile...\n")
                    generate_new_tile()
                case "a":
                    print("Merging left...\n")
                    merge_left(BOARD_GAME)  
                    print("Adding new tile...\n")
                    generate_new_tile()
                case "s":
                    print("Merging down...\n")
                    merge_down(BOARD_GAME)
                    print("Adding new tile...\n")
                    generate_new_tile()
                case "d":
                    print("Merging right...\n")
                    merge_right(BOARD_GAME)
                    print("Adding new tile...\n")
                    generate_new_tile()
                case "exit":
                    print("Bye!")
                    break
                case _:
                    print("Unknown command. Valid input: w, a, s, d, exit")
                    continue

if __name__ == "__main__":
    start_game()