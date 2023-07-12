def month_to_days():
    thirty_days = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
    thirtyone_days = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
    user_input = input('Введите названия месяца и узнайте сколько в нем дней: ')
    if user_input.lower() in thirty_days:
        print(f'В месяце {user_input} ровно 30 дней')
    elif user_input.lower() in thirtyone_days:
        print(f'В месяце {user_input} ровно 31 день')
    elif user_input.lower() == 'февраль':
        print(f'В месяце {user_input} чаще всего 28 дней, но раз в 4 года в нем 29 дней')
    else:
        print('Нет такого месяца')


month_to_days()
