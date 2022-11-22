from datetime import datetime as dt
from view import Get_mode 
# нужно импортировать функции внесения чисел, выбора операции и вывода результата
'''
Функция calc_logger записывает в файл время внесения данных, 
число 1 и число 2 от пользователя 
(вне зависимости от того рациональное оно или нет), 
вид операции над числами и сам результат.
'''
def calc_logger(num1, num2, oper, res):
    time = dt.now().strftime('%H:%M')
    with open('Seminar7\log.txt', 'a', encoding='utf-8') as file:
        file.write('{}; число 1: {};число 2: {}; операция: {}; результат: {};\n'
                    .format(time, num1, num2, oper, res))