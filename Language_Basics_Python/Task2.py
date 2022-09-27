# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]

# a = [2, 5, 8, 2, 12, 12, 4]
# b = [2, 7, 12, 3]

# for number in a[:]: #проходим по копии списка а, чтобы не потерять ни один элемент
#     if number in b:
#         a.remove(number)
# print(a)


# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. 
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года. 
# Склонением пренебречь (2000 года, 2010 года)

# date = '02.11.2013' 
# d, m, y = date.split('.') # разбиваем строку
# print(d, m, y)
# months = {          # создаем словари
#     '01': 'января',
#     '11': 'ноября'
# }
# days = {
#     '01': 'первое',
#     '02': 'второе'
# }
# result = f'{days[d]} {months[m]} {y} года'
# print(result)


# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет:
# [5, 8]


numbers = [2, 2, 5, 12, 8, 2, 12]

result = []    
for number in numbers:
    if numbers.count(number) == 1:    #.count - метод, который проверяет сколько раз число входит в список
        result.append(number) # в result добавляем число, которое повторяется 1 раз в списке
print(result)