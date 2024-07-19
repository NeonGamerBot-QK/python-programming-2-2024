import random

# Constants
FLAG_PLAIN_CELL = 0b0001  # 1
FLAG_MINE = 0b0010        # 2
FLAG_REVEALED = 0b0100    # 4

# Game variables
width = 10
height = 10
mine_count = 20
cells = []
game_over = False
score = 0

def initialize_board():
    # YOUR CODE GOES HERE
    pass

def place_mines():
    # YOUR CODE GOES HERE
    pass

def render_board():
    print("\033[H\033[J", end="")  
    for y in range(height):
        for x in range(width):
            cell = cells[y][x]
            if cell & FLAG_REVEALED:
                if cell & FLAG_MINE:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            else:
                print("?", end=" ")
        print()
    print(f"Score: {score}")

def reveal_cell(x, y):
    # YOUR CODE GOES HERE
    pass

def main():
    initialize_board()
    while not game_over:
        render_board()
        try:
            guess = input("Enter coordinates to reveal (x y): ").strip().split()
            if len(guess) != 2:
                continue

            # YOUR CODE GOES HERE

        except (ValueError, IndexError):
            continue
        render_board()
    print("Game Over! You hit a mine.")

if __name__ == "__main__":
    main()

