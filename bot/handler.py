from question import Test
from model import People


drawler = Test()

def handler(callback_text:str, message, bot):

    result = callback_text.split("_answer_")
    callback_text = result[0]
    if len(result) > 1:
        answer = result[1]
        print(answer)

    if callback_text == 'quiz_started':
        drawler.draw_first(message, bot)
        
    if callback_text == 'first_completed':
        people = People(bb=5)
        drawler.draw_second(message, bot, people)
    elif callback_text == 'to_first':
        
        drawler.draw_first(message, bot)

    if callback_text == 'second_completed':
        drawler.draw_third(message, bot)
    elif callback_text == 'to_second':
        people = People(bb=5)
        drawler.draw_second(message, bot, people)
    
    if callback_text == 'third_completed':
        drawler.draw_fourth(message, bot)
    elif callback_text == 'to_third':
        drawler.draw_third(message, bot)
    
    if callback_text == 'fourth_completed':
        drawler.draw_five(message, bot)
    elif callback_text == 'to_fourth':
        drawler.draw_fourth(message, bot)
    
    if callback_text == 'five_completed':
        drawler.draw_six(message, bot)
    elif callback_text == 'to_five':
        drawler.draw_five(message, bot)