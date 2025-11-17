import random


logo = '''
$$$$$$$\ $$\                 $$\         $$\     $$\                                                                       $$\                           
$$  _____|\__|                $$ |        $$ |    $$ |                                                                      $$ |                          
$$ |      $$\ $$$$$$$\   $$$$$$$ |      $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$$$$\    $$ |$$  __$$\ $$  __$$ |      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  __|   $$ |$$ |  $$ |$$ /  $$ |        $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |$$ |  $$ |$$ |  $$ |        $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
$$ |      $$ |$$ |  $$ |\$$$$$$$ |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
\__|      \__|\__|  \__| \_______|         \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\__| \__| \__|\_______/  \_______|\__| 
'''



win = """
$$\     $$\                         $$\      $$\                     
\$$\   $$  |                        $$ | $\  $$ |                    
 \$$\ $$  /$$$$$$\  $$\   $$\       $$ |$$$\ $$ | $$$$$$\  $$$$$$$\  
  \$$$$  /$$  __$$\ $$ |  $$ |      $$ $$ $$\$$ |$$  __$$\ $$  __$$\ 
   \$$  / $$ /  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ /  $$ |$$ |  $$ |
    $$ |  $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |  $$ |$$ |  $$ |
    $$ |  \$$$$$$  |\$$$$$$  |      $$  /   \$$ |\$$$$$$  |$$ |  $$ |
    \__|   \______/  \______/       \__/     \__| \______/ \__|  \__|                                                                                                                                                                                                          
"""


lose ='''
 $$$$$$\                                           $$$$$$\                                 
$$  __$$\                                         $$  __$$\                                
$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
 \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|      
                                                                                           
                                                                                                                                                                                    
'''







number = []

for i in range(1,101):
    number.append(i)


print(logo)

num_chossed = random.choice(number)


easy_live = 10
hard_live = 5
game_over=False




def scr_cal(life):
    game_over = False
    life -= 1
    print(f"You have {life} attempts remaining to guess the number.")
    if life == 0:
        print(f"{lose}\nYou are out of moves")
        game_over = True
    return life, game_over





print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")



if level == "easy":
    print("You have 10 attempts remaining to guess the number.")
    while not game_over:
    
        user_input_1 = int(input("Make a guess: "))
        if user_input_1 == num_chossed:
            print(f"You got it! The answer was: {num_chossed}")
            game_over = True

        elif user_input_1 > num_chossed:
            print("Too High")
            easy_live, game_over = scr_cal(easy_live)
    
        else:
            print("Too Low")
            easy_live, game_over = scr_cal(easy_live)

if level == "hard":
    print("You have 5 attempts remaining to guess the number.")
    
    while not game_over:
        user_input_1 = int(input("Make a guess: "))
        if user_input_1 == num_chossed:
            print(f"{win}You got it! The answer was: {num_chossed}")
            game_over = True

        elif user_input_1 > num_chossed:
            print("Too High")
            hard_live, game_over = scr_cal(hard_live)
    
        else:
            print("Too Low")
            hard_live, game_over = scr_cal(hard_live)