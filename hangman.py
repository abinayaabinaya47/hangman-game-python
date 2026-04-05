import random

# Word list with hints
words = {
    "python": "Programming language",
    "apple": "A fruit",
    "tiger": "A wild animal",
    "india": "A country",
    "laptop": "Electronic device"
}

word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game")
print("💡 Hint:", hint)

# Display hidden word
display = ["_"] * len(word)

while attempts > 0:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validation
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Enter a valid single letter")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    # Check letter
    if guess in word:
        print("✅ Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong!")
        attempts -= 1

    # Win check
    if "_" not in display:
        print("\n🎉 You Win! The word was:", word)
        break

# Lose condition
if "_" in display:
    print("\n💀 You Lost! The word was:", word)