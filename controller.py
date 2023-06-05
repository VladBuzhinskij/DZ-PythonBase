import view
import model
my_pb=model.PhoneBook()

def start1():
    while True:
        choice=view.main_menu1()


        match choice:
            case 1:
                my_pb._file_name=view.read_name_file()
                if my_pb.open_file(): 
                    view.done(True)
                    start2()
                else: view.done(False)
            case 2:
                break

def start2():
    while True:
        choice=view.main_menu2()


        match choice:
            case 1:
                if my_pb.save_file(): view.done(True)
                else: view.done(False)
            case 2:
                f=list(my_pb.print_file (my_pb.phones))
                view.print_list(f)
            case 3:
                my_pb.add_contact(list(view.input_data_contact()))
                view.done(True)
            case 4:
                if my_pb.search_contact (view.search_contact()): view.done(True)
                else: view.done(False)

            case 5:
                if my_pb.edit_contact(view.orger_number(),list(view.input_data_contact())): view.done(True)
                else: view.done(False)
            case 6:
                if my_pb.pop_contact(view.orger_number()): view.done(True)
                else: view.done(False)
            case 7:
                break