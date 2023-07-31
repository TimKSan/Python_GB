# n = 999
# sum = 0
# while n > 0:
#     b = n % 10
#     sum = sum + b
#     n = n // 10
# print (sum)

# n = 13
# p = int(n / 3 / 2)
# k = int(int(n / 3) * (2))
# s = int(n / 3 / 2)
# print(p, k, s)

# n = 456255
# numLeft = n // 1000
# numRight = n % 1000
# sumLeft = (numLeft % 10) + (numLeft % 100 // 10) + (numLeft // 100)
# sumRight = (numRight % 10) + (numRight % 100 // 10) + (numRight // 100)
# if sumLeft == sumRight:
#     print('yes')
# else: print('no')

a = 3
b = 5
c = 10
area = a*b
if area < c or area % c == 1:
    #if c == 1 and a == 1 or b == 1
    print('no')
elif c == 1 and a != 1 or b != 1: print('no')
else: print('yes')

print(15%10)