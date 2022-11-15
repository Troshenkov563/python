# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

data = [2, 3, 5, 9, 3]
result = sum(data[1::2])
print(result)


#  Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


my_list = list(map(int, input("Введите список чисел, разделенных пробелом: ").split())) 
print(f'Введенный список: {my_list}')

list_unuque = list(filter(lambda x: my_list.count(x) == 1, my_list)) #lambda and filter
print(f'Список уникальных значений: {list_unuque}')


# Задайте число. Составьте список чисел Фибоначчи

fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
print(fib(int(input())))


# Вывести список, содержащий средние арифметические значения чисел 
# каждого вложенного кортежа в заданном кортеже кортежей numbers.

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
my_list = [sum(i)/len(i) for i in numbers] #list comprehension с изменением
print(my_list)
