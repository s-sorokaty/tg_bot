from telebot import types, TeleBot

import messages_text
from model import People

class Result():
    action = None
    first_result = None
    second_result = None
    third_result = None


class Test():
    first_result = None
    second_result = None
    third_result = None

    @staticmethod
    def draw_hello_message(message :types.Message, bot: TeleBot):
        callback_next = "1"
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Старт', callback_data=f"{callback_next}")
        markup.add(btn1)

        bot.send_photo(chat_id=message.chat.id, photo=open('images/placeholder.png', 'rb'), caption=messages_text.hello_message, reply_markup=markup)
        
        #message = bot.send_message(message.from_user.id, hello_message, reply_markup = markup)


    def draw_first(self, message :types.Message, bot: TeleBot):
        callback_next = "2"
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Мужчина, 16-25 лет', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='Мужчина, 26-45 лет', callback_data=f"{callback_next}_answer_2") 
        btn3 = types.InlineKeyboardButton(text='Мужчина, 45+ лет', callback_data=f"{callback_next}_answer_3")
        btn4 = types.InlineKeyboardButton(text='Женщина, 16-25 лет', callback_data=f"{callback_next}_answer_4")
        btn5 = types.InlineKeyboardButton(text='Женщина, 26-45 лет', callback_data=f"{callback_next}_answer_5")
        btn6 = types.InlineKeyboardButton(text='Женщина, 45+ лет', callback_data=f"{callback_next}_answer_6")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        new_photo = types.InputMediaPhoto(open('images/first.png', 'rb'), caption="Намекни нам на свой пол и возраст :)")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)
        
        #bot.edit_message_caption("Намекни нам на свой пол и возраст :)", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        

    @staticmethod
    def draw_second(message :types.Message, bot: TeleBot, people: People):
        callback_next = "3"
        callback_select = "2"
        callback_back = "1"

        labels = ["Младенец", "Ребенок", "Подросток", "Партнер", "Родитель"]
        
        markup = types.InlineKeyboardMarkup(row_width=1)

        for i in range(0,5):
            btn1 = types.InlineKeyboardButton(text=f'{labels[i]}, М: {people.as_list()[i*2]}', callback_data=f"{callback_select}_answer_{i}_selected_{i*2}_+")
            btn1dc = types.InlineKeyboardButton(text=f'Сбросить', callback_data=f"{callback_select}_answer_{i}_selected_{i*2}_-")
            if int(people.as_list()[i*2]) != 0:
                markup.row(btn1, btn1dc)
            else:
                markup.row(btn1)

            btn2 = types.InlineKeyboardButton(text=f'{labels[i]}, Ж: {people.as_list()[i*2+1]}', callback_data=f"{callback_select}_answer_{i}_selected_{i*2+1}_+")
            btn2dc = types.InlineKeyboardButton(text=f'Сбросить', callback_data=f"{callback_select}_answer_{i}_selected_{i*2+1}_-")
            if int(people.as_list()[i*2+1]) != 0:
                markup.row(btn2, btn2dc)
            else:
                markup.row(btn2)


        
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)
        btncompleted = types.InlineKeyboardButton(text=messages_text.next_button, callback_data=callback_next)
        markup.add(btncompleted, btnback)

        new_photo = types.InputMediaPhoto(open('images/second.png', 'rb'), caption="Кто живет с тобой?")
        bot.edit_message_media(media=new_photo, message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        


    @staticmethod
    def draw_third(message :types.Message, bot: TeleBot):
        callback_next = "4"
        callback_back = "2"

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Да, регулярно! Гостеприимство мое второе имя', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='Иногда Есть люди, двери для которых всегда открыты', callback_data=f"{callback_next}_answer_2")
        btn3 = types.InlineKeyboardButton(text='Нет, никогда! Мой дом - моя крепость, в крайнем случае переночуют в гостиной', callback_data=f"{callback_next}_answer_3")
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)

        markup.add(btn1, btn2, btn3, btnback)
        new_photo = types.InputMediaPhoto(open('images/third.jpg', 'rb'), caption="Бывает ли, что у тебя остаётся ночевать кто-то из близких?")
        bot.edit_message_media(media=new_photo, message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        
        #bot.edit_message_text("Бывает ли, что у тебя остаётся ночевать кто-то из близких?", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        

    @staticmethod
    def draw_fourth(message :types.Message, bot: TeleBot):
        callback_next = "5"
        callback_back = "3"

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Один И этот человек мечтает о домашнем офисе', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='Два Пандемия, что ты хочешь', callback_data=f"{callback_next}_answer_2")
        btn3 = types.InlineKeyboardButton(text='Ни одного Квартира для жизни, а не для работы', callback_data=f"{callback_next}_answer_3")
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)

        markup.add(btn1, btn2, btn3, btnback)
        
        new_photo = types.InputMediaPhoto(open('images/thourth.jpg', 'rb'), caption="Сколько человек работают из дома?")
        bot.edit_message_media(media=new_photo, message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        
        
        #bot.edit_message_text("Сколько человек работают из дома?", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        

    @staticmethod
    def draw_five(message :types.Message, bot: TeleBot):
        callback_next = "6"
        callback_back = "4"

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='В специальной комнате Мне спокойнее, когда все под рукой', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='Никакой возни в квартире Буду сдавать стирку управляющей компании!', callback_data=f"{callback_next}_answer_2")
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)

        markup.add(btn1, btn2, btnback)
        
        new_photo = types.InputMediaPhoto(open('images/five.jpg', 'rb'), caption="Как будет устроен быт?")
        bot.edit_message_media(media=new_photo, message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        
        #bot.edit_message_text("Как будет устроен быт?", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        

    @staticmethod
    def draw_six(message :types.Message, bot: TeleBot):
        callback_next = "7"
        callback_back = "5"

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Эстетика', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='Свобода', callback_data=f"{callback_next}_answer_2")
        btn3 = types.InlineKeyboardButton(text='Сила', callback_data=f"{callback_next}_answer_3")
        btn4 = types.InlineKeyboardButton(text='Уверенность', callback_data=f"{callback_next}_answer_4")
        
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)
        markup.add(btn1, btn2, btn3, btn4, btnback)

        new_photo = types.InputMediaPhoto(open('images/six.jpg', 'rb'), caption="Перейдем к стилизации! Какое настроение больше тебе подходит?")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)
        
        #bot.edit_message_text("Перейдем к стилизации! Какое настроение больше тебе подходит?", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        
    @staticmethod
    def draw_seven(message :types.Message, bot: TeleBot, image_type:int):
        callback_next = "8"
        callback_back = "6"

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='1', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='2', callback_data=f"{callback_next}_answer_2")
        btn3 = types.InlineKeyboardButton(text='3', callback_data=f"{callback_next}_answer_3")
        btn4 = types.InlineKeyboardButton(text='4', callback_data=f"{callback_next}_answer_4")
        #btn5 = types.InlineKeyboardButton(text='Подвесное кресло-качель', callback_data=f"{callback_next}_answer_5")
        #btn6 = types.InlineKeyboardButton(text='Второй этаж', callback_data=f"{callback_next}_answer_6")
   
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)
        markup.add(btn1, btn2, btn3, btn4, btnback)

        new_photo = types.InputMediaPhoto(open(f'images/seven_{image_type}.jpg', 'rb'), caption="А здесь?")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)
        
        #bot.edit_message_caption("Что должно быть в квартире мечты?", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        
    @staticmethod
    def draw_eight(message :types.Message, bot: TeleBot, image_type:int):
        callback_next = "9"
        callback_back = "7"

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='1', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='2', callback_data=f"{callback_next}_answer_2")
        btn3 = types.InlineKeyboardButton(text='3', callback_data=f"{callback_next}_answer_3")
        btn4 = types.InlineKeyboardButton(text='4', callback_data=f"{callback_next}_answer_4")
   
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)
        markup.add(btn1, btn2, btn3, btn4, btnback)

        new_photo = types.InputMediaPhoto(open(f'images/eight_{image_type}.jpg', 'rb'), caption="Здесь?")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)
        

        #bot.edit_message_text("Здесь?", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)
        

    @staticmethod
    def draw_nine(message :types.Message, bot: TeleBot, image_type:int):
        callback_next = "10"
        callback_back = "8"

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='1', callback_data=f"{callback_next}_answer_1")
        btn2 = types.InlineKeyboardButton(text='2', callback_data=f"{callback_next}_answer_2")
        btn3 = types.InlineKeyboardButton(text='3', callback_data=f"{callback_next}_answer_3")
        btn4 = types.InlineKeyboardButton(text='4', callback_data=f"{callback_next}_answer_4")
   
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)
        markup.add(btn1, btn2, btn3, btn4, btnback)

        new_photo = types.InputMediaPhoto(open(f'images/nine_{image_type}.jpg', 'rb'), caption="И вот тут ещё")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)
        
        #bot.edit_message_text("И вот тут еще", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)


    @staticmethod
    def draw_ten(message :types.Message, bot: TeleBot, selected_items: list[str]):
        callback_next = "11"
        callback_selected = "10"
        callback_back = "9"

        labels = ['Терраса', 'Камин', 'Джакузи', 'Библиотека', 'Подвесное кресло-качель', 'Второй этаж']
        markup = types.InlineKeyboardMarkup(row_width=1)

        for i in range(0,6):
            if str(i) in selected_items:
                btn = types.InlineKeyboardButton(text=f"{labels[i]} ✅", callback_data=f"{callback_selected}_answer_{i}_selected_{i}")
            else:
                btn = types.InlineKeyboardButton(text=labels[i], callback_data=f"{callback_selected}_answer_{i}_selected_{i}")
            markup.add(btn)

        if len(selected_items) > 0:
            btnnext = types.InlineKeyboardButton(text=messages_text.next_button, callback_data=callback_next)
            markup.add(btnnext)

        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)

        markup.add(btnback)

        new_photo = types.InputMediaPhoto(open(f'images/ten.jpg', 'rb'), caption="Что должно быть в квартире мечты? (Возможно несколько вариантов)")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)
        
        #bot.edit_message_text("И вот тут еще", message_id=message.id, chat_id=message.chat.id, reply_markup=markup)

    @staticmethod
    def draw_eleven(message :types.Message, bot: TeleBot, selected_items: list[str]):
        callback_next = "12"
        callback_selected = "11"
        callback_back = "10"
        markup = types.InlineKeyboardMarkup(row_width=1)
        labels = ['Детская площадка', 'Достопримечательности', 'Бизнес центр', 'Природа']

        for i in range(0,4):
            if str(i) in selected_items:
                btn = types.InlineKeyboardButton(text=f"{labels[i]} ✅", callback_data=f"{callback_selected}_answer_{i}_selected_{i}")
            else:
                btn = types.InlineKeyboardButton(text=labels[i], callback_data=f"{callback_selected}_answer_{i}_selected_{i}")
            markup.add(btn)

        if len(selected_items) >0:
            btnnext = types.InlineKeyboardButton(text=messages_text.next_button, callback_data=callback_next)
            markup.add(btnnext)

        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)
        markup.add(btnback)

        new_photo = types.InputMediaPhoto(open(f'images/eleven.jpg', 'rb'), caption="Рядом с идеальной квартирой находится...")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)


    @staticmethod
    def draw_result(message :types.Message, bot: TeleBot, res):
        callback_back = "11"
        markup = types.InlineKeyboardMarkup(row_width=1)
        btnback = types.InlineKeyboardButton(text=messages_text.back_button, callback_data=callback_back)

        markup.add(btnback)

        new_photo = types.InputMediaPhoto(open(f'images/final.jpg', 'rb'), caption="Тест пройден!")
        bot.edit_message_media(message_id=message.id, chat_id=message.chat.id, media=new_photo, reply_markup=markup)
        
        