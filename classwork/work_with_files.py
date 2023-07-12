# import os
file = 'files/lesson.txt'


def find_word(path):
    counter = 0
    search_request = input('Введите слово, которое хотите найти: ')
    with open(path, mode='r', encoding='utf-8') as content:
        for index, line in enumerate(content.readlines(), 1):
            if search_request in line:
                print(f'Ваше слово "{search_request}" находится в тексте на строке №{index}')
                counter += 1
        if counter == 0:
            print('Такого слова в тексте нет!')


find_word(file)
