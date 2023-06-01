import view
import model
def start1():
    while True:
        choice=view.main_menu1()



        match choice:
            case 1:
                
                if model.open_file(): start2()
          
            case 2:
                break

def start2():
    while True:
        choice=view.main_menu2()



        match choice:
            case 1:
                model.save_file()
            case 2:
                model.print_file ()
            case 3:
                model.add_contact()
            case 4:
                model.search_contact ()
            case 5:
                model.edit_contact()
            case 6:
                model.pop_contact()  
            case 7:
                break