# ====== ФУНКЦИЯ map() --> применяет указанную функцию к каждому элементу и
# возвращает итератор с новыми объектами.===================================
# li = [x for x in range(1, 21)]
# print(li) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# li = list(map(lambda x: x + 10, li))
# print(li) # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
##при map() - нельзя пройтись по коду дважды, можно при: list(map(...))
# data = list(map(int, input().split())) #приведение данных к типу list(список), int - из строк в числа

# #def select(f, col):  # заменим функцию select на map
#  #   return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data) #преобразовываем строки в числа
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res) # [(2, 4), (8, 64), (38, 1444)]
