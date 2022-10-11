# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


def read_numbers(file):
    with open(file, 'r') as data:
        numbers = data.read()
    return [int(i) for i in numbers.split()]


file1 = 'Seminars/sem5_task1.txt'
temp_res = read_numbers(file1)
for i in range(1, len(temp_res)):
    if temp_res[i-1] != temp_res[i] - 1:
        print(temp_res[i-1] + 1)

print(temp_res)
