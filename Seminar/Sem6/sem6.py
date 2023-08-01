# def sq(sp):
#     res = []
#     for i in sp:
#         res.append(i**2)
#     return res

# sp = [1, 23, 43,3]
# print(sq(sp))

# print([i**2 for i in sp]) #то же самое что и сверху 

# def sq(sp):
#     res = []
#     for i in sp:
#         if i > 4:
#             res.append(i**2)
#     return res

# sp = [1, 23, 43,3]
# print(sq(sp))

# sp = [1, 23, 43,3]

# print([i**2 for i in sp if i > 4]) # то же самое что и сверху 




# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# import random

# sp1_len = int(input('введите 1 массив: '))
# sp2_len = int(input('введите 2 массив: '))
# sp1 = [random.randint(1, 10) for _ in range(sp1_len)]
# sp2 = [random.randint(1, 10) for _ in range(sp2_len)]
# sp3 = []
# for i in sp1:
#     if i not in sp2:
#         sp3.append(i)
    
# print(sp1)
# print(sp2)
# print(sp3)

############### ВАРИАНТ 2 #################

# import random

# arr1_length = int(input("Введите N: "))
# arr2_length = int(input("Введите M: "))

# arr1 = [random.randint(1, 10) for _ in range(arr1_length)]
# arr2 = [random.randint(1, 10) for _ in range(arr2_length)]

# print(arr1)
# print(arr2)

# result = [item for item in arr1 if item not in arr2]
# print(result)

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.





# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
import random

sp_len = int(input('введите длину N: '))
sp = [random.randint(1, 10) for _ in range(sp_len)]
print(sp)
count = 0
for i in range(len(sp)):
    # print(sp[i-1])
    if sp[i-1] < sp[i] :
        print(f'{sp[i-1]} < {sp[i]}')
        count +=1
print(count)



# import random


# def check_neighbours(index, array):
#     if array[(index + 1) % len(array)] < array[index] and array[(index - 1) % len(array)]  < array[index]:
#         return array[index]



# arr_length = int(input("Введите N: "))
# arr = [random.randint(1, 5) for _ in range(arr_length)]
# print(arr)

# result = [1 for (index, value) in enumerate(arr) if check_neighbours(index, arr)]
# print(sum(result))