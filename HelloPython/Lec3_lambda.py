# ПРОСТЫЕ КОНЕЧНЫЕ ФУНКЦИИ:

# def sum1(x):
#     return x + 10

# def sum2(x):
#     return x + 22

# def sum3(x):
#     return x + 242

# def mylt1(x):
#     return x**2

# def mylt2(x):
#     return x**3

# def mylt3(x):
#     return x**5

# sum1(mylt1(2))
# sum2(mylt2(2))
# sum3(mylt2(2))
# =============================================
# def f(x):
#     return x**2

# g = f # помещаем функцию в переменную
# print(type(f)) # <class 'function'>
# print(type(g)) # <class 'function'>
# print(f(4)) # 16
# print(g(4)) # 16 
# ============= =============== ============
# ПОМЕЩАЕМ ФУНКЦИЮ В ПЕРЕМЕННУЮ ----> 1 аргумент:
# def calc1(x):  #некая функция сложения
#     return x + 10
# print(calc1(10)) # 20

# def calc2(x):   #некая функция умножения
#     return x * 10
# print(calc2(10)) # 100

# def math(op, x): #функция, принимающая некую функцию и аргумент
#     print(op(x))

# math(calc2, 10) # 100
# math(calc1, 10) # 20

# ========== ============ ========== ============
# ПОМЕЩАЕМ ФУНКЦИЮ В ПЕРЕМЕННУЮ ----> 2 аргумента:
# def sum1(x, y):   #некая функция сложения
#     return x + y

# def mylt1(x, y): #некая функция умножения
#     return x * y

def calc(op, x, y): #функция, принимающая некую функцию и два аргумента
    print(op(x, y))
    # return op(x, y)

# calc(mylt1, 4, 5) # 20

# LAMBDA =======================================
# результат по итогу один:
# def sum1(x, y):   
#     return x + y
# f = lambda q, w: q + w
# sum = lambda x, y: x + y

# calc(sum1, 4, 5) # 9
# calc(f, 4, 5) # 9
# calc(sum, 4, 5) # 9

# НО!!! МОЖНО БЕЗ ИСПОЛЬЗОВАНИЯ ЛИШНИХ ПЕРЕМЕННЫХ:
calc(lambda x, y: x + y, 4, 5) # 9