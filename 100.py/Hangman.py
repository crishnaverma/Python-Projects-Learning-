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
=========''', ''''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




import random
word_list=["camel","hen","book"]

choice=random.choice(word_list)
print(choice)

live=6

space_holder=""
for no_letter in choice:
    space_holder+="_"
print(space_holder)


correct_list=[]
game_over= False
while not game_over:

    print("****************************<???>/6 LIVES LEFT****************************")

    gess_word=input("Enter the letter: ").lower()

    gess=""
    for letter in choice:
        if letter==gess_word:
            gess+=letter
            if gess_word in choice:
                 if gess_word not in correct_list:
                     correct_list.append(gess_word)
        elif letter in correct_list:
            gess +=letter
        else:
            gess+="_"
    print("Word to guess: "+gess)

    if gess_word not in choice:
        live-=1
       
        print(f"You guessed {gess_word}, that's not in the word. You lose a life.")

        if live == 0:
            game_over=True
            print(f"***********************IT WAS {gess_word}! YOU LOSE**********************")

    
    if "_" not in gess:
        game_over=True
        print("****************************YOU WIN****************************")

    print(stages[6-live])