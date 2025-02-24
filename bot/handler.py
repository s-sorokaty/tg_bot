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

        answer = Result().get_result_by_question(message.message_id, message.chat.id, 2, SessionLocal())

        people = People()
        if len(answer) > 0:
            people.from_answer(answer[0].answer)

        #answer = Result().get_result_by_question(message.message_id, message.chat.id, 1, SessionLocal())

        #if len(answer) > 0:
        #    first_answer = answer[0].answer
        #    if int(first_answer)<3 and people.sb == 0:
        #        people.sb = "1"
        #    if int(first_answer)>=3 and people.sg == 0:
        #        people.sg = "1"

        #    print(first_answer, people.sb)
        #    print(first_answer, people.sg)

        if len(result) > 1:
            selected = result[1].split("_selected_")
            if len(selected) > 1:
                number, action = selected[1].split("_")
                if action == "+":
                    people.increce_by_id(int(number))
                else:
                    people.decrece_by_id(int(number))

            #FIXME Need to edit structure, cant save in main call, because next qeustion is multieselect
            else:
                if int(result[1])<=3 and int(people.sb) == 0:
                    people.sb = "1"
                if int(result[1])>3 and int(people.sg) == 0:
                    people.sg = "1"
                
                Result().add_result(message.message_id, message.chat.id, int(callback_text) - 1, result[1], SessionLocal())

        drawler.draw_second(message, bot, people)
        Result.add_result(message.message_id, message.chat.id, 2, people.as_answer(), SessionLocal())
        return
    
    if callback_text == '3':
        drawler.draw_third(message, bot)
        return
    
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

    if callback_text == '10':
        selected_items = []
        ans = Result().get_result_by_question(message.message_id, message.chat.id, 10, SessionLocal())
        if len(ans) > 0:
            for item in ans[0].answer.split('_'):
                selected_items.append(item)
        
        if len(result) > 1:
            selected = result[1].split("_selected_")
            if len(selected) > 1:
                if selected[1] in selected_items:
                    selected_items.remove(selected[1])
                else:
                    selected_items.append(selected[1])
                Result.add_result(message.message_id, message.chat.id, 10, "_".join(selected_items).strip('_'), SessionLocal())

            #FIXME Need to edit structure, cant save in main call, because next qeustion is multieselect
            else:
                Result().add_result(message.message_id, message.chat.id, int(callback_text) - 1, result[1], SessionLocal())

        drawler.draw_ten(message, bot, selected_items)
        return

    if callback_text == '11':
        selected_items = []
        ans = Result().get_result_by_question(message.message_id, message.chat.id, 11, SessionLocal())
        if len(ans) > 0:
            for item in ans[0].answer.split('_'):
                selected_items.append(item)
        
        if len(result) > 1:
            selected = result[1].split("_selected_")
            if len(selected) > 1:
                if selected[1] in selected_items:
                    selected_items.remove(selected[1])
                else:
                    selected_items.append(selected[1])
                Result.add_result(message.message_id, message.chat.id, 11, "_".join(selected_items).strip('_'), SessionLocal())
        drawler.draw_eleven(message, bot, selected_items)
        return
    
    #TODO result
    if callback_text == '12':
        res = Result().get_all(message.message_id, message.chat.id, SessionLocal())
        drawler.draw_result(message, bot, res) 


    if len(result) > 1 and \
    callback_text != '3' and \
    callback_text != '11' and \
    callback_text != '12':
            
        answer = result[1]
        Result().add_result(message.message_id, message.chat.id, int(callback_text) - 1, answer, SessionLocal())