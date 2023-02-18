import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["Cat", "Dog", "Rat", "Horse", "Duck", "Parrot", "Deer"]
word = random.choice(word_list).lower()
print(f"The word chosen -> {word}") # For testing purposes only (delete when code is ready)
no = len(word)

display = []
for i in range(no):
    display.append("_")
print(display)

lives_left = 6
end_game = False

while not end_game:
    guess = input("Guess a Letter : ").lower()

    if guess in display:
        print(f"You have already guessed the letter '{guess}'. Please try again.")
        continue

    if guess not in word:
        lives_left -= 1
        print(f"Wrong Guess!\nYou have {lives_left} lives left.")
        if lives_left == 0:
            print(f"You Lost! The word was '{word}'.")
            end_game = True
            break
    else:
        for i in range(no):
            if word[i] == guess:
                display[i] = guess

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You Won!")
        break

    print(stages[lives_left])
