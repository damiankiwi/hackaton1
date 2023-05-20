import random
import time

player_cards = []
computer_cards = []
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

deck = cards*4

player_cards = random.sample(deck, 10)
print('Wylosowane karty dla gracza:', player_cards)

computer_cards = random.sample(deck, 10)
print('Wylosowane karty dla komputera:', computer_cards)

player = 0
computer = 0

i = 0
while i < 10:
    print('RUNDA', i+1,':', player_cards[i], 'vs', computer_cards[i])

    if player_cards[i] == computer_cards[i]:
        print('---Remis---')
        time.sleep(1)
        i += 1

    elif player_cards[i] > computer_cards[i]:
        print('Wygral gracz')
        time.sleep(1)
        player += 1
        i += 1

    elif player_cards[i] < computer_cards[i]:
        print('Wygral komputer')
        time.sleep(1)
        computer += 1
        i += 1

print('Wynik gry: gracz:',player, 'komputer:',computer)