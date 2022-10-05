# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python (например, numpy.roots)

# import numpy as np
# p = [1, 5, 6]
# roots = np.roots(p)
# print(roots)

a = float(input("Введите число A: "))
b = float(input("Введите число B: "))
с = float(input("Введите число C: "))
discr = (b ** 2) - (4 * a * с)
print(discr)
if discr > 0:
    x1 = round((-b + ((discr) ** 0.5)) / (2 * a), 2)
    x2 = round((-b - ((discr) ** 0.5)) / (2 * a), 2)
    print(x1, x2)
elif discr == 0:
    x1 = round(-b / (2 * a), 2)
    print(x1)
elif discr < 0:
    print('Нет корней')


# a, b, c = list(map(int, input('Введите три числа через пробел: ').split())) # Сами распакуются
# d = b ** 2 - 4 * a * c
# if d > 0:
#     print((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))
# elif d == 0:
#     print(-b / (2 * a))
# else:
#     print('Корней нет.')