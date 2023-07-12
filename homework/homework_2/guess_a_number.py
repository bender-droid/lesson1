from random import randint


def guess_number():
    quiz_number = randint(1, 10)
    try_count = 3
    while True:
        print('Приветствую! Вы не знаете меня, но я знаю вас. \n'
              'Я хочу сыграть с вами в игру. \n'
              'Я загадал число от 1 до 10. У вас будет всего \n'
              'три попытки, чтобы угадать. Жить или умереть - решать вам!')
        while try_count > 0:
            print()
            user_guess = int(input('Ваша догадка: '))
            if user_guess == quiz_number:
                print('Вы угадали! Большинство людей \n'
                      'в нашем мире совершенно не ценят жизнь. \n'
                      'Но только не вы, и только не теперь...')
                return None
            elif abs(quiz_number - user_guess) > 2:
                try_count -= 1
                print(f'Холодно... Количество оставшихся попыток: {try_count}')
            elif abs(quiz_number - user_guess) <= 2:
                try_count -= 1
                print(f'Тепло... Количество оставшихся попыток: {try_count}')
        print(f'Я загадывал число {quiz_number}! Игра окончена!')
        print()
        another_try = input('Сыграем еще? (y/n): ')
        print()
        if another_try == 'n':
            print('Игра окончена!')
            break
        else:
            try_count = 3


guess_number()
