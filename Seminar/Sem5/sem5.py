# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n - 1)
        
# print(sum(5))




# Задача №31. Решение в группах. Последовательностью Фибоначчи называется
# последовательность чисел. Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib((n - 2)) + fib((n - 1))

# print(fib(10))



# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


# def change(n, i = 0):
#     if i == len(n):
#         return n
#     if n[i] == 5 or n[i] == 4:
#         n[i] = 1
#     change(n, i + 1)




# x = [1, 3, 5, 3, 4]
# change(x)
# print(x)

