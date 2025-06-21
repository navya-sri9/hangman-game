import random
# List of 5 predefined words
word_list = ['apple', 'table', 'chair', 'grape', 'zebra']

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display setup
display_word = ['_' for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", max_incorrect, "incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_incorrect and '_' in display_word:
    print("Word:", ' '.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Invalid input. Enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_incorrect - incorrect_guesses} guesses left.\n")

# Final outcome
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)