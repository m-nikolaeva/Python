# ====== ФУНКЦИЯ filter() --> применяет указанную функцию к каждому элементу и
# возвращает итератор с теми объектами, для которых функция вернула TRUE.========

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res) # [0, 2, 4, 6, 8]

##def select(f, col):  # заменим функцию select на map
##   return [f(x) for x in col]

## def where(f, col): # заменим функцию where на filter
##     return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data) #преобразовываем строки в числа
res = list(filter(lambda x: not x%2, res))
print(res) # [2, 8, 38]
res = list(map(lambda x: (x, x**2), res))
print(res) # [(2, 4), (8, 64), (38, 1444)]
