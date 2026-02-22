# Hangman.py
# User guesses a word, letter by letter, until they have guessed the word or run out of guesses.
# Word chosen from file, user is asked for their first guess, shows correct letter.
import random


def print_logo():
    print("  _                                              ")
    print(" | |                                             ")
    print(" | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print(" |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|")
    print(" | | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print(" |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|")
    print("                     __/ |                      ")
    print("                    |___/                       ")


def start_game():
    print_logo()
    print("\nWelcome to Hangman! Guess the word, letter by letter. \nYou have 6 chances to guess the word before you lose. Good luck!")
    word_list = get_word_list()
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = []
    for _ in range(word_length):
        display += "_"
    print_game(0)
    print(display)
    check_guess(chosen_word, 0, display)


def check_guess(chosen_word, wrong_guesses, display):
    solved = False
    max_guesses = 6
    while solved == False:
        if wrong_guesses >= max_guesses:
            print(f"\n Game Over! The word was: {chosen_word}")
            break
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            is_containing = False
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
                    is_containing = True
                    if "_" not in display:
                        solved = True
                        print("\nCongratulations! You've guessed the word.")
                        break
            if is_containing == False:
                wrong_guesses += 1
            print_game(wrong_guesses)
            print(display)
        else:
            print("Invalid input. Please enter a single letter.")


def get_word_list():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return words


def print_game(guesses):
    print("\n")
    print(" +---+")
    print(" |   |")

    if guesses == 0:
        print("     |")
        print("     |")
        print("     |")
    elif guesses == 1:
        print(" O   |")
        print("     |")
        print("     |")
    elif guesses == 2:
        print(" O   |")
        print(" |   |")
        print("     |")
    elif guesses == 3:
        print(" O   |")
        print("/|   |")
        print("     |")
    elif guesses == 4:
        print(" O   |")
        print("/|\\  |")
        print("     |")
    elif guesses == 5:
        print(" O   |")
        print("/|\\  |")
        print("  \\  |")
    elif guesses == 6:
        print(" O   |")
        print("/|\\  |")
        print("/ \\  |")

    print("     |")
    print("=========")


start_game()
