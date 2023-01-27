import model
import view

model.read_db('database.txt')


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_db('database.txt')
            view.db_success(model.db_list)
        case 3:
            view.save_contact()
       
        case 4:
            view.change_contact()
    
        case 5:
            view.show_all(model.db_list)
            view.delete_contact()

        case 6:
            view.find_contact()

        case 7:
            view.exit_prog()
    




def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
