from random import randint
def input_data (text="Введите два числа A B: "):
    Input=input(text)
    Input=Input.split()   
    Input.insert(0,0)
    for i in range(1,len(Input)):
        if not(Input[i].isdigit()):
            Input[0]=1
    return Input

def rand_array (min=0,max=10,count=10):
    array=[]
    for i in range(0,count):
        array.append(randint(min,max))
    return array

def range_array (arr=[],min=0,max=10):
    res_arr=[]
    for i in range(0,len(arr)):
        if arr[i]>=min and arr[i]<=max:
            res_arr.append(i)
    return res_arr

def ariphmetic_prog(a1,d,count):
    res=[]
    for i in range (1,count+1):
        res.append(a1+(i-1)*d)
    print(res)
    return res



# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
print("Задача 30")
a1=input("Введите a1: ")
while not(a1.isdigit()):
    a1=input("Введите a1: ")
d=input("Введите d: ")
while not(d.isdigit()):
    d=input("Введите d: ")
count=input("Введите количество элементов: ")
while not(count.isdigit()):
    count=input("Введите количество элементов: ")
ariphmetic_prog(int(a1),int(d),int(count))


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
print("Задача 32")
Input32=input_data("Введите границы диапазона: ")
rand_arr=rand_array ()
print(rand_arr)
if Input32[0]==0 and len(Input32)==3:
    if Input32[1]>Input32[2]:
        print(range_array(rand_arr,int(Input32[2]),int(Input32[1])))   
    elif Input32[1]<Input32[2]:
        print(range_array(rand_arr,int(Input32[1]),int(Input32[2])))
    elif Input32[1]==Input32[2]:
        print('нет элементов удовлетворяющих требованиям')
        

