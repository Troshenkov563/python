# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

list= random.sample(range(1000), 10)
print (f'Список {list}')
list2 = list[1::2]
result = sum(list2)
print(f'Сумма нечетных элементов = {result}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint, random


num = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(num):
     list.append(randint(0, 10))

for i in range(len(list)):
     while i < len(list)/2 and num > len(list)/2:
         num = num - 1
         a = list[i] * list[num]
         list2.append(a)
         i += 1

print(list)
print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def dif_max_min(mylist):
    min = 1
    max = 0
    for i in mylist:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)  
    print(f"Разница составила: {max-min}")
mylist = [1.1, 1.2, 3.1, 5, 10.01]
dif_max_min(mylist)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input())
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
n = int(input('Введите число: '))
for e in range(1, n + 1):
    list.append(fib(e))
    list.insert(0, NegaFibonacci(e))
print(list)
