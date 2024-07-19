import random
import os
import sys 
# from colored import fg, attr
FgGray = "\x1b[90m"
FgYellow = "\x1b[33m"
FgGreen = "\x1b[32m"
Reset = "\x1b[0m"
# board = []
def get_word_list():
    # Create a list of words for the game; the more the merrier!

    # YOUR CODE GOES HERE
    return ['tasco', 'scalp', 'tress', 'folks']
    pass

def pick_random_word(word_list):
    # Use the random module to pick a random word from the list
    # YOUR CODE GOES HERE
    return random.choice(word_list)
    pass

def color_letter(letter, color):
    # Use the colored module to color the letter

    # YOUR CODE GOES HERE
    return f'{color}{letter}{Reset}'
    pass

def evaluate_guess(guess, secret_word):
    # Determine how many letters in the guess are in the secret word
    words = []
    # YOUR CODE GOES HERE
    for i in range(len(guess)):
        letter = guess[i]
        lIndex = secret_word.find(letter)
        if lIndex >= 0:
            if lIndex == guess.find(letter):
                words.append(color_letter(letter=letter,color=FgGreen))
            else:
                words.append(color_letter(letter=letter,color=FgYellow))
        else:
            words.append(color_letter(letter=letter, color=FgGray))
        pass 
    return words;
    pass
# global index_of_tries
# index_of_tries = 0
def play_wordle():
    # Loop through the game until the user guesses the word or runs out of guesses

    # YOUR CODE GOES HERE
    
    print("Starting Wordle...")
    word = pick_random_word(get_word_list())
    index = 0
    board = []
    def run(err, index):
        # global index
        if os.environ.get('REVAL_WORD'):
            print(f'Cheater: {word}')
        print(f'Try {index}/6')
        print('============================================')
        if len(board) > 0:
            for row in board:
                print(''.join(row))
        else:
            print('<empty board>')
        print('============================================')
        if err:
            print(err)
        # print()
        inp = input('Enter your guess: ')
        if inp.isalpha() == False or len(inp) < 5:
            os.system('cls||clear')
            run(err="Make sure you only have letters and have 5 chars", index=index)
            return;
        inp = inp[0:5]
        nextRow = evaluate_guess(inp, word)
        if len(board) >= 5:
            if inp == word:
                print(f'{FgGreen}You Won?{Reset}')
            else:
                print(f'{FgGray}You lost{Reset}')
            quit()
        else:
            if inp == word:
                print(f'{FgGreen}You Won?{Reset}')
                quit()
            else:
                board.append(nextRow)
                os.system('cls||clear')
                index += 1
                run(err=None,index=index)
        pass
    pass
    run(err=None,index=index)

if __name__ == "__main__":
    play_wordle()