"""
Написать метод/функцию, который/которая на вход принимает число (int),
а на выходе выдает слово “компьютер” в падеже, соответствующем указанному количеству.
Например, «25 компьютеров», «41 компьютер», «1048 компьютеров».
Есть Python-библиотека pytils для работы с числительными и падежами вокруг них.
"""


# def function_computer(value):
#     if value == 1:
#         return str(value) + ' компьютер'
#     elif value <= 4:
#         return str(value) + ' компьютера'
#     else:
#         return str(value) + ' компьютеров'


# if __name__ == '__main__':
#     value = int(input('Введите число компьютеров: '))
#     print(function_computer(value))


from pytils import numeral

value = int(input('Введите количество компьютеров: '))
print("%s" % (
    numeral.get_plural(value, "компьютер, компьютера, компьютеров"),
    ))

