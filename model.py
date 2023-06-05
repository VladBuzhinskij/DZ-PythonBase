import os.path
import view
class PhoneBook:
    def __init__(self,file_name: str='') :
        self.phones = []
        self._file_name = file_name

    # 1. Открыть файл 
    def open_file (self):
        file =os.path.exists(self._file_name)
        if file:
            f = open(self._file_name, 'r')
            self.phones=(f.readlines())
            self.phones=list(map(lambda x: x[:-1] ,self.phones ))                 
            f.close()
            return True
        else: return False
            
        
# 2. Сохранить файл
    def save_file (self):
        lis=self.phones
        file =os.path.exists(self._file_name)
        if file:
            lis=list(map(lambda x:x+"\n",lis))
            lis=''.join(lis)
            f = open(self._file_name, 'w')
            f.write(lis)
            f.close()
            return True
        else: 
            return False
    
    # 3. Показать все контакты
    def print_file (self, list_name):
        f=list(map(lambda x : x.replace(',',' '),list_name))
        return f

    # 4. Добавить контакт
    def add_contact(self, data_contact):
    
        contact=(f'{data_contact[0]},{data_contact[1]},{data_contact[2]}')
        self.phones.append(contact)
    

    # 5. Найти контакт
    def search_contact (self, name):
        res=list()
        for i in range(len(self.phones)):
            con=self.phones[i].split(",")      
            if name in con[0]:
                res.append(f'№{i+1}    {self.phones[i]}')
        self.print_file (res)
        if len(res)==0:return True
        else:return False
        
    # 6. Изменить контакт
    def edit_contact(self, number,data_contact):
        if (int(number)<=len(self.phones)):
            self.phones[int(number)-1]=(f'{data_contact[0]},{data_contact[1]},{data_contact[2]}')
            return True
        else: return False
            

    # 7. Удалить контакт
    def pop_contact(self, number):
        if (int(number)<=len(self.phones)):
            self.phones.pop(int(number)-1)
            return True
        return False