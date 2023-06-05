import text

def main_menu1() -> int:
    print(text.main_menu1)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice)<3:
            return int(choice)
def main_menu2() -> int:
    print(text.main_menu2)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice)<9:
            return int(choice)
def read_name_file ():
    file_name=input(text.input_file)
    return file_name

def done(don):
    if don: print(text.ready)
    else: print(text.err) 

def print_list(lis=[]):
    for i, val in enumerate(lis, start=1):
        print(f'№ {i}    {val}')

def input_data_contact():
    data_contact=list()
    data_contact.append(input("Введите ФИО:  "))
    data_contact.append(input("Введите телефон:  "))
    data_contact.append(input("Введите комментарий:  "))
    return data_contact

def search_contact():
    name_con=input(text.search_contact)
    return name_con

def orger_number():
    order=input(text.order_number)
    return order