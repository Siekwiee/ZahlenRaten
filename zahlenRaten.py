import random

solution = random.randint(1,100)

print('Eine zufällige Zahl von 1 bis 100 wurde generiert, versuche doch mal sie zu erraten :-)')

guess = int()

while guess != solution:
    guess = int(input())
    if guess == solution:
        print(f'GLÜCKWUNSCH DU HAST DIE RICHTIGE ZAHL ERRATEN')
        print(f'Die Zahl war: {guess}')
        break
    if guess < solution:
        print(f'Die gesuchte Zahl ist größer versuche es doch noch einmal')
        continue
    else:
        print(f'Die gesuchte Zahl ist kleiner versuche es doch noch einmal')
        continue
