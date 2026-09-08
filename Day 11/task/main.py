import random, art
from idlelib.run import MyHandler
from struct import calcsize

game = input('Do you want to play a game? (y/n): ')
if game == 'y':
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_card = []
    system_card = []
    continue_game = True
    i=0
    while i<2:
        system_card.append(random.choice(cards))
        print(system_card)
        cards.remove(system_card[-1])
        my_card.append(random.choice(cards))
        cards.remove(my_card[-1])
        i += 1

    def summation(card):
        summation = 0
        for key in card:
            summation += key
        return summation

    my_summation = summation(my_card)
    system_summation = 0
    def calculate_score(my_summation, system_summation):
        if my_summation < system_summation <= 21:
            print('System won!')
        elif 21>= my_summation > system_summation:
            print('You won!')
        elif system_summation > 21:
            print('You won!')
        elif my_summation > 21:
            print('System won!')

    print(f'Your cards: {my_card}, current score: {my_summation}')
    print(f'Computers first card: {system_card[0]}')

    yes_or_no = input('Type y to get another card, or n to pass.')
    if yes_or_no == 'n':
        continue_game = False
        print(f'Your final hand: {my_card}, final score: {my_summation}')
        system_card.append(random.choice(cards))
        system_summation = summation(system_card)
        print(f'Computers final hand: {system_card}, final score: {system_summation}')
        calculate_score(my_summation, system_summation)
    else:
        my_card.append(random.choice(cards))
        cards.remove(my_card[-1])
        my_summation = summation(my_card)
        system_summation = summation(system_card)
        print(f'Your cards: {my_card}, current score: {my_summation}')
        print(f'Computers final hand: {system_card}, final score: {system_summation}')
        calculate_score(my_summation, system_summation)
