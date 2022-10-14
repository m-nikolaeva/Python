# controller - связующее звено интерфейса(view) и модуля
from statistics import mode
import  model_sub as model
import view

def button_click(): # "кнопка" для пользователя
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, "result")