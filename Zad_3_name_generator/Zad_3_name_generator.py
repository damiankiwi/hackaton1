import random
a = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z']
b = ['a', 'e', 'i', 'o', 'u', 'y']
new_nick = []
nickname = ["Śmiały", "Dumny", "Zuchwały", "Mocny", "Lew", "Niedźwiedź", "Żelazny", "Żelaznoboki", "Żelazne Ramię", "Surowy", "Srogi", "Groźny", "Spokojny", "Wesoły", "Uśmiechnięty", "Szczęśliwy", "Jagnię", "Milczek", "Cichy", "Pamiętny", "Krótki", "Mały", "Łokietek", "Łysy", "Ryży", "Gęba", "Krzywousty", "Krzywobrody", "Pryszczaty", "Gruby", "Tłusty", "Garbaty", "Krzywy", "Kulawy", "Plątonogi", "Krótkonogi", "Laskonogi"]
number_list = ["I", "II", "III", "IV", "V", "VI"]


def generate_name(n):
    new_name = [first_letter]
    for i in range(n):
        if i % 2 == 0:
            new_name.append(random.choice(a))
        else:
            new_name.append(random.choice(b))
    nick = random.choice(nickname)
    number = random.choice(number_list)
    name = ''.join(new_name).capitalize() + ' ' + number + ' ' + nick
    return name


print("Generator imienia dla Wojownika RPG")
first_letter = input("Podaj pierwszą literę imienia: ")
name_length = int(input("Podaj ile liter ma zawierać imię: "))
rpg_name = generate_name(name_length)

print(rpg_name)