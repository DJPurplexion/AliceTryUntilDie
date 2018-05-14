# coding: utf-8
from __future__ import unicode_literals
import json
from random import choice

WAIT = 0
REPLY = 1


cities_data = json.load(open('big-city-data.json'))


# Функция для непосредственной обработки диалога.
def handle_dialog(request, response, user_storage):
    if request.is_new_session:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        city = choice(cities_data.keys())

        user_storage = {
            # 'suggests': [
            #     "Загадать город"
            # ]
            'city': city,
            'state': WAIT
        }

        # buttons, user_storage = get_suggests(user_storage)
        response.set_text('Привет! В какой стране находится город %s?' % city)
        # response.set_buttons(buttons)

        return response, user_storage

    if user_storage.get('state') == WAIT:
        # Обрабатываем ответ пользователя.
        if request.command.lower() in cities_data[user_storage['city']]:
            # Пользователь угадал.
            response.set_text('Правильно! Загадать новый?')

            buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": False
            }]
            response.set_buttons(buttons)
        else:
            response.set_text('Неправильно! Попробуй еще раз!')
    elif user_storage.get('state') == REPLY:
        if request.command.lower() == 'да':
            city = choice(cities_data.keys())
            user_storage = {
                'city': city,
                'state': WAIT
            }
            response.set_text('Привет! В какой стране находится город %s?' % city)
        elif request.command.lower() == 'нет':
            request.set_end_session(True)
        else:
            response.set_text('Алиса тобi не понимает :(')

    return response, user_storage


# Функция возвращает две подсказки для ответа.
def get_suggests(user_storage):
    # Выбираем две первые подсказки из массива.
    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in user_storage['suggests'][:2]
    ]

    # Убираем первую подсказку, чтобы подсказки менялись каждый раз.
    user_storage['suggests'] = user_storage['suggests'][1:]

    # Если осталась только одна подсказка, предлагаем подсказку
    # со ссылкой на Яндекс.Маркет.
    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text=слон",
            "hide": True
        })

    return suggests, user_storage
