# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

ent_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", ent_list)
n = '0'
print(ent_list.count(n)) # Выводит количество вхождений
count = 0
if ent_list.count(n) >= 2:
    for i in range(len(ent_list)):
        if ent_list[i] == n:
            count += 1
        if count == 2:
            print(f'Индекс второй позиции {i}')
else:
    print('Второй позиции нет.')


from itertools import count


# input_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# my_str = "1qwe"
# count1 = 0
# for i, el in enumerate(input_list): # будет выдавать кортежи (индекс и значение)
#     if my_str == el:
#         count1 += 1
#     if count1 == 2:
#         print(i)
#     if count1 < 2:
#         print("-1")