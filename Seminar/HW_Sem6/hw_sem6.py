# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_el = int(input('Введите первый элемент: '))
diff = int(input('Введите разность элементов: '))
q = int(input('Введите кол-во элементов: '))

def arefm(first_el, diff, q):
    sp = [item for item in range(first_el, q+1, diff)]
    return sp
    
print(arefm(first_el, diff, q))




# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = []
min = 5
max = 55



def searchInInterval(list1, min, max):
    for i in range(len(list1)):
        if list1[i] > min and list1[i] < max:
            list2.append(i)
            


searchInInterval(list1, min, max)
print(list1)
print(f'Индексы {list2} входят в интервал {min} - {max}')