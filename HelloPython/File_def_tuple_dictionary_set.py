# FILE ========файлы====================
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') #создание файла и 'a' дозапись в него, 'r'- чтение данных,
#                              #'w'- запись данных(стирает все что было, меняет на новое).
# data.writelines(colors) # .writelines - без разделителей
# data.write('\nLINE12\n')
# data.write('LINE123\n')
# data.close() # обязательно закрывать файл после использования!

# exit() # ставится перед программой, которую не надо в данный момент выполнять

# path = 'file.txt'
# data = open(path, 'r') # открытие файла для чтения данных
# for line in data:
#     print(line)
# data.close() # обязательно закрывать файл после использования!

# with open('file.txt', 'a') as data: # сам закрывается
#     data.write('line1133111\n')
#     data.write('line2244222\n')

# FUNCTION =======функции==================
# import hello   #из скрипта выдергиваем функцию, которую ранее создали...
# print(hello.f(1))
# # ====== or ========
# import hello as h   #из скрипта выдергиваем функцию(hello), присваиваем псевдоним(h), которую ранее создали, ...
# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5)) #!!!!!
# print(new_string('!')) #!!!
# print(new_string(4)) #12

# def concatenatio(*params):
#     res: str = ''
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio(1, 2, 3, 4)) #TypeError: работаем со строкой!

# --recursion--------
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# TUPLE=======кортежи=====================================
# t = ()
# print(type(t)) # <class 'tuple'>
# t = (1,)
# print(type(t)) # <class 'tuple'>
# t = (1)
# print(type(t)) # <class 'int'>
# t = (28, 9, 1990)
# print(type(t)) # <class 'tuple'>
# colors = ['red', 'green', 'blue'] # список
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors) # преобразование списка в кортеж
# print(t) # ('red', 'green', 'blue')

# a = (3, 1, 41, 4)
# print(a) #вывести картеж
# print(a[-2]) # вывести второй с конца элемент кортежа

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# print(t[-2]) # green

# for e in t:
#     print(e) # red green blue

# t[0] = 'black' # TypeError: -кортеж неизменяем! нельзя присвоить новое значение, в отличие от списка

# -------двойное преобразование--------
# t = tuple(['red', 'green', 'blue']) #список превращаем в кортеж
# red, green, blue = t # превращение в независимые переменные
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# DICTIONARY=========словари======================================
# dictionary = {} #пустой словарь

# dictionary = \
#     {
#         'up': 'u',
#         'left': 'l',
#         'down': 'd',
#         'right': 'r'
#     } 
# print(dictionary) # {'up': 'u', 'left': 'l', 'down': 'd', 'right': 'r'}
# print(dictionary['left']) # l

# for k in dictionary.keys(): #вытащить все ключи из словаря
#     print(k) # up left down right

# for k in dictionary.values(): #вытащить все значения из словаря
#     print(k) # u l d r

# del dictionary['left'] # удаление элемента

# SET========множества=======================================================
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') #добавление элемента, но если он есть, добавления не произойдет
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue', 'gray'}
# colors.remove('red') #удаление элемента, если его нет, выдаст ошибку
# print(colors) # {'green', 'blue', 'gray'}
# colors.discard('red') #удаление элемента, если его нет, НЕ выдаст ошибку
# print(colors) # {'green', 'blue', 'gray'}
# colors.clear() #очистка множества
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # создание копии множества а
# print(c) # {1, 2, 3, 5, 8}
# u = a.union(b) # объединение множеств
# print(u) # {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # пересечение
# print(i) # {8, 2, 5}
# dl = a.difference(b) # отличие а от в
# print(dl) # {1, 3}
# dr = b.difference(a) # отличие в от а
# print(dr) # {13, 21}

# q = a\
#     .union(b)\
#     .difference(a.intersection(b))
# print(q) # {1, 21, 3, 13}

# s = frozenset(a) # замороженное множество, невозможно ничего в нем изменить.

# LIST========списки===========================================================
# list1 = [1, 2, 3, 4, 5]  #ОСТОРОЖНО С КОПИРОВАНИЕМ СПИСКОВ!
# list2 = list1
# for e in list1:
#     print(e) # 1 2 3 4 5
# print()
# for e in list2:
#     print(e) # 1 2 3 4 5
# print()
# list1[0] = 123 #при копировании списка, меняя значение в одном, оно поменяется и во втором.
# list2[1] = 333
# for e in list1:
#     print(e) # 123 333 3 4 5
# print() 
# for e in list2:
#     print(e) # 123 333 3 4 5

# list1 = [1, 2, 3, 4, 5]
# print(len(list1)) # 5
# print(list1.pop()) #метод .pop удаляет последний элемент списка
# print(list1) # [1, 2, 3, 4]
# print(list1.pop())
# print(list1) # [1, 2, 3]
# print(list1.pop())
# print(list1) # [1, 2]

# list1 = [1, 2, 3, 4, 5]
# print(list1.insert(2, 11)) #метод .insert  вставляет элемент на нужную позицию списка
# print(list1) # [1, 2, 11, 3, 4, 5]

# list1 = [1, 2, 3, 4, 5]
# print(list1.append(11)) #метод .append  добавляет элемент в конец списка
# print(list1) # [1, 2, 3, 4, 5, 11]