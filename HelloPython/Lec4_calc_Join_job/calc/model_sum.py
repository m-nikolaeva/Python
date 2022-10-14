x = 0
y = 0

def init(a, b): # метод, отвечающий за инициализацию(указание значений) начальных значений
    global x
    global y
    x = a
    y = b

def do_it(): # складывает значения
    return x + y