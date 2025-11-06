import random

# Word list categorized by difficulty
easy_words = [
    "cat", "dog", "sun", "book", "tree",
    "fish", "code", "java", "pen", "cup"
]

medium_words = [
    "python", "laptop", "screen", "object", "method",
    "program", "engineer", "keyboard", "compiler", "syntax"
]

hard_words = [
    "algorithm", "processor", "developer", "interface", "database",
    "framework", "encryption", "operating", "debugging", "machinelearning"
]

print("🎯 Welcome to the Hangman Game!")
print("Select Difficulty Level:")
print("1️⃣ Easy\n2️⃣ Medium\n3️⃣ Hard")

# Get user’s choice
choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    words = easy_words
    print("\n🟢 Easy mode selected!")
elif choice == "2":
    words = medium_words
    print("\n🟡 Medium mode selected!")
elif choice == "3":
    words = hard_words
    print("\n🔴 Hard mode selected!")
else:
    print("\n⚠️ Invalid choice! Defaulting to Medium mode.")
    words = medium_words

# Randomly pick a word from selected list
word = random.choice(words)
guessed_letters = []
attempts = 6

print("\nLet's start! You have 6 attempts.")
print("_ " * len(word))

# Main game loop
while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter! Try again.")
        continue

    guessed_letters.append(guess)

    # Check guess correctness
    if guess in word:
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    # Display current word progress
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

    # Win condition
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break

# Lose condition
if attempts == 0:
    print(f"\n💀 Game Over! The correct word was '{word}'.")
