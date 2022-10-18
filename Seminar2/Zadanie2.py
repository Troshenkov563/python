# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = input("Введите число: ")
print(f"Сумма цифр = {sumNums(num)}")

# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input("Введите число: "))

list = []
mult = 1
for e in range(1, num + 1):
    mult *= e
    list.append(mult)

print(f"Произведения чисел от 1 до {num}:  {list}")

# второй вариант:

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = int(input("Введите число: "))

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')



# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на введенных пользователем позициях.



# *Реализуйте алгоритм перемешивания списка.

import random 
listA = [2, 8, 4, 3, 1, 5] 
random.shuffle(listA) 
print(listA)
