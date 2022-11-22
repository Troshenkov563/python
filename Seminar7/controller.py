from view import Value_type, Get_mode, Print_result, Get_rational_value, Get_complex_value
from logger import calc_logger
import mod_sum, mod_div, mod_mult, mod_sub

def Launch_project():
    if Value_type():
        print('Введите первое число') 
        num1 = Get_complex_value() 
        print('Введите второе число')
        num2 = Get_complex_value()
        operat = Get_mode()
        if operat == '+':
            result = mod_sum.summa(num1, num2)
        elif operat == '-':
            result = mod_sub.sub(num1, num2)
        elif operat == '*':
            result = mod_mult.Mult(num1, num2)
        elif operat == '/':
            result = mod_div.Division(num1, num2)
    else:
        print('Введите первое число')  
        num1 = Get_rational_value()
        print('Введите второе число')
        num2 = Get_rational_value()
        operat = Get_mode()
        if operat == '+':
            result = mod_sum.summa_compl(num1, num2)
        elif operat == '-':
            result = mod_sub.sub_compl(num1, num2)
        elif operat == '*':
            result = mod_mult.Mult_compl(num1, num2)
        elif operat == '/':
            result = mod_div.Division_compl(num1, num2)
    calc_logger(num1, num2, operat, result)

    Print_result(operat, num1, num2, result)