from telebot import types, TeleBot
from db.engine import SessionLocal

from model import People
from question import Test
from result import get_result, create_final_message
from db.db_model import Result, UserInfo, LogChats



drawler = Test()


def handler(callback_text:str, message: types.Message, bot: TeleBot):
    '''Handling complete the test , redraw the new question and save result to db'''

    result = callback_text.split("_answer_")
    callback_text = result[0]

    if callback_text == '0':
        drawler.draw_hello_message(message, bot)
        if message.from_user.first_name:
            first_name = message.from_user.first_name
        else:
            first_name = "Скрыто"

        if message.from_user.last_name:
            last_name = message.from_user.last_name
        else:
            last_name = "Скрыто"
        full_name = f"{first_name} {last_name}"
        
        #save username to communicate
        UserInfo.add_user(message.chat.id, message.from_user.id,  \
                          message.from_user.username, full_name, SessionLocal())
        
        #Notification of start test 
        #for chat in LogChats.get_all(SessionLocal()):    
        #    bot.send_message(text=f"Пользователь @{message.from_user.username} начал прохождение теста", chat_id=chat.chat_id)
        
    if callback_text == '1': drawler.draw_first(message, bot)

    if callback_text == '2':

        answer = Result().get_result_by_question(message.message_id, message.chat.id, 2, SessionLocal())

        people = People()
        if len(answer) > 0:
            people.from_answer(answer[0].answer)


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
                Result().add_result(message.message_id, message.chat.id, int(callback_text) - 1, result[1], SessionLocal())

        drawler.draw_second(message, bot, people)
        Result.add_result(message.message_id, message.chat.id, 2, people.as_answer(), SessionLocal())
        return

    if callback_text == '3': drawler.draw_third(message, bot)
        
    if callback_text == '4': drawler.draw_fourth(message, bot)
    
    if callback_text == '5': drawler.draw_five(message, bot)
    
    if callback_text == '6': drawler.draw_six(message, bot)

    if callback_text == '7': drawler.draw_seven(message, bot)

    if callback_text == '8': drawler.draw_eight(message, bot)

    if callback_text == '9':
        if len(result) > 1:
            answer = result[1]
        else:
            answer = Result().get_result_by_question(message.message_id, message.chat.id, 6, SessionLocal())[0].answer
        drawler.draw_nine(message, bot, answer)

    if callback_text == '10':
        ans = Result().get_result_by_question(message.message_id, message.chat.id, 6, SessionLocal())
        drawler.draw_ten(message, bot, ans[0].answer)

    if callback_text == '11':
        ans = Result().get_result_by_question(message.message_id, message.chat.id, 6, SessionLocal())
        drawler.draw_eleven(message, bot, ans[0].answer)

    if callback_text == '12':
        selected_items = []
        question_num = 12
        ans = Result().get_result_by_question(message.message_id, message.chat.id, question_num, SessionLocal())
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
                Result.add_result(message.message_id, message.chat.id, question_num, "_".join(selected_items).strip('_'), SessionLocal())

            #FIXME Need to edit structure, cant save in main call, because next qeustion is multieselect
            else:
                Result().add_result(message.message_id, message.chat.id, int(callback_text) - 1, result[1], SessionLocal())

        drawler.draw_twelve(message, bot, selected_items)
        return

    if callback_text == '13':
        selected_items = []
        question_num = 13
        ans = Result().get_result_by_question(message.message_id, message.chat.id, question_num, SessionLocal())
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
                Result.add_result(message.message_id, message.chat.id, question_num, "_".join(selected_items).strip('_'), SessionLocal())
        drawler.draw_thirteen(message, bot, selected_items)
        return
    
    #TODO result
    if callback_text == '14':
        res = Result().get_all(message.message_id, message.chat.id, SessionLocal())
        img_name = get_result(res)
        drawler.draw_fourthteen(message, bot, img_name)
        
        user = UserInfo.get_user_by_chat_id(message.chat.id, SessionLocal())
        if user.username:
            username = user.username
        else:
            username = ""
        if user.name:
            fullname = user.name
        else:
            fullname = ""
        log_message = create_final_message(res, fullname, username)
        # TODO create result form and send to log chat
        for chat in LogChats.get_all(SessionLocal()):    
            bot.send_photo(caption=log_message, chat_id=chat.chat_id, photo=open(f'results_images/{img_name}', 'rb'))
        

    if len(result) > 1 and \
    callback_text != '3' and \
    callback_text != '13' and \
    callback_text != '14':
        answer = result[1]
        Result().add_result(message.message_id, message.chat.id, int(callback_text) - 1, answer, SessionLocal())