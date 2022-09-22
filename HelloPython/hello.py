# print('hello world')

# типы данных и переменная
#  int, float, boolean, str, list, None


# value = None  # заявление переменной для ее использования в дальнейшем
# print(type(value))
# a = 123
# b = 1.23
# print(type(a)) # type - чтобы узнать, какой тип переменной используется
# print(type(b))
# value = 12334
# print(type(value))

# s = 'hello world' # строка, \n (\nworld')- перенос на другую строку
# print(s) # вывод строки
# print(a, '-',b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)
# list = ['1', '2', '3', 'hello world', 1,2,4.5,True] # список
# print(list)

# Ввод и вывод данных:
# print, input

# print('Введите a');
# a = int(input()) #без int или float, считать не будет
# print('Введите b');
# b = float(input())
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(a, '+' , b, '=', a+b)

# Арифметические операции:
# +, -, *, /, %, // - результат деления целое число, ** - возведение в степень
# () - скобки меняют приоритет

# a = 123
# b = -321  # унарный минус
# c = a + b
# print(c)

# a = 1.31232
# b = 3
# c = round(a*b, 5) # округление(  , 5) до 5 знаков после запятой
# print(c)

# Сокращенные операции
# a = 3
# a += 5 # все равно что a = a+5
# print(a)

# Логические операции:
# >, >=, <, <=, ==, !=
# not, and, or НЕ ПУТАТЬ С &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# funk = 1
# T = 4
# x = 2
# print(funk < T > (x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2 ==0
# print(is_odd)

# Управляющие конструкции:
# if, if-else; if - elif - else


# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет,', username)

# Циклы:

## while:
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original %10)
#     original //=10
# print(inverted)

## while-else:
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original %10)
#     original //=10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

## for i in ...:

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

    # или 

# for i in range(10):
#     print(i) 

    # или 

# for i in range(1, 10, 2): #приращение(шаг) 2: 1,3,5,7,9
#     print(i)

# или 

# for i in 'qwe - rty':
#     print(i)

##СТРОКИ:

# text = 'съешь еще этих мягких французских булок'
# print(len(text)) #количество символов
# print('еще' in text) #наличие подстроки 
# print(text.isdigit()) #являются ли символы числами?
# print(text.islower()) #являются ли символы символами нижнего регистра?
# print(text.replace('еще', 'ЕЩЁ')) #заменить одно на другое

# for c in text:
#     print(c)

## help(text.istitle) - когда необходимо понять, что за метод/функция

##СРЕЗЫ:

# text = 'съешь еще этих мягких французских булок'
# print(text[0])
# print(text[1])
# #print(text[len(text)]) ошибка
# print(text[len(text)-1])
# print(text[-5])
# print(text[:]) #от 1 до последнего символа, т.е. весь текст
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]
# print(text)

##СПИСКИ: введение
## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# ran = range(1, 6)
# numbers = list(ran)
# print(numbers)

# numbers[0] = 10
# print(f'{len(numbers)} len')

# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)

# colors.append('gray') #добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red') #del colors[0] # удалить элемент

##ФУНКЦИИ:

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2
# print(f(arg))
# print(type(f(arg)))