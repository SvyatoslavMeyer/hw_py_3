# Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# list = [int(input('Добавьте число в список: ')) for _ in range(int(input('Введите количество элементов списка: ')))]
# summ = 0
# for i in range(1, len(list), 2):
#     summ += list[i]
# print(f'Полученный список - {list}')
# print(f'Сумма элементов списка, стоящих на нечётной позиции равна: {summ}')

# list_2 = [int(input()) for _ in range(int(input()))]
# print(sum(list_2[1::2]))


# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# list_3 = [int(input('Добавьте число в список: ')) for _ in range(int(input('Введите количество элементов списка: ')))]
# list_4 = []
# for i in range((len(list_3)+1)//2):
#     list_4.append(list_3[i] * list_3[len(list_3) - 1 - i]) 
# print(f'Список с произведением пар чисел списка: {list_4}')


# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# list_3 = [float(input('Добавьте число в список: ')) for _ in range(int(input('Введите количество элементов списка: ')))]
# min = 1
# max = 0
# for i in list_3:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)
# print(max - min) 


# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

# s = ''
# num = int(input('Введите число для его реобразования: '))
# while num > 0:
#     s = str(num % 2) + s
#     num //= 2
# print(f'Введенное число в двоичной системе => {s}')


# Задайте число. Составьте список чисел 
# Фибоначчи, в том числе для отрицательных индексов.

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# def NegaFibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = [0]
# userNumber = int(input('Введите число: '))
# for e in range(1, userNumber + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)
