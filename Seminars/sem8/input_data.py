from contacts_op import write_contact


def add_contact(data, columns):
    print('Внесите данные нового контакта: ')
    flag = True
    while flag:
        user = {}
        for column in columns:
            user[column] = input(column + ': ')
        confirm = input('\nНажмите 1 для сохранения или любую клавишу для возврата в меню: ')
        if confirm == '1':
            write_contact(user, data)
        flag = False

    
def input_column():
    return input('Введите название нового столбца: ')
