# чтобы быстро создавать списки:
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)] - на начальном уровне лучше не применять

# =======LIST COMPREHENSION============================
# list1 = []
# for i in range(1, 21):
#     if (i % 2 == 0):
#         list1.append(i)
# print(list1) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# -----то же самое, но короче и красивее:
# list1 = [i for i in range(1, 21) if i % 2 == 0]
# print(list1) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# list1 = []
# for i in range(1, 21):
#     list1.append(i)
# print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # -----то же самое, но короче и красивее:
# list1 = [i for i in range(1, 21)]
# print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# СПИСОК КОРТЕЖЕЙ:
# list1 = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(list1) # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

# list1 = [(i, i**2) for i in range(1, 21) if i % 2 == 0]
# print(list1) # [(2, 4), (4, 16), (6, 36), (8, 64), (10, 100), (12, 144), (14, 196), (16, 256), (18, 324), (20, 400)]

# ОБРАБОТКА ДАННЫХ:
# def f(x):
#     return x ** 3

# list1 = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list1) # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

# list1 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list1) # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]

# РАБОТА С file.txt!!!============
# path = '/Users/marina/Documents/Python/HelloPython/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out) # [(2, 4), (8, 64), (38, 1444)]

# ===СДЕЛАЕМ ПРЕДЫДУЩИЙ КОД КРАСИВЕЕ:
# возьмем функцию select, которая принимает на вход функцию и какой-то набор данных, 
# формирует новый список и сразу его возвращает:
def select(f, col):
    return [f(x) for x in col]

# возьмем функцию where, которая принимает на вход функцию и какой-то набор данных, 
# формирует новый список и сразу его возвращает: 
def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data) #преобразовываем строки в числа
res = where(lambda e: not e % 2, res)
res = select(lambda x: (x, x**2), res)
print(res) # [(2, 4), (8, 64), (38, 1444)]