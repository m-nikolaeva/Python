# Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослечайных чисел

import time

now = time.time()
print(now)
print(str(now).split('.')[1][0])