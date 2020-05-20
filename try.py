operator_list = ['+', '-', '/', '*']
try:
    operator, number_1, number_2 = input('введите польскую нотацию: ').split()
    number_1, number_2 = int(number_1), int(number_2)
    assert operator in operator_list, 'Таких заков операторов нету'
    if operator == '-':
        print(number_1 - number_2)
    elif operator == '+':
        print(number_1 + number_2)
    elif operator == '/':
        print(number_1 / number_2)
    elif operator == '*':
        print(number_1 * number_2)
except TypeError as t:
    print('Ошибка', t)
except ValueError as v:
    print('Нельзя вводить строки', v)
except IndexError as i:
    print('Ошибка в количестве аргументов ', i)
except ZeroDivisionError as z:
    print('Деление на ноль', z)
