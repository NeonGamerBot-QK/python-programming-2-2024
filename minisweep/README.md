# Project 2 Handout: Mini Minesweeper

## Project Overview

In this project, you will create a simplified version of the Minesweeper game using Python. The game will involve generating a game board, scattering mines, and allowing the player to reveal cells. The objective is to reveal as many safe cells as possible without hitting a mine. The game ends when a mine is revealed, and the player's score is the number of safe cells revealed.

## Learning Objectives

- Building a list of lists with comprehensions. 
- Learn how to index lists and nested lists to represent a game board.
- Practice using global variables to manage game state.
- Practice using bitwise operators to update binary data.

## Project Requirements

### Initialization

- Define constants for different cell states (plain, mine, revealed).
- Create functions to initialize the game board and place mines.

### Game Logic

- Implement a function to render the game board to the console.
- Develop a function to handle revealing cells, updating the game state, and checking for mines.
- Create a main game loop to handle user input and game progression.

### User Interaction

- Prompt the user to enter coordinates to reveal cells.
- Validate user input to ensure it is within the game board boundaries.

### End Game

- Detect when a mine is revealed and end the game.
- Display the player's score and a game over message.

## Project Structure

- `FLAG_PLAIN_CELL`, `FLAG_MINE`, `FLAG_REVEALED`: Constants representing different cell states.
- `width`, `height`, `mine_count`, `cells`, `game_over`, `score`: Global variables for game configuration and state.
- `initialize_board()`: Function to set up the game board and place mines.
- `place_mines()`: Function to randomly place mines on the game board.
- `render_board()`: Function to display the game board to the console.
- `reveal_cell(x, y)`: Function to reveal a cell and update the game state.
- `main()`: Main game loop handling user input and game progression.

## Step-by-Step Instructions

### Define Constants and Global Variables

- Define binary constants (0bXXX) for plain cells, mines, and revealed cells.
- Set up global variables for the game board dimensions, mine count, game state, and score.

### Initialize the Game Board

- Implement the `initialize_board()` function to create a 2D list representing the game board.
- Write the `place_mines()` function to randomly place a specified number of mines on the board.

### Render the Game Board

- Develop the `render_board()` function to print the game board to the console. Use different symbols to represent revealed and unrevealed cells.

### Reveal Cells

- Implement the `reveal_cell(x, y)` function to reveal a cell and check if it is a mine. Update the game state and score accordingly.

### Main Game Loop

- Create the `main()` function to handle the game loop. This function should render the board, prompt the user for input, and call `reveal_cell()` to update the game state.
- Add input validation to ensure the user enters valid coordinates.

### End Game Detection

- Update the `reveal_cell(x, y)` function to set `game_over` to `True` if a mine is revealed.
- Display a game over message and the player's score when the game ends.
