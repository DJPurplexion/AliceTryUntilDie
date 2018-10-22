from __future__ import unicode_literals
import json, alice_static
from random import choice
def format_new_question(quest):
    question = choice(alice_static.questions)
    return question.format(quest=quest)
"""
Установить requests
"""
def timeynotwimey()
            user_storage['try'] += 1
            timeup = choice(alice_static.answer_timeup)
            right_answer=choice(alice_static.right_answer)
            real_answer=quest_data[user_storage['answer']]
            again=choice(alice_static.again)
            response.set_text('{timeup}\n{right_answer}{real_answer}\n{again}'.format(
                timeup=timeup,
                right_answer=right_answer
                real_answer=real_answer
                again=again
            ))
            buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": True
            }]
            response.set_buttons(buttons)
            #Выводим кнопочки
            user_storage['state'] = REPLY
            #Меняем состояние пользователя
def handle_dialog(request, response, user_storage):
    if request.is_new_session:
          # Это новый пользователь.
          # Инициализируем сессию и поприветствуем его.

          quest = choice(list(quest_data.keys()))

          user_storage = {
              'quest': quest,
              'team': team,
              'state': STOP,
              #STOP-вопрос не задан Wait-ожидается ответ Reply - ответ получен
              'wins': 0,
              'tries':0
         }

          response.set_text('Вы готовы к викторине?')

          return response, user_storage
    """
    if user_storage.get('state') == STOP:
      newquest = choice(alice_static.newquest)
      response.set_text('{newquest}\n{right_answer}{real_answer}\n{again}'.format(
          newquest=newquest,
            ))
      buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": True
            }]
            response.set_buttons(buttons)
      if request.command.lower() == 'да':
          quest = choice(list(quest_data.keys()))
          user_storage = {
              'quest': quest,
              'team': user_storage['team'],
              'state': WAIT,
              'wins': user_storage['wins'],
              'tries': user_storage ['tries']
            }
          response.set_text(format_new_question(quest))
      elif request.command.lower() == 'нет':
          response.set_text("Желаете выйти?")
          buttons = [{
              "title": "Да",
              "hide": True
          }, {
              "title": "Нет",
              "hide": True
          }]
            response.set_buttons(buttons)
          if request.command.lower() == 'нет':
            ВСТАВИТЬ ДЕЙСТВИЕ
          elif request.command.lower() == 'да':
            ВСТАВИТЬ ДЕЙСТВИЕ выхода
          else:
            response.set_buttons(buttons)
            response.set_text ('Извините я не понимаю, вы хотите выйти?')
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

    Вставить задавание первого вопроса и переделать это
    """"
    if user_storage.get('state') == WAIT:
        # Обрабатываем ответ пользователя.
        timeywimey = Timer(30.0, timeynotwimey)
        t.start()
        if request.command.lower() == quest_data[user_storage['answer']].lower():
            # Пользователь угадал.
            user_storage['wins'] += 1
            user_storage['try'] +=1
            #Добавляем победу и попытку
            correct = choice(alice_static.answer_correct)
            again=choice(alice_static.again)
            #Выбираем реплику для поздравления

            response.set_text('{correct}\n{again}'.format(
                correct=correct
                again=again
            ))
            #Поздравляем и спрашиваем хочет ли пользователь сыграть ещё раз

            buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": True
            }]
            response.set_buttons(buttons)
            #Выводим кнопочки
            user_storage['state'] = REPLY
            #Меняем состояние пользователя
        else:
            user_storage['try'] += 1
            incorrect = choice(alice_static.answer_incorrect)
            right_answer=choice(alice_static.right_answer)
            real_answer=quest_data[user_storage['answer']]
            again=choice(alice_static.again)
            response.set_text('{incorrect}\n{right_answer}{real_answer}\n{again}'.format(
                incorrect=incorrect,
                right_answer=right_answer
                real_answer=real_answer
                again=again
            ))
            buttons = [{
                "title": "Да",
                "hide": True
            }, {
                "title": "Нет",
                "hide": True
            }]
            response.set_buttons(buttons)
            #Выводим кнопочки
            user_storage['state'] = REPLY
            #Меняем состояние пользователя
    """
    Разделитель для лучшей видимости
    """
    elif user_storage.get('state') == REPLY:
        if request.command.lower() == 'да':
            quest = choice(list(quest_data.keys()))
            user_storage = {
                'quest': quest,
                'team': user_storage['team'],
                'state': WAIT,
                'wins': user_storage['wins'],
                'tries': user_storage ['tries']
            }
            response.set_text(format_new_question(quest))

        elif request.command.lower() == 'нет':
             user_storage['state'] = STOP
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