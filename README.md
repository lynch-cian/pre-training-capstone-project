# Hangman Game

A classic word-guessing game implemented in Python. Guess the hidden word letter by letter before running out of chances!

## How to Play

1. The game selects a random word from a word list
2. You have **6 incorrect guesses** before the game is over
3. Guess one letter at a time
4. For each correct guess, the letter is revealed in the word
5. For each incorrect guess, another body part is drawn
6. Win by guessing all the letters in the word before reaching 6 wrong guesses
7. Lose if you reach 6 wrong guesses before completing the word

## Requirements

- `words.txt` file in the same directory containing one word per line

## How to Run

python3 hangman.py

## Features

- **ASCII Art Display** - Visual representation of the hangman that updates with each wrong guess
- **Input Validation** - Only accepts single alphabetic characters as valid guesses
- **Word Selection** - Randomly selects words from a word list file
- **Game Status** - Displays current progress and number of wrong guesses

## Files

- `hangman.py` - Main game file
- `words.txt` - Text file containing words (one per line)

## Game Rules

- Only single letters are accepted as guesses
- Letters are case-insensitive (uppercase and lowercase are treated the same)
- Duplicate guesses are still counted as attempts
- Win condition: All letters in the word are guessed
- Lose condition: 6 incorrect guesses made
