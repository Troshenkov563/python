def Value_type():
    
    type = int(input('Введите "0", если будем производить вычисления с рациональными числами, или "1" - если с комплексными '))
    if type == 0 or type == 1:
        return type
    else:
        print('Вы некорректно ввели тип чисел. Используйте символы 0 или 1')

def Get_mode():
    
    mode = input('Введите интересующую вас операцию соответствующим символом: + сложение, - вычитание, * умножение, / деление  ')
    if mode in ['+', '-', '*', '/']:
        return mode
    else:
        print('Вы некорректно ввели опереацию. Используйте символы + - * /')

#Библиотека операций    
mode = {'+': 'сложения', '-': 'вычитания', '*': 'умножения', '/': 'деления'}

def Print_result(oper, n1, n2, res):
    
    print(f'Результат операции {mode[oper]} чисел {n1} и {n2} = {res}')

def Get_rational_value():
    
    value = float(input())
    return value

def Get_complex_value():
    
    print('Введите комплексное число в сл. формате: a+bi. Без пробелов')
    print('Например: 2+1j')
    value = complex(input())
    return value