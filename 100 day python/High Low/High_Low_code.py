import random
from art import logo, vs
from Data import data

def format_data(account):
    acc_name = account["name"]
    acc_descr = account["description"]
    acc_location = account["country"]
    
    return f"{acc_name}, a {acc_descr}, from {acc_location}"

def check_answer(user_gess , a_follower, b_follower):
    if a_follower>b_follower:
        return user_gess == "a"
    else:
        return user_gess =="b"


print(logo)
score = 0
account_b = random.choice(data)


game_should_continue =True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    
    


    guess = input("Who has greater follower").lower
    
    print("\n"*50)
    print(logo)


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    
    is_ass=check_answer(guess, a_follower_count, b_follower_count)
    if is_ass:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False

