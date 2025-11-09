import random
import time
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialize colorama for Windows
init(autoreset=True)

# Create fancy title
f = Figlet(font='slant')
print(Fore.CYAN + f.renderText('HANGMAN'))

# Hangman stages
stages = [
    '''
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
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

# Word list
words = {
    "easy": ["cat", "dog", "cow"],
    "medium": ["planet", "rocket", "forest"],
    "hard": ["algorithm", "neutron", "galaxy"]
}
level = input("Choose difficulty (easy/medium/hard): ").lower()
choice = random.choice(words[level])

# print(choice)  # uncomment for debugging

lives = 6
correct_list = []
game_over = False
display = "_" * len(choice)
score = 0

# Animated intro
print(Fore.MAGENTA + "Loading word", end="")
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print("\n")

# Show initial state
print(Fore.YELLOW + "Word to guess:", Fore.WHITE + " ".join(display))

while not game_over:
    print(Fore.CYAN + f"\n{'*' * 20} {lives}/6 LIVES LEFT {'*' * 20}")
    print(Fore.LIGHTBLACK_EX + "Guessed letters:", ", ".join(correct_list) if correct_list else "None")
    print(Fore.RED + "Lives: " + "❤️" * lives + "🖤" * (6 - lives))

    guess = input(Fore.GREEN + "Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print(Fore.YELLOW + "⚠️ Please enter a single valid letter!")
        continue

    # Already guessed
    if guess in correct_list:
        print(Fore.YELLOW + "😅 You already guessed that letter. Try another one!")
        continue

    new_display = ""
    correct = False

    # Main guessing loop
    for letter in choice:
        if letter == guess:
            new_display += letter
            correct = True
            if guess not in correct_list:
                correct_list.append(guess)
        elif letter in correct_list:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(Fore.WHITE + "\nWord to guess:", Fore.LIGHTCYAN_EX + " ".join(display))

    if not correct:
        lives -= 1
        print(Fore.RED + f"❌ Wrong guess! The letter '{guess}' is not in the word.")
        print(Fore.RED + random.choice(["Try again!", "Oof!", "Keep going!", "Don't give up!"]))
        score -= 5
        if lives == 0:
            game_over = True
            print(Fore.RED + f"\n💀 You’re out of lives! The word was '{choice.upper()}'.")
            print(Fore.RED + f"Your final score: {score}")
    else:
        print(Fore.GREEN + random.choice(["✅ Great!", "👏 Nice one!", "🎯 Correct!", "🔥 You got it!"]))
        score += 10

    if "_" not in display:
        game_over = True
        print(Fore.GREEN + "\n🎉 YOU WIN!")
        print(Fore.GREEN + f"✅ The word was '{choice.upper()}'")
        print(Fore.CYAN + f"🏆 Your final score: {score}")
        print(Fore.MAGENTA + f.renderText("You Win!"))

    # Show hangman stage
    print(Fore.LIGHTWHITE_EX + stages[6 - lives])
    time.sleep(0.3)

# Option to replay
print("\n" + "*" * 60)
play_again = input(Fore.YELLOW + "Do you want to play again? (y/n): ").lower()
if play_again == 'y':
    print(Fore.CYAN + "\nRestarting the game...\n")
    time.sleep(1)
    exec(open(__file__).read())
else:
    print(Fore.MAGENTA + "Thanks for playing Hangman! 🎮")
