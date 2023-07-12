import datetime


def days_from_now():
    today = datetime.date.today()
    user_input = input('Введите дату в формате "ГГГГ-ММ-ДД": ')
    user_date = datetime.date.fromisoformat(user_input)
    days_left = user_date - today
    if int(days_left.days) > 0:
        print(f'До {user_date} осталось дней: {days_left.days}')
    else:
        print(f'С даты {user_date} прошло дней: {abs(days_left.days)}')


days_from_now()
