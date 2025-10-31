import random

logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""




def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def cal_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    


def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    user_scr = -1
    comp_scr = -1

    is_game_over=False


    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:
        user_scr = cal_score(user_card)
        comp_scr = cal_score(computer_card)
        print(f"User card: {user_card}    User score: {user_scr}")
        print(f"Computer First Card: {computer_card[0]}")


        if user_scr == 0 or comp_scr == 0 or user_scr > 21:
            is_game_over = True

        else:
            user_choice =input("If you want to continue press 'y' ot to end press 'n'")
            if user_choice == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while comp_scr != 0 and comp_scr < 17:
        computer_card.append(deal_card())
        comp_scr = cal_score(computer_card)


    

    print(f"Your final hand: {user_card}, final score: {user_scr}")
    print(f"Computer's final hand: {computer_card}, final score: {comp_scr}")
    print(compare(user_scr, comp_scr))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
