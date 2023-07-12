def is_vowel(letter):
    vowel_letters = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
    return True if letter in vowel_letters else False


def vowels():
    # letters =
    letter_list = list(input('Введите буквы через пробел: ').split(' '))
    vowels_list = []
    consonants = []
    for letter in letter_list:
        if is_vowel(letter.lower()):
            vowels_list.append(letter)
        else:
            consonants.append(letter)
    print(f'Гласные: {", ".join(vowels_list)}')
    print()
    print(f'Соласные: {", ".join(consonants)}')


vowels()
