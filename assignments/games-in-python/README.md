
# 📘 Assignment: Hangman Game

## 🎯 Objective

Practice Python skills including string manipulation, loops, conditionals, and random selection by building a classic Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up Word Selection and Game State

#### Description
Implement the initial game setup by creating a predefined word list and randomly selecting a word for the player to guess. Track which letters have been guessed and how many incorrect attempts remain.

#### Requirements
Completed program should:

- Define a list of at least 10 words to use in the game
- Randomly select one word from the list using the `random` module
- Initialize a variable to track the number of incorrect guesses remaining (e.g., 6)
- Initialize a list or set to store letters the player has already guessed
- Example setup:
  ```python
  import random
  words = ["python", "hangman", "keyboard", ...]
  word = random.choice(words)
  attempts_remaining = 6
  guessed_letters = []
  ```


### 🛠️ Implement the Game Loop

#### Description
Create the main game loop that accepts player input, validates guesses, updates the game state, and displays current progress in the `_ _ _` format after each guess.

#### Requirements
Completed program should:

- Display the current word progress using underscores for unguessed letters (e.g., `_ _ a _`)
- Prompt the player to enter a single letter guess
- Validate that the input is a single alphabetic character not already guessed
- Update the display when a correct letter is guessed
- Decrease the remaining attempts count when an incorrect letter is guessed
- Example output after a guess:
  ```
  Word: _ _ t _ _ n
  Incorrect guesses remaining: 5
  Guessed letters: ['a', 't']
  Enter a letter: 
  ```


### 🛠️ Handle Game End Conditions

#### Description
Detect when the game is over — either the player has correctly guessed the entire word, or they have run out of attempts — and display an appropriate win or lose message.

#### Requirements
Completed program should:

- End the game and display a congratulations message when the full word is guessed
- End the game and reveal the answer when the player runs out of attempts
- Display the number of incorrect guesses remaining after each turn
- Show all previously guessed letters so the player can track their progress
- Example win message:
  ```
  Congratulations! You guessed the word: python
  ```
- Example lose message:
  ```
  Game over! The word was: python
  ```
