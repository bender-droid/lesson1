import random
import time


def magic_eight_ball():
    answers = [
        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Определённо - да",
        "Можешь быть уверен в этом",
        "Мне кажется — да",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят — да",
        "Да",
        "Пока не ясно, попробуй снова",
        "Спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять",
        "Даже не думай",
        "Мой ответ — нет",
        "По моим данным — нет",
        "Перспективы не очень хорошие",
        "Весьма сомнительно"
    ]
    print('Приветствую вас! Можете задать мне любой вопрос о будущем, \n'
          'а я на него отвечу со стопроцентной гарантией... и \n'
          'стопроцентной погрешностью :-). Задайте свой вопрос \n'
          'или напишите "Пока", чтобы попрощаться!')
    print()
    while True:
        user_answer = input('Введите ваш вопрос: ')
        while not user_answer:
            print()
            print('Я хоть и колдун, но мысли читать не умею! \n'
                  'Озвучьте вопрос, пожалуйста!')
            user_answer = input('Введите ваш вопрос: ')
        print()
        if user_answer.lower() == "пока":
            print('Хорошего дня!')
            break
        else:
            print('Думаю...')
            time.sleep(2)
            print(random.choice(answers))
            print()


magic_eight_ball()