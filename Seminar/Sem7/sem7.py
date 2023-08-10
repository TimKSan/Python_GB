# def create_prase(func, word):
#     print(func(word))

# def hello(s):
#     return f'Hello {s}'

# def bye(s):
#     return f'{s} bye-bye'

# create_prase(hello, "world")
# create_prase(hello, "Timur")
# create_prase(bye, "world")
# create_prase(bye, "Timur")

# def calc_power(degree):
#     def power(number):
#         return number ** degree
#     return power

# # print(calc_power(2)(3)) # передается 2 числа

# square = calc_power(2)  # передаем первое число
# cube = calc_power(3)

# print(square(8))  #передаем второе
# print(cube(3))

##############ЛЯМБДА ФУНКЦИЯ

# print((lambda x, y: x+y) (5, 8))


# CALC = {'+': lambda x, y: x + y,
#         '-': lambda x, y: x + y,
#         '*': lambda x, y: x + y,
#         '/': lambda x, y: x + y,
# }
# print(CALC['+'](5,15))

###### Функция mар()

# sp = [ 4, 6, 7, 2, 56, 5]
# print(list(map(lambda item: item**2 if item > 5 else 0, sp)))
# print(*filter(lambda item: True if item>5 else False, sp))
# print(list(filter(lambda item: item>5, sp)))

############### enumerate()

# sp = [ 4, 6, 7, 2, 56, 5]
# for i, v in enumerate(sp):
#     print(i,v)

################# zip()

# name = ['петя', 'ваня']
# sp = [ 4, 6, 7, 2, 56, 5]
# for x1, x2 in zip(name, sp):
#     print(x1, x2)





# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# 20 минут
# Семинар 7. Функции высшего порядка
# Задача №49. Решение в группах
# Ввод:


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def find_farthest_orbit(orbits):
#     s = list(map(lambda item: 3.14*item[0]*item[1] if item[0] != item[1] else 0, orbits))
#     return f'сама далекая планета имеет индекс {s.index(max(s))}'
# print(find_farthest_orbit(orbits))


# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:

# def same_by(characteristic, objects):
   
#     el = len(list(filter(characteristic,objects)))
#     print(el)
#     return not el or el == len(objects)
# values = [0, 2, 10, 6]
# values2 = [1, 3, 5, 7]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')



# Необходимо написать программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три различных списка - Фамилии владельцев банковских счетов, указание валют счетов, соответствующее состояние счетов. То есть у Иголкина счет в евро и там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.



# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент, далее надо применить ее в комбинациях с map и zip.

#   На выходе программы должны быть три пары значений - фамилии владельцев счетов и состояние рублевого счета.

# surnames = ["Иванов", "Карпов", "Иголкин"]
# currency_name = ["рубль", "доллар", "евро"]
# balances = [30000, 40000, 50000]
# dollar = 90
# euro = 99

# def calc(currency, balance):
#     result = balance
#     if currency == "доллар":
#         result *= dollar
#     elif currency == "евро":
#         result *= euro
#     return result
    
# new_ballances = list(map(calc, currency_name, balances))
# print(*zip(surnames, new_ballances))

