import random

# List of words to choose from
words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'keyboard']

# Hangman ASCII stages
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Choose a random word
word = random.choice(words)
word_letters = set(word)
guessed_letters = set()
lives = len(stages) - 1

print("🎮 Welcome to Hangman!\n")

while lives > 0 and len(word_letters) > 0:
    # Show current word progress
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("\nWord: ", ' '.join(display_word))
    print(stages[len(stages) - 1 - lives])
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Lives left: {lives}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("❗ You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("✅ Correct!")
    else:
        lives -= 1
        print("❌ Incorrect.")

# Game result
if len(word_letters) == 0:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(stages[-1])
    print(f"\n💀 Game Over. The word was: {word}")
