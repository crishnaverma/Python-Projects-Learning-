import winsound
winsound.Beep(700, 300)  # beep sound


import random

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = {
    "easy": ["cat", "dog", "cow"],
    "medium": ["planet", "rocket", "forest"],
    "hard": ["algorithm", "neutron", "galaxy"]
}
level = input("Choose difficulty (easy/medium/hard): ").lower()
choice = random.choice(words[level])

# print(choice)  # uncomment to debug

lives = 6
correct_letters = set()
wrong_letters = set()
game_over = False

display = "_" * len(choice)
print(display)

while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    # keep asking until we get a valid single letter (no numbers, no symbols, not empty)
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one character.")
            continue
        if not guess.isalpha():
            print("Please enter a letter (a–z). Numbers and symbols are not allowed.")
            continue
        if guess in correct_letters or guess in wrong_letters:
            print(f"You already tried '{guess}'. Try a different letter.")
            continue
        break

    # Update display
    if guess in choice:
        correct_letters.add(guess)
    else:
        wrong_letters.add(guess)
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS '{choice.upper()}'! YOU LOSE ***********************")

    new_display = ""
    for letter in choice:
        if letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    print("Word to guess:", new_display)

    if "_" not in new_display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    # show hangman stage (make sure index never goes out of range)
    stage_index = max(0, 6 - lives)
    if stage_index > 6:
        stage_index = 6
    print(stages[stage_index])