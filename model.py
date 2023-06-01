import os.path
import view
phones=[]

# 1. Открыть файл 
def open_file ():
    file_name=view.read_name_file ()
    file =os.path.exists(file_name)
    if file:
        global phones
        f = open(file_name, 'r')
        phones=(f.readlines())
        phones=list(map(lambda x: x[:-1] ,phones ))                 
        f.close()
        view.done(True)
        return True
    else:
        view.done(False) 
        return False
    
# 2. Сохранить файл
def save_file ():
    lis=phones

    file =os.path.exists(view.file_name)
    if file:
        lis=list(map(lambda x:x+"\n",lis))
        lis=''.join(lis)
        f = open(view.file_name, 'w')
        f.write(lis)
        f.close()
        view.done(True)
        return True
    else: 
        view.done(False)
        return False
    
# 3. Показать все контакты
def print_file (list_name=phones):
    f=list(map(lambda x : x.replace(',',' '),list_name))
    view.print_list(f)

# 4. Добавить контакт
def add_contact():
    data_contact=list(view.input_data_contact())
    contact=(f'{data_contact[0]},{data_contact[1]},{data_contact[2]}')
    phones.append(contact)
    view.done(True)

# 5. Найти контакт
def search_contact ():
    name=view.search_contact()
    res=list()
    for i in range(len(phones)):
        con=phones[i].split(",")      
        if name in con[0]:
            res.append(f'№{i+1}    {phones[i]}')
    print_file (res)
    if len(res)==0:view.done(False)
    else:view.done(True)
    
# 6. Изменить контакт
def edit_contact():
    number=view.orger_number()
    data_contact=list(view.input_data_contact())
    if (int(number)<=len(phones)):
        phones[int(number)-1]=(f'{data_contact[0]},{data_contact[1]},{data_contact[2]}')
        view.done(True)
    else: view.done(False)
        

# 7. Удалить контакт
def pop_contact():
    number=view.orger_number()
    if (int(number)<=len(phones)):
        phones.pop(int(number)-1)
        view.done(True)
    else: view.done(False)