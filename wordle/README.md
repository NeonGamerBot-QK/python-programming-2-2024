# Project 1: Wordle 

This handout will guide you through creating a Wordle game in Python using the `colored` package to highlight letters based on the player's guesses.

## Project Structure

The main parts of the project are:
1. Getting a list of words
2. Picking a random word from the list
3. Coloring letters based on the guess
4. Evaluating the user's guess
5. Implementing the main game loop

## Step 1: Getting a List of Words

Create a list of words for the game. These words should all be five letters long.  Add more words to make the game more interesting.

## Step 2: Picking a Random Word

Use the `random` module to pick a random word from the list. The `random` module provides functions to work with randomization.

### Reference

- `random.choice(seq)`: Return a random element from the non-empty sequence `seq`.

## Step 3: Coloring Letters

Use the `colored` package to color letters based on whether they are correctly placed, present but misplaced, or not present in the secret word. The `fg` and `attr` objects from `colored` are used for foreground color and resetting the attributes.

### Reference

- `fg(color)`: Get the foreground color. The color paramter is a string (i.e. "green", "yellow")
- `attr('reset')`: Reset the text attributes to default.

## Step 4: Evaluating the User's Guess

Evaluate the user's guess against the secret word and use the `color_letter` function to highlight letters.

### Hints

- Loop through each letter of the guess and compare it with the secret word.
- Use  `==` operator to test if the letter matches exactly.
- Use `in` keyword to test if the letter is contained in the guess.
- Append a list of formatted letters using `color_letter`. 
- Return the result, collapsing the list with the string function **join**.

## Step 5: Implementing the Main Game Loop

Create the main game loop that allows the user to make up to six guesses.
Be sure to check for invalid inout (less than 5 characters or contains invalid characters).


### Hints

- Iterate over a `range(num_attemps)`, prompting the user for a new guess with the function `input`.

### Steps

1. Call `get_word_list` to get the list of words.
2. Call `pick_random_word` to select a secret word.
3. Implement the main game loop with six attempts.
4. Get user input and validate it.
5. Evaluate the guess and print the result.
6. Check for a win condition or end of attempts.