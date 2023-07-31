# x: int = 4
# y: int = 3
# print(x + y) # 7

# x: int = "Hello"
# y: int = "World"
# print(x + y) # Hello World

# def summa(x1, x2):
#     print(x1 + x2)

# summa(8, 12)

# def summa(x1: int, x2: int) -> int:
#     res: int = x1 + x2
#     return res

# print(summa(8, 12))
# print(summa("Hello ", "World"))

# x: int = "Привет "
# y: int = " мир "
# # print(x + y)

# def summa(x1, x2):
#     print(x1 + x2)

# def summa2(x1: int, x2: int) -> int:
#     global x
#     res: int = x1 + x2
#     x = x + " алоха "
#     print(x1 + x2)
#     return res

# summa(8,12)
# print(summa2(7,13))
# print(summa2(" hello ", " world "))
# print(x)


# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# str1 = 'a a a b c a a d c d d'
# a = ''
# str1 = str1.split(' ')
# for i in str1:
#     count1 = a.count(i)
#     print(count1)
#     if a.count(i) == 0:
#         a += i+' '
#     else:
#         a += i+'_'+str(count1)+' '
# print(a.strip())

#Более правильный вариант

# sp = "a a a b c a a d c d d"
# new_list = sp.split()
# # print(new_list)
# new_ar = {}
# result = ""
# for i in new_list:
#     if i not in new_ar:
#         new_ar[i] = 0
#         result +=f"{i} "
#     else:
#         new_ar[i] += 1
#         result +=f"{i}_{new_ar[i]} "
# print(result)



# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# str1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# str2 = str1.replace('.', ' ')
# sp = str2.lower().split()
# print(str2)
# print(len(set(sp)))

#Вариант 2, в рдну строку
# str1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# str1 = str1.replace('.', ' ').lower().split()
# print(len(set(str1)))




# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# def max_num() -> int:
#     max_number: int = 0
#     while True:
#         n: int = int(input("Введите число: "))
#         if n == 0:
#             break
#         if n > max_number:
#             max_number = n
#     return max_number
# print(f"Максимальное значение  {max_num()} ")