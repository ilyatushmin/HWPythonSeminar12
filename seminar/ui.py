from logger import input_data, print_data, delete_data, update_data


def interface():
    print("добрый день! вы попали в специальный бот \n 1 - запись данных  \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных")
    command = int(input('введите число '))
    while command != 1 and command != 2 and command != 3 and command != 4:
        print("неправильный ввод")
        command = int(input('введите число '))

    if command == 1:
        input_data()
        
    elif command == 2:
        print_data()
        
    elif command == 3:
        update_data()
        
    elif command == 4:
        delete_data()