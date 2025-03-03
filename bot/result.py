from db.db_model import Result
from model import People

def get_result(res:list[Result]):
    people:People = People()
    is_leave_with_partner:bool = False
    is_leave_with_parents:bool = False
    is_want_guest:bool = False
    count_working_from_home:int = 0
    is_want_wash_at_home:bool = False

    #Parsing results
    for ans in res:
        if ans.question_id == 2:
            people.from_answer(ans.answer)
    
        if ans.question_id == 3:
            if int(ans.answer) == 1:
                is_leave_with_partner = True

        if ans.question_id == 4:
            if int(ans.answer) == 1:
                is_leave_with_parents = True  

        if ans.question_id == 5:
            if int(ans.answer) == 1:
                is_want_guest = True   

        if ans.question_id == 6:
            if int(ans.answer) == 1:
                count_working_from_home = 1
            if int(ans.answer) == 2:
                count_working_from_home = 2  

        if ans.question_id == 7:
            if int(ans.answer) == 1:
                count_working_from_home = True      

    # Initialize room counts

    count_bedroom_ch = 0  # детская спальня
    count_bedroom = 0     # взрослая спальня
    count_office = 0      # офис
    count_playroom = 0    # игровая
    count_laundryroom = 0 # постирочная
    img_title = ''
    
    # ДЕТСКАЯ
    teenager_m = int(people.zb)  # подросток М
    teenager_w = int(people.zg)  # подросток Ж
    
    if teenager_m + teenager_w >= 2:
        count_bedroom_ch = 2
    elif teenager_m + teenager_w == 1:
        count_bedroom_ch = 1

    # Ребенок или младенец одного пола 0.5 комнаты
    teen_m = int(people.kb)  # ребенок или младенец М
    teen_w = int(people.kg)  # ребенок или младенец Ж

    count_bedroom_ch += min(2, round(teen_m * 0.5))
    count_bedroom_ch += min(2, round(teen_w * 0.5))
    count_bedroom_ch = min(count_bedroom_ch, 2)

    #СПАЛЬНЯ
    if is_leave_with_partner:
        count_bedroom += 1   
    if is_leave_with_parents and count_bedroom < 2:
        count_bedroom += 1  
    if is_want_guest and count_bedroom < 2:
        count_bedroom += 1      

    # ОФИС
    if count_working_from_home == 1:
        count_office = 1
    if count_bedroom + count_bedroom_ch < 2 and count_working_from_home == 2:
        count_office = 2
        
    

    # Убираем одну спальню
    if count_office + count_bedroom_ch + count_bedroom > 4:
        count_bedroom = 1


    # ИГРОВАЯ
    if teen_m + teen_w >= 3 and count_office + count_bedroom_ch + count_bedroom < 4:
        count_playroom = 1

    # ПОСТИРОЧНАЯ
    if is_want_wash_at_home:
        count_laundryroom = 1

    # Вывод изображения
    img_name = f'{count_bedroom_ch}-{count_bedroom}-{count_office}-{count_playroom}-{count_laundryroom}.jpg'
    
    # Return results
    return img_name

