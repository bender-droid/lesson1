from random import randint


random_start = randint(1, 10)
random_step = randint(1, 5)
random_end = randint(20, 100)
random_list = [x for x in range(random_start, random_end, random_step)]

# collection = input('Введите числа: ')

def evens_and_odds(*collection):
    evens = []
    odds = []

    for number in collection:
        if number % 2 == 0:
            evens.append(str(number))
        else:
            odds.append(str(number))

    print(f'Список чисел: {", ".join(map (str, collection))}')
    if odds and evens:
        print()
        print(f'Четные числа: {", ".join(evens)}')
        print(f'Нечетные числа: {", ".join(odds)}')
    elif odds and not evens:
        print()
        print(f'Четных чисел нет!')
        print(f'Нечетные числа: {", ".join(odds)}')
    elif evens and not odds:
        print()
        print(f'Четные числа: {", ".join(evens)}')
        print(f'Нечетных чисел нет!')


evens_and_odds(4, 5, 4786, 23165798, 98763251465, 22057)
