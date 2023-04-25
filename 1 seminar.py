def level (A=0,B=0):
    if B==1:
        return A
    else:
        return A*level(A,B-1)    
    
def sum_recursion (A,B):
    if B==0:
        return A
    else:
        return 1+sum_recursion (A,B-1)    

def input_data (text="Введите два числа A B: "):
    Input=input(text)
    Input=Input.split()   
    Input.insert(0,0)
    for i in range(1,len(Input)):
        if not(Input[i].isdigit()):
            Input[0]=1
    return Input


# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
print("Задача 26")
Input26=input_data()
if Input26[0]==0 and len(Input26)==3:
    print(level(int(Input26[1]),int(Input26[2])))
else:
    print('Ошибка')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех 
# арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
print("Задача 28")
Input28=input_data()
if Input28[0]==0 and len(Input28)==3:
    print(sum_recursion(int(Input28[1]),int(Input28[2])))
else:
    print('Ошибка')