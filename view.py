def main_menu() -> int:
    print('Главное меню ')
    menu_list = ['Показать все контакты',
                 'Открыть файл ',
                 'Создать и сохранить контакт',
                 'Изменить контакт ', 
                 'Удалить контакт ',
                 'Найти контакт ', 
                 'Выход',
                ]
    for i in range(len(menu_list)):
        print(f'    {i+1}.{menu_list[i]}')
    user_input = int(input('Введите команду >: '))
    return user_input
    
    


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end= '. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()

def db_success(db: list):
    if db:
        print('Телефоннная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False

def exit_prog():
    print('Завершение программы.')
    exit()


    
def save_contact():
    array = input('Введите фамилию, имя, номер и комметарий к новому контакту через «;» >: ')  
    my_file = open('database.txt', 'a', encoding='UTF-8')
    text_for_file =  array
    my_file.write('\n')
    my_file.write(text_for_file)
    my_file.close()
    print('Контакт успешно добавлен в телефонную книгу')


def find_contact():
    fnd = input('Введите фимилию контакта, который хотите найти  >: ')
    with open('database.txt', mode='r', encoding='UTF-8') as file:
        lst = file.readlines()    
        for i in lst: 
            if fnd in i: 
                print(i)
                break 
        if not fnd in i: 
            print('Нет такого контакта')



def delete_contact():
    with open('database.txt', encoding='UTF-8') as file:
        text = file.read()
    old = input('Введите полностью контакт, который хотите удалить  >: ')

    forbidden = (' ')
    for i in old:
        if i in forbidden:
            old = old.replace(i, ';')

    text = text.replace(old, ' ')

    with open('database.txt', "w", encoding='UTF-8') as file:
        file.write(text)
    print('Контакт удалён') 



def change_contact():
    with open('database.txt', encoding='UTF-8') as file:
        text = file.read()
    old = input('Введите какой элемент хотите заменить >: ')
    new = input('Введите замену >: ')
    text = text.replace(old, new)

    with open('database.txt', "w", encoding='UTF-8') as file:
        file.write(text)
    print('Изменения успешно внесены')

