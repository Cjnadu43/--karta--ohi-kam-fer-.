import random
from kalajack_art import logo
print(logo)
def  deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []

computer_cards = []
for x in range(0,2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
def calculate_score (cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards > 21):
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, you genuinly are a failiure and you suck 😱"
    elif u_score == 0:
        return "Win with a Blackjack. Singh tu hega aura farmer 😎"
    elif u_score > 21:
        return "You went over. You lose. Bhor koina Bhor  😭"
    elif c_score > 21:
        return "Opponent went over. You win. You lucky truck driver 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose. Bhor Bhor ki hi he mardu! 😤"