def create_final_message(result:list[Result], full_name, username) -> str:
    message = f"""Лид с [@smartres_quiz_bot]
Имя: {full_name}
Телеграмм: @{username}\n"""
    for res in result:
        if int(res.question_id) == 1:
            message +=f"\n{res.question_id}. Намекни нам на свой пол и возраст :)\n"
            if int(res.answer) == 1: message += """- Мужчина, 16-25 лет\n"""
            if int(res.answer) == 2: message += """- Мужчина, 26-45 лет\n"""
            if int(res.answer) == 3: message += """- Мужчина, 45+ лет\n"""
            if int(res.answer) == 4: message += """- Женщина, 16-25 лет\n"""
            if int(res.answer) == 5: message += """- Женщина, 26-45 лет\n"""
            if int(res.answer) == 6: message += """- Женщина, 45+ лет\n"""

        if int(res.question_id) == 2:
            message +=f"\n{res.question_id}. Рядом с идеальной квартирой находится...\n"
            answers = res.answer.split("_")
            message +=f"\n{res.question_id}. С тобой проживают дети?\n"
            message += f"""- Ребенок, М {answers[0]}\n"""
            message += f"""- Ребенок, Ж {answers[1]}\n"""
            message += f"""- Подросток, М {answers[2]}\n"""
            message += f"""- Подросток, Ж {answers[3]}\n"""

        if int(res.question_id) == 3:
            message +=f"\n{res.question_id}. Ты живёшь с партнёром?\n"
            if int(res.answer) == 1: message += """- Да\n"""
            if int(res.answer) == 2: message += """- Нет\n"""

        if int(res.question_id) == 4:
            message +=f"\n{res.question_id}. Живёте со старшим поколением вместе?\n"
            if int(res.answer) == 1: message += """- Да\n"""
            if int(res.answer) == 2: message += """- Нет\n"""    

        if int(res.question_id) == 5:
            message +=f"\n{res.question_id}. Бывает ли, что у тебя остаётся ночевать кто-то из близких?\n"
            if int(res.answer) == 1: message += """- Да, регулярно!\n"""
            if int(res.answer) == 2: message += """- Да, иногда.\n"""         
            if int(res.answer) == 3: message += """- Нет, редко.\n"""       

        if int(res.question_id) == 6:
            message +=f"\n{res.question_id}. Сколько человек работают из дома?\n"
            if int(res.answer) == 1: message += """- Один! И он мечтает о домашнем офисе.\n"""
            if int(res.answer) == 2: message += """- Два! Мы на удалёнке 😎\n"""         
            if int(res.answer) == 3: message += """- Никто! Квартира для жизни, а не для работы\n"""  

        if int(res.question_id) == 7:
            message +=f"\n{res.question_id}. Как будет устроен быт?\n"
            if int(res.answer) == 1: message += """- Хочу специальную комнату 🤩\n"""
            if int(res.answer) == 2: message += """- Никакой возни в квартире!\n"""

        if int(res.question_id) == 8:
            message +=f"\n{res.question_id}. Перейдем к стилизации! Какое настроение больше тебе подходит?\n"
            if int(res.answer) == 1: message += """- Эстетика\n"""
            if int(res.answer) == 2: message += """- Свобода\n"""
            if int(res.answer) == 3: message += """- Сила\n"""
            if int(res.answer) == 4: message += """- Уверенность\n"""

        if int(res.question_id) == 9:
            message +=f"\n{res.question_id}. А здесь?\n"
            if int(res.answer) == 1: message += """- Кухня 1\n"""
            if int(res.answer) == 2: message += """- Кухня 2\n"""
            if int(res.answer) == 3: message += """- Кухня 3\n"""
            if int(res.answer) == 4: message += """- Кухня 4\n"""     

        if int(res.question_id) == 10:
            message +=f"\n{res.question_id}. Здесь?\n"
            if int(res.answer) == 1: message += """- Спальня/гардеробная 1\n"""
            if int(res.answer) == 2: message += """- Спальня/гардеробная 2\n"""
            if int(res.answer) == 3: message += """- Спальня/гардеробная 3\n"""
            if int(res.answer) == 4: message += """- Спальня/гардеробная 4\n"""        

        if int(res.question_id) == 11:
            message +=f"\n{res.question_id}. И вот тут ещё\n"
            if int(res.answer) == 1: message += """- Ванна/гардеробная 1\n"""
            if int(res.answer) == 2: message += """- Ванна/гардеробная 2\n"""
            if int(res.answer) == 3: message += """- Ванна/гардеробная 3\n"""
            if int(res.answer) == 4: message += """- Ванна/гардеробная 4\n"""   

        if int(res.question_id) == 12:
            message +=f"\n{res.question_id}. Что должно быть в квартире мечты? (Возможно несколько вариантов)\n"
            answers = res.answer.split("_")
            if "1" in answers: message += """- Терраса\n"""
            if "2" in answers: message += """- Камин\n"""
            if "3" in answers: message += """- Джакузи\n"""
            if "4" in answers: message += """- Библиотека\n"""   
            if "5" in answers: message += """- Подвесное кресло-качель\n"""   
            if "6" in answers: message += """- Второй этаж\n"""   

        if int(res.question_id) == 13:
            message +=f"\n{res.question_id}. Рядом с идеальной квартирой находится...\n"
            answers = res.answer.split("_")
            if "1" in answers: message += """- Детская площадка\n"""
            if "2" in answers: message += """- Достопримечательности\n"""
            if "3" in answers: message += """- Бизнес центр\n"""
            if "4" in answers: message += """- Природа\n"""   
    return message
    