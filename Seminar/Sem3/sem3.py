# sp = []
# sp.append(5)
# sp.extend([7,8,True])
# sp.insert(0,5.7)
# sp = sp + [1,2,True,44]
# print(sp)
# # print(sp[3::])
# # print(sp[2:5])
# # print(sp[-5])
# a = sp.pop()
# print(a)
# sp.remove(True)
# del sp[0]

# for i,k in enumerate(sp):
#     print(i,k)
# print(sp)
# t = (4,8,9)
# print(t[0])

# d = {}
# d["дядя Ваня"] = "+78465564"
# d["дядя Вова"] = "12312131"
# del d["дядя Вова"]
# print(d)
# for key, value in d.items():
#     print(key, value)

# print(d.keys())
# print(d.values())

# s = set()
# s.add(5)
# s.add(7)
# print(s)
# print(6 in s)

# list списки tuple кортежи dict словари set множество

# #ВТОРАЯ ЗАДАЧА
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# data = [1, 2, 3, 4, 5]
# k = 3
# print(data[k:] + data[:k])

# #ВТОРАЯ ЗАДАЧА второй вариант
# l_1 = [1, 2, 3, 4, 5]
# k = 3
# print (l_1)
# for i in range (k):
#     a = l_1.pop(len(l_1) - 1)
#     l_1.insert(0, a)
# print (l_1)



# # ПЕРВАЯ ЗАДАЧА
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# data = [1, 1, 2, 0, -1, 3, 4, 4]
# print(data)
# different_numbers = []
# for number in data:
#     if number not in different_numbers:
#         different_numbers.append(number)
# print(f"Различных чисел: {len(different_numbers)}")


#Задача 3
# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# v = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

# v2 = []
# for i in v:
#     for k,v in i.items():
#         if v.strip() not in v2:
#             v2.append(v.strip())
#             print(k.strip(), v.strip()) 

# print(v2)






# Задача 4
# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


# v = [0, -1, 5, 2, 3]
# i = 1
# j = 0
# while i < len(v):
#     if v[i] > v[i-1]:
#         j+=1
#     i+=1
# print(j)
