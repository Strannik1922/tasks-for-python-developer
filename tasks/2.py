"""
Написать метод/функцию, который/которая на вход принимает число (float),
а на выходе получает число, округленное до пятерок.
"""


def function_to_five(value, base):
    five = base * round(value/base)
    return five


if __name__ == '__main__':
    value = int(input('Введите число: '))
    base = 5
    print(function_to_five(value, base))
