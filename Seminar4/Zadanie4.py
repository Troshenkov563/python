# 30.
k = open('Seminar4/users.txt', 'r', encoding='utf-8') # opening
v = open('Seminar4/hobby.txt', 'r', encoding='utf-8') 

users = k.readlines() #reading
hobby = v.readlines()

for i in range(len(users)): #clearing
    users[i] = users[i].replace('\n','')

for i in range(len(hobby)):
    hobby[i] = hobby[i].replace('\n','')

k.close()
v.close()

my_dict = dict(zip(users, hobby)) #concatination into dictionary
# print(dictionary)

with open('Seminar4/users_hobby.txt', 'w', encoding="utf-8") as out: # print dict into file (from Seminar 4)
    keys = my_dict.keys()
    for key in keys:
        out.write(f'{key}: {my_dict[key]} \n')

# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def fac(n):
    q = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            q.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        q.append(n)
    return q
print(fac(int(input())))

# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")

# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0


from random import randint

k = int(input('Задайте натуральную степень '))

ratiosList = []
for i in range(k + 1):
    ratiosList.append(randint(1, 100))
print(f'Список коэффициентов: {ratiosList}') 
formula = ''
for i in range(k-1):
    formula = formula + str(ratiosList[i]) + 'x' + '^' + str(k - i) + ' + '
formula = formula + str(ratiosList[k-1]) + 'x' + ' + '
formula = formula + str(ratiosList[k]) + ' = 0'

print(formula)


with open('Seminar4\Polynomial_1.txt', 'w') as p:
    p.write(formula)





# 34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0