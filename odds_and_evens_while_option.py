from random import randint

random_start = randint(1, 10)
random_step = randint(1, 5)
random_end = randint(20, 100)
random_list = [x for x in range(random_start, random_end, random_step)]
evens = []
odds = []
list_length = len(random_list)
counter = 0

while list_length > 0:
    number = random_list[counter]
    if number % 2 == 0:
        evens.append(str(number))
        counter += 1
    else:
        odds.append(str(number))
        counter += 1
    list_length -= 1

print(f'Список чисел: {", ".join(map(str, random_list))}')
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
