# Напишите программу, которая на вход принимает 5 чисел (можно списком)
# и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
# c = int(input('Введите третье число '))
# d = int(input('Введите четвертое число '))
# e = int(input('Введите пятое число '))
# numbers = [a, b, c, d, e]
# max_num = numbers[0]
# for i in numbers:
#     if i > max_num:
#         max_num = i
# print('Максимальное число', max_num)

# ======================================================

# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
# c = int(input('Введите третье число '))
# d = int(input('Введите четвертое число '))
# e = int(input('Введите пятое число '))
# numbers = [a, b, c, d, e]
# max_num = numbers[0]
# for i in range(1, 5):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
# print('Максимальное число', max_num)

# ========================================================

# list = [3, 6, 54, 10, 12]
# max_num = list[0]

# for i in list:
#     if i > max_num:
#         max_num = i
# print(max_num)

# ========================================================

entered_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", entered_list)
num_list = list(map(int, entered_list))
print("Список чисел: ", num_list)
print("Максимальное число списка:", max(num_list))
