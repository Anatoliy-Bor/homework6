my_dict = {'Tom' : [1984, 892066456697],'Anniy' : 1987, 'Djon' : 1996 }
print('Словарь с исходными данными :', my_dict)
print('Данные на пользователя Том :', my_dict['Tom'])
print(my_dict.get('Nina', 'Вывод без ошибки'))
my_dict.update({'Kat': 1987,
               'Misha': 1992})
print(my_dict)
user_del = my_dict.pop('Tom')
print('Удалить пользователя Tom ',user_del)
print(my_dict)
my_set = {1, 1, 5, 5, 1, 9, 8, 'Tom', 'Anniy', True, (12, 56, 56, 14)}
print(my_set)
print(my_set.add(2))
print(my_set)
print(my_set.discard(5))
print(my_set)