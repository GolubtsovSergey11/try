documents = [
        {"type": "passport", "number": "2207 876234", "names": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "names": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "names": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def start_programm():
    print('''Список команд:
            'P' - спросит номер документа и выведет имя человека, которому он принадлежит;
             'S' - которая спросит номер документа и выведет номер полки, на которой он находится;
             'L' - которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
             'A' - которая добавит новый документ в каталог и в перечень полок, спросив его номер,
             тип, имя владельца и номер полки, на котором он будет храниться.
             'X' - если хотите выйти из программы''')
    while True:
        comands = input("Bведите команду: ").upper()
        if comands == 'P':
            peoples(documents)
        elif comands == 'S':
            shelf(directories)
        elif comands == 'L':
            document(documents)
        elif comands == 'A':
            add(documents, directories)
        elif comands == 'X':
            print('Вы завершили программу.')
            break
        else:
            print('Вы ввели не существующую команду.')


def show_names(name):
    for item in name:
        try:
            if 'name' not in item['name']:
                print(item['name'])
        except KeyError:
            print('No name')
            break


def peoples(people):
    while True:
        number_doc = input('Введите номер документа: ')
        for name in people:
            if number_doc == name['number']:
                return print(f'Документ с номером {number_doc} принадлежит {name["name"]}')
        else:
            print('Несуществующий документ.')


def shelf(number_shelf):
    while True:
        number_doc = input('Введите номер документа: ')
        for key, value in number_shelf.items():
            if number_doc in value:
                return print(f'Документ с номером {number_doc} находится на полке {key}')
        else:
            print('Несуществующий документ.')

def document(list_of_documents):
    print('Список всех документов:')
    a = 0
    for doc in list_of_documents:
        a += 1
        print(f'{a}) {doc["type"]} {doc["number"]} {doc["name"]};')

def add(add_documents, add_shelf):
    new_vocabulary = {'type': '', 'number': '', 'name': ''}
    new_vocabulary['type'] = input('Введите тип документа: ')
    new_vocabulary['number'] = input('Введите номер документа: ')
    new_vocabulary['name'] = input('введите имя: ').title()
    add_documents.append(new_vocabulary)
    print(f'Пользователь с именим {new_vocabulary["name"]} добавлен в базу данных')

    while True:
        add_in_shelf = input('введите номер полки: ')
        if add_in_shelf in add_shelf.keys():
            add_shelf[add_in_shelf].append(new_vocabulary['number'])
            print(f'Пользователь {new_vocabulary["name"]} добавил документ с номером {new_vocabulary["number"]} '
                f'на полку № {add_in_shelf}')
            break
        if add_in_shelf not in add_shelf.keys():
            print('Такой полки нету')

start_programm()

show_names(documents)
