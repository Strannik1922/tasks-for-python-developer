"""
Написать метод/функцию, который/которая на вход принимает целое число,
а на выходе возвращает то, является ли число простым.
"""


def function_check(value):
    if value <= 0:
        return 'Error: число должно быть положительным'
    elif value == 2:
        return True
    elif value % 2 == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    value = int(input('Введите число: '))
    print(function_check(value))
