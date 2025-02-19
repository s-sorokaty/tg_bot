from question import Test
from model import People
from db.db_model import Result
from telebot import types, TeleBot
from db.engine import SessionLocal
drawler = Test()


def handler(callback_text:str, message: types.Message, bot: TeleBot):
    '''Handling complete the test , redraw the new question and save result to db'''

    result = callback_text.split("_answer_")
    callback_text = result[0]
    if len(result) > 1:
        answer = result[1]

    if callback_text == 'quiz_started':
        drawler.draw_first(message, bot)
        
    if callback_text == 'first_completed':
        people = People(bb=5)
        drawler.draw_second(message, bot, people)
        Result().add_result(message.message_id, message.chat.id, 1, answer, SessionLocal())
    elif callback_text == 'to_first':
        drawler.draw_first(message, bot)

    if callback_text == 'second_completed':
        drawler.draw_third(message, bot)
        #Result().add_result(message.message_id, message.chat.id, 2, answer, SessionLocal())
    elif callback_text == 'to_second':
        people = People(bb=5)
        drawler.draw_second(message, bot, people)
    
    if callback_text == 'third_completed':
        drawler.draw_fourth(message, bot)
        Result().add_result(message.message_id, message.chat.id, 3, answer, SessionLocal())
    elif callback_text == 'to_third':
        drawler.draw_third(message, bot)
    
    if callback_text == 'fourth_completed':
        drawler.draw_five(message, bot)
        Result().add_result(message.message_id, message.chat.id, 4, answer, SessionLocal())
    elif callback_text == 'to_fourth':
        drawler.draw_fourth(message, bot)
    
    if callback_text == 'five_completed':
        drawler.draw_six(message, bot)
        Result().add_result(message.message_id, message.chat.id, 5, answer, SessionLocal())
    elif callback_text == 'to_five':
        drawler.draw_five(message, bot)
    
    if callback_text == 'six_completed':
        drawler.draw_seven(message, bot)
        Result().add_result(message.message_id, message.chat.id, 6, answer, SessionLocal())
    elif callback_text == 'to_six':
        drawler.draw_six(message, bot)