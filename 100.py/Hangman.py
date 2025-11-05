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




import random

word_list = ["camel", "hen", "book"]
choice = random.choice(word_list)
# print(choice)  # uncomment for debugging

lives = 6
correct_list = []
game_over = False

# Create initial display
display = "_" * len(choice)
print(display)

while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Enter a letter: ").lower()

    new_display =""
    gess=""
    for letter in choice:
        if letter == guess:
            new_display += letter
            if guess not in correct_list:
                correct_list.append(guess)
        elif letter in correct_list:
            new_display += letter
        else:
            new_display += "_"

    print("Word to guess:", new_display)

    if guess not in choice:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS '{choice}'! YOU LOSE ***********************")

    if "_" not in new_display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(stages[6 - lives])
