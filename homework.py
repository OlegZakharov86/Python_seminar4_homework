# Задача1
# Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$

n = 100
pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))
print(round(pi,3))

# Задача2
#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def simplemult(n):
#     list = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             list.append(i)
#     print(list)
# print('введите целое число: ')
# n = int(input())
# simplemult(n)

# Задача3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# def newList(list):
#     uniqueList = [i for i in list if list.count(i)==1]
#     print(uniqueList)
  
# list = [2, 4, 5, 2, 4, 6, 5, 3]
# print(newList(list))

