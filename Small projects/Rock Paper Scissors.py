from random import randint
def Rock_Paper_Scissors(Rounds):
    i = 0
    counter1 = 0
    counter2 = 0
    while i < Rounds:
        Hand = input('Choose Rock, Paper or Scissors: ')
        while Hand != 'Rock' and Hand != 'Paper' and Hand != 'Scissors': Hand = input('Try again, choose rock paper or scissors: ')
        Opp = ''
        Randomizer = randint(1, 3)  # 1 equals rock, 2 equals paper and 3 equals scissors
        if Randomizer == 1: Opp += 'Rock'

        elif Randomizer == 2: Opp += 'Paper'

        else: Opp += 'Scissors'

        if Hand == Opp:
            counter1 += 1
            counter2 += 1
            print('\nDraw', Hand.lower(), 'equals', Opp.lower(),  '\ncurrent score: ', counter1, '-', counter2, '\n')

        elif Hand == 'Rock' and Opp == 'Paper':
            counter2 += 1
            print('\nYou lose against paper \nCurrent score: ', counter1, '-', counter2, '\n')

        elif Hand == 'Rock' and Opp == 'Scissors':
            counter1 += 1
            print('\nYou win against scissors \nCurrent score: ', counter1, '-', counter2, '\n')

        elif Hand == 'Paper' and Opp == 'Rock':
            counter1 += 1
            print('\nYou win against rock \nCurrent score: ', counter1, '-', counter2, '\n')

        elif Hand == 'Paper' and Opp == 'Scissors':
            counter2 += 1
            print('\nYou lose against scissors \nCurrent score: ', counter1, '-', counter2, '\n')

        elif Hand == 'Scissors' and Opp == 'Rock':
            counter2 += 1
            print('\nYou lose against rock \nCurrent score: ', counter1, '-', counter2, '\n')

        elif Hand == 'Scissors' and Opp == 'Paper':
            counter1 += 1
            print('\nYou win against paper \nCurrent score: ', counter1, '-', counter2, '\n')

        i += 1

    if counter1 > counter2 and counter1-counter2 == 1: print('You have won with', counter1-counter2, 'more point')

    elif counter1 > counter2: print('You have won with', counter1 - counter2, 'more points')

    elif counter1 < counter2 and counter2-counter1 == 1: print('You have lost with', counter1 - counter2, 'less point')

    elif counter1 < counter2: print('You have lost with', counter1 - counter2, 'less points')

    else: print('The match is a draw')

Rounds = int(input('How many rounds? : '))

Rock_Paper_Scissors(Rounds)



