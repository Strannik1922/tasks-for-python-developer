# if __name__ == '__main__':
#     list_of_cities = str(input('Введите список городов: '))
#     list = str(list_of_cities.split(' '))
#     print(list)
#     string = ''.join(list)
#     print(string)


# def function_list_into_string_of_cities(cities):
#     return cities


# if __name__ == '__main__':
#     cities = list(map(str, input('list_of_cities: ').split(' ')))
#     print(function_list_into_string_of_cities(cities))


cities = list(map(str, input('Введите список городов: ').split(' ')))
print('Строка городов: ' + ' '.join(cities))
