# Задача 2: Найдите сумму цифр трехзначного числа.
print("Задача 2")
Input1=input("введите трехзначное число: " )
while not(Input1.isdigit()and len(Input1)==3):
    Input1=input("введите трехзначное число:" )
Suma=int(0)
for i in Input1:
    Suma+=int(i)
print(Suma)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print("Задача 4")
Input2=input("Введите количество журовликов: " )
while not(Input2.isdigit()):
    Input2=input("Введите количество журовликов:" )
Input2=int(Input2)
if Input2%6!=0:
    print('Ошибка')
else:
    print(f'{Input2//6}  {(Input2//6)*4}  {Input2//6}')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали 
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых 
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

print("Задача 6")
Input3=input("введите номер билета: " )
while not(Input3.isdigit()): Input3=input("введите номер билета:" )
if len(Input3)==6 :
    SumLeft = int(0)
    SumRight = int(0)
    for i in Input3[0:3]:SumLeft+=int(i)   
    for i in Input3[3:6]:SumRight+=int(i)   
    if SumLeft==SumRight: print('yes')    
    else: print('no')     
else: print('no')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print("Задача 6")
Input4=input("введите n m k: " )
array = Input4.split()
if len(array)==3:
    if  array[0].isdigit()and array[1].isdigit() and array[2].isdigit():
        for i in range(0,3):     array[i]=int(array[i])
        if   (array[2] % array[0]==0 or array[2] % array[1]==0) and array[0]*array[1]>array[2]:
            print('yes')
        else: print('no')           
    else: print('Ошибка')
else: print('Ошибка')