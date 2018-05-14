# coding: utf-8
from __future__ import unicode_literals
import json, alice_static
from random import choice

WAIT = 0
REPLY = 1

cities_data = json.load(open('big-city-data.json'))


def format_new_question(city):
    question = choice(alice_static.questions)
    return question.format(city=city)


# Функция для непосредственной обработки диалога.
def handle_dialog(request, response, user_storage):
    if request.is_new_session:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        city = choice(list(cities_data.keys()))

        user_storage = {
            'city': city,
            'state': WAIT,
            'try': 0
        }

        response.set_text('Викторина началась!\n' + format_new_question(city))

        return response, user_storage

    if user_storage.get('state') == WAIT:
        # Обрабатываем ответ пользователя.
        if request.command.lower() == cities_data[user_storage['city']].lower():
            # Пользователь угадал.
            correct = choice(alice_static.answer_correct)
            response.set_text('{correct}\nЗагадать новый?'.format(correct=correct))

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
            user_storage['try'] += 1
            hint = cities_data[user_storage['city']]
            if user_storage['try'] == 3:
                hint = '\n\nПервая буква - %s' % hint[0]
            elif user_storage['try'] == 5:
                hint = '\n\nНачало - %s' % hint[:2]
            else:
                hint = ''
            incorrect = choice(alice_static.answer_incorrect)
            response.set_text('{incorrect}\nПопробуй еще раз!{hint}'.format(
                incorrect=incorrect,
                hint=hint
            ))

    elif user_storage.get('state') == REPLY:
        if request.command.lower() == 'да':
            city = choice(list(cities_data.keys()))
            user_storage = {
                'city': city,
                'state': WAIT,
                'try': 0
            }
            response.set_text(format_new_question(city))

        elif request.command.lower() == 'нет':
            response.set_end_session(True)
            goodbye = choice(alice_static.goodbye)
            response.set_text(goodbye)

        else:
            buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": True
            }]
            response.set_buttons(buttons)
            response.set_text('Выбери один из двух вариантов - Да или Нет')

    return response, user_storage
