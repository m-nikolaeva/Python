# Шаг 1. Загадать случайное число +
import random

number = random.randint(1, 100)
print(number)

# Шаг 2. Предложить пользователю ввести число +
# user_number = int(input('Введите число: '))
# # Шаг 3. Сравнение чисел. Вывод результата +
# if number == user_number:
#     print('Победа')
# elif number < user_number:
#     print('Ваше число больше загаданного')
# else:
#     print('Ваше число меньше загаданного')
# Шаг 4. Для удобства пользователя сформируем бесконечный цикл
# while True:
#     user_number = int(input('Введите число: '))
#     if number == user_number:
#         print('Победа')
#         break
#     elif number < user_number:
#         print('Ваше число больше загаданного')
#     else:
#         print('Ваше число меньше загаданного')
# Шаг 5. Улучшаем цикл, выход из цикла по условию:
user_number = None
# Шаг 6. Усложняем. Добавляем и ограничиваем кол-во попыток.
count = 0
# Шаг 7. Добавляем уровни сложности. Возможность выбрать уровень.
levels = {1: 10, 2: 5, 3: 3} # уровни удобнее делать через словари
level = int(input('Выберите уровень сложности: '))
max_count = levels[level]
# Шаг 8. Добавляем кол-во игроков, ввод имен, систему поочередного хода, объявление победителя
user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя игрока {i}: ')
    users.append(user_name)
is_winner = False
winner_name = None
while not is_winner:
    count +=1
    if count > max_count:
        print('Все игроки проиграли')
        break
    print(f'Попытка №{count}')
    for user in users:
        print (f'Ход игрока {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'Победитель {winner_name}')


