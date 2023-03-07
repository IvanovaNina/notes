import actions


def choose_menu(choice):
    match choice:
        case 1:
            actions.index()
        case 2:
            actions.show()
        case 3:
            actions.create()
        case 4:
            actions.update()
        case 5:
            actions.delete()
        case 0:
            return True


def main_menu():
    print('Выберите команду меню')
    print('1. Показать заметки')
    print('2. Показать заметку')
    print('3. Добавить заметку')
    print('4. Изменить заметку')
    print('5. Удалить заметку')
    print('0. Выйти из приложения \n')


def input_menu():
    while True:
        # try:
        main_menu()
        choice = int(input(' Введите пункт меню: '))
        print(choice)
        if choice in range(1, 6) or choice == 0:
            if choose_menu(choice):
                return
        else:
            print('Такого пункта нет в меню. Внимательнее, пожалуйста: ')
        # except:
        #     print('Ошибка ввода')
