import random
Reset = "\x1b[0m"
Bright = "\x1b[1m"
Dim = "\x1b[2m"
Underscore = "\x1b[4m"
Blink = "\x1b[5m"
Reverse = "\x1b[7m"
Hidden = "\x1b[8m"

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"
FgGray = "\x1b[90m"

BgBlack = "\x1b[40m"
BgRed = "\x1b[41m"
BgGreen = "\x1b[42m"
BgYellow = "\x1b[43m"
BgBlue = "\x1b[44m"
BgMagenta = "\x1b[45m"
BgCyan = "\x1b[46m"
BgWhite = "\x1b[47m"
BgGray = "\x1b[100m"
# Constants
FLAG_PLAIN_CELL = 0b0001  # 1
FLAG_MINE = 2 #0b0010        # 2
FLAG_REVEALED = 0b0100    # 4

# Game variables
width = 10
height = 10
mine_count = 20
cells = []
revealed_cells = []
game_over = False
score = 0

def initialize_board():
    # YOUR CODE GOES HERE
    
    for i in range(height):
        row = []
        for j in range(width):
            row.append(FLAG_PLAIN_CELL)
        cells.append(row)
        revealed_cells.append(row)
    place_mines()
    pass

def place_mines():
    # YOUR CODE GOES HERE
    for i in range(mine_count):
        cords = (random.randint(0, width - 1), random.randint(0,height - 1))
        x,y = cords
        # print(f'Mime at ({x},{y})')
        cells[y][x] = FLAG_MINE
    # cells[5][5] = FLAG_MINE
    pass
inputs = []
def render_board():
    print("\033[H\033[J", end="")  
    # print(cells)
    for y in range(height):
        for x in range(width):
            cell = cells[y][x]
            if cell == FLAG_MINE and inputs.__contains__([x,y]):
                print(FgRed+"X"+Reset, end=" ")
            elif cell == FLAG_REVEALED:
                # print(cell, FLAG_MINE)
                    print(FgGreen+"."+Reset, end=" ")
            else:
                print(FgGray+"?"+Reset, end=" ")
        print()
    print(f"Score: {score}")

def reveal_cell(x, y):
    # YOUR CODE GOES HERE
    revealed_cells[y][x] = FLAG_REVEALED
    cells[y][x] = FLAG_REVEALED
    pass

def main():
    initialize_board()
    global game_over
    global score
    while not game_over:
        render_board()
        try:
            guess = input("Enter coordinates to reveal (x y): ").strip().split()
            if len(guess) != 2:
                print('bad')
                continue

            # YOUR CODE GOES HERE
            cords = guess
            x,y = (int(cords[0]), int(cords[1]))
            inputs.append([x,y])
            cell = cells[y][x]
            # print(cell, FLAG_MINE)
            reveal_cell(x,y)
            if cell == FLAG_MINE:
                cells[y][x] = FLAG_MINE
                game_over = True

            else:
                if cell != FLAG_REVEALED:
                    score += 1
        except (ValueError, IndexError):
            continue
        render_board()
    render_board()
    print("Game Over! You hit a mine.")
if __name__ == "__main__":
    main()

