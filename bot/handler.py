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

    if callback_text == '1':
        drawler.draw_first(message, bot)
        
    if callback_text == '2':
        people = People(bb=5)
        drawler.draw_second(message, bot, people)

    if callback_text == '3':
        drawler.draw_third(message, bot)
    
    if callback_text == '4':
        drawler.draw_fourth(message, bot)

    if callback_text == '5':
        drawler.draw_five(message, bot)

    if callback_text == '6':
        drawler.draw_six(message, bot)

    if callback_text == '7':
        if len(result) > 1:
            answer = result[1]
        else:
            answer = Result().get_result_by_question(message.message_id, message.chat.id, 6, SessionLocal())[0].answer
        drawler.draw_seven(message, bot, answer)

    if callback_text == '8':
        ans = Result().get_result_by_question(message.message_id, message.chat.id, 6, SessionLocal())
        drawler.draw_eight(message, bot, ans[0].answer)

    if callback_text == '9':
        ans = Result().get_result_by_question(message.message_id, message.chat.id, 6, SessionLocal())
        drawler.draw_nine(message, bot, ans[0].answer)

    #if callback_text == '9':
    #    res = Result().get_all_db_model(message.message_id, message.chat.id, SessionLocal())
    #    drawler.draw_result(message, bot, res) 


    if len(result) > 1:
        answer = result[1]
        Result().add_result(message.message_id, message.chat.id, int(callback_text) - 1, answer, SessionLocal())