# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

#poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# poem_list = list(poem.split(' '))
# vowels_list = []


# # for i in range(len(poem_list)):
# #     vowels_list.append(poem_list[i].replace('а', 'Ж'))
# # #     #vowels_list.append(j.replace(j, ''))
# for i in range(len(poem)):
#     if poem[i] == 'а' or poem[i] == ' ':
#         vowels_list.append(poem[i])
#     else: continue

# join_vowels = ''.join(vowels_list)
# join_list = list(join_vowels.split(' '))


# print(len(join_list[]))

# while i < len(poem_list) - 1:
#     if poem_list[i] == poem_list[i+1]:
#         print('Парам пам-пам')
#     else: print('Пам парам')
#     i += 1

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да па-ра-па-да па-ра-па-да пара-ра-рам пара-ра-рам'

def vinipuh(poem):
    vowels_str = poem.translate(dict.fromkeys(map(ord, u"бвгджзйклмнпрстфхцчшщ-")))     # в виде строки получаем гласные каждого отдельного слога(удалением согласных)
    poem_list = list(vowels_str.split(' '))                                             # строку в список
    
    result = all(poem_list[i] == poem_list[i+1] for i in range(len(poem_list) - 1))     # сравниваем все элементы списка all() -> true/false
    if result:
        return print('Парам пам-пам')
    else: print('Пам парам')

vinipuh(poem)