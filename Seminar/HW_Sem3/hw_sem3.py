# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1

# list_1 = [1, 1, 1, 1, 5]
# k = 1

# count = 0
# for i in list_1:
#     if i == k:
#         count += 1

# print(count)




# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

# list_1 = [1, 12, 11, 6, 7, 8, 15]
# k = 11
# list_1.sort() #[1, 6, 7, 8, 12, 15]
# tempMin = 0

# for i in range(len(list_1)):
#     if list_1[i] > tempMin and list_1[i] < k:
#         tempMin = list_1[i]
#     if list_1[i] > k and list_1[i] - k < k - tempMin:
#         tempMin = list_1[i]
#     if list_1[i] == k:
#         tempMin = list_1[i]
#     i+=1

# print(tempMin)
