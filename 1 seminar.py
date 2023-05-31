# 1. Открыть файл 
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход
import os.path
phones=[]

# 1. Открыть файл 
def open_file (file_name):
    file =os.path.exists(file_name)
    if file:
        global phones
        f = open(file_name, 'r')
        phones=(f.readlines())
        phones=list(map(lambda x: x[:-1] ,phones ))                 
        f.close()
        return True
    else: return False

# 2. Сохранить файл
def save_file (file_name,lis=[]):
    file =os.path.exists(file_name)
    if file:
        lis=list(map(lambda x:x+"\n",lis))
        lis=''.join(lis)
        f = open(file_name, 'w')
        f.write(lis)
        f.close()
        return True
    else: return False

# 3. Показать все контакты
def print_file ():
    f=list(map(lambda x : x.replace(',',' '),phones))
    for i, val in enumerate(f, start=1):
        print(f'№ {i}    {val}')

# 4. Добавить контакт
def add_contact(name,phone,comm):
    contact=(f'{name},{phone},{comm}')
    phones.append(contact)

# 5. Найти контакт
def search_contact (name):
    res=list()
    for i in range(len(phones)):
        con=phones[i].split(",")      
        if name in con[0]:
            res.append(f'№{i+1}    {phones[i]}')
    f=list(map(lambda x : x.replace(',',' '),res))  
    for i in f:print(i)
    return res

# 6. Изменить контакт
def edit_contact(number,new_name,new_phone,new_comm):
    if (int(number)<=len(phones)):
        phones[int(number)-1]=(f'{new_name},{new_phone},{new_comm}')
        return True
    else:return False
  
# 7. Удалить контакт
def pop_contact(number):
    if (int(number)<=len(phones)):
        phones.pop(int(number)-1)
        return True
    else: return False

# 8. Выход


start=True
while start:
    status=input("Введите '1', чтобы открыть файл или '0'чтобы выйти из программы: ")
    if status=="1":
        file_name=input("введите имя файла: ")
        if open_file (file_name):
            print("Файл открыт")
            start1=True
            while start1:
                status1=input("Введите '1', чтобы сохранить файл \nВведите '2', чтобы показать все контакты\nВведите '3', чтобы добавить контакт\nВведите '4', чтобы найти контакт\nВведите '5', чтобы изменить контакт\nВведите '6', чтобы удалить контакт\nВведите '7', чтобы вернуться в предыдущее меню:  ")
                if status1=="1":
                    print("Сохранение файла")
                    save_file (file_name,phones)
                elif status1=="2":
                    print("Все контакты")
                    print_file ()
                elif status1=="3":
                    print("Добавление контакта")
                    name=input("Введите ФИО:  ")
                    phone=input("Введите телефон:  ")
                    comm=input("Введите комментарий:  ")
                    add_contact(name,phone,comm)
                elif status1=="4":
                    print("Поиск контакта")
                    name=input("Введите ФИО полостью или частично:  ")
                    search_contact (name)
                elif status1=="5":
                    print("Изменение контакта")
                    number=input("Введите порядковый номер контакта:  ")
                    new_name=input("Введите ФИО:  ")
                    new_phone=input("Введите телефон:  ")
                    new_comm=input("Введите комментарий:  ")
                    if edit_contact(number,new_name,new_phone,new_comm): print("Изменение внесены")
                    else: print("Ошибка")    
                elif status1=="6":
                    print("Удаление контакта")
                    number=input("Введите порядковый номер контакта:  ")
                    if pop_contact(number): print("контакт удален")
                    else: print("Ошибка")
                elif status1=="7":
                    print("Возврат к предыдущему меню")
                    start1=False
        else: print("Файла не существует")
    elif status=="0": start=False



