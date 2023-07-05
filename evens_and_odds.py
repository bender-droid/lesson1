from random import randint

random_start = randint(1, 10)
random_step = randint(1, 5)
random_end = randint(20, 100)
random_list = [x for x in range(random_start, random_end, random_step)]
evens = []
odds = []

for number in random_list:
    if number % 2 == 0:
        evens.append(str(number))
    else:
        odds.append(str(number))

if odds and evens:
    print(f'Список чисел: {random_list}')
    print()
    print(f'Четные числа: {", ".join(evens)}')
    print()
    print(f'Нечетные числа: {", ".join(odds)}')
elif odds and not evens:
    print(f'Список чисел: {random_list}')
    print()
    print(f'Четных чисел нет!')
    print()
    print(f'Нечетные числа: {", ".join(odds)}')
elif evens and not odds:
    print(f'Список чисел: {random_list}')
    print()
    print(f'Четные числа: {", ".join(evens)}')
    print()
    print(f'Нечетных чисел нет!')
