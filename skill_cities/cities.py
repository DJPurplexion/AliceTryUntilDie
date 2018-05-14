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

        city = choice(list(cities_data.keys()))

        user_storage = {
            # 'suggests': [
            #     "Загадать город"
            # ]
            'city': city,
            'state': WAIT
        }

        # buttons, user_storage = get_suggests(user_storage)
        # FIXME
        response.set_text('Привет! В какой стране находится город %s? (%s)' % (city, cities_data[city]))
        # response.set_buttons(buttons)

        return response, user_storage

    if user_storage.get('state') == WAIT:
        # Обрабатываем ответ пользователя.
        if request.command.lower() in cities_data[user_storage['city']].lower():
            # Пользователь угадал.
            response.set_text('Правильно! Загадать новый?')

            buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": True
            }]
            response.set_buttons(buttons)
            user_storage['state'] = REPLY
        else:
            response.set_text('Неправильно! Попробуй еще раз!')
    elif user_storage.get('state') == REPLY:
        if request.command.lower() == 'да':
            city = choice(list(cities_data.keys()))
            user_storage = {
                'city': city,
                'state': WAIT
            }
            # FIXME
            response.set_text('В какой стране находится город %s? (%s)' % (city, cities_data[city]))
        elif request.command.lower() == 'нет':
            response.set_end_session(True)
            response.set_text('Пока :)')
        else:
            buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": True
            }]
            response.set_buttons(buttons)
            response.set_text('Выбери один из двух вариантов - Да / Нет')
    return response, user_storage

