import random

print("Witaj w grze wisielec, słowo do odgadnięcia z dziedziny ZWIERZĘTA w domu")

words_game = ['kot', 'pies', 'rybka', 'papuga', 'chomik']
words_ask = []
words_list = []
game_chances = 6


def generate(words_to_generate):
    guess = random.choice(words_to_generate)
    words = [guess]
    for i in range(len(words[0])):
        words_list.append(words[0][i])
    for i in range(len(words[0])):
        words_ask.append('-')
    return guess

secret_word = generate(words_game)

def game(guess_word, game_chances):
    print('Długość słowa', len(words_ask))
    while game_chances > 0:
        letter = (input(f'Podaj literę lub słowo aby odgadnąć hasło, masz {game_chances} szans: '))
        letter = letter.lower()
        game_chances -= 1
        if letter == guess_word:
            print('ZGADŁEŚ HASŁO PO SŁOWIE GRATULACJE, wylosowane hasło to:', guess_word)
            break

        else:
            for x in range(len(words_list)):
                if words_list[x] == letter:
                     words_ask[x] = letter

            print(words_ask)
            if words_ask == words_list:
                print('Hasło odgadnięte, wylosowane hasło to:', guess_word)
                break

            if game_chances == 0:
                print('Koniec gry, skończyły się Tobie szanse, hasło to :', guess_word)


game(secret_word, game_chances)

