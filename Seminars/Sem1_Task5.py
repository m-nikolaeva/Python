# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 10 или 15, но не 30.

a = int(input('Введите число a '))
if (a % 10 == 0 or a % 15 == 0) and a % 30 != 0:  # не кратно 30
    print('Yes')
else:
    print('No')

# =================================================================

a = int(input('Введите число a '))
if (a % 10 == 0 or a % 15 == 0) and a != 30:  # не число 30
    print('Yes')
else:
    print('No')

# ==================================================================

# a = int(input("Введите число "))
# if a % 30 == 0 :
#     print("Число кратно 30, не подходит")
# elif a % 10 == 0 or a % 15 == 0:
#     print ('Число подходит')
# else:
#     print("Число совершенно не подходит!")

# ==================================================================

# a = int (input ("Введите 1 число "))
# if (a % 10 == 0 or a % 15 == 0) and a % 30 != 0:

#     print("Кратно")
# else:
#     print ("не кратно")