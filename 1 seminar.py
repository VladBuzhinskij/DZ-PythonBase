# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите 
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той 
# же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
print("Задача 10")
Input10=input("Введите количество монет n: " )
while not(Input10.isdigit()):
    Input10=input("ведите количество монет n:" )
List1=[]
Hands,Tails=0,0
for i in range(0,int(Input10)):
    List1.append(bool(random.getrandbits(1)))
print(List1)
for i in List1:
    if i: Hands+=1
else: Tails+=1
# print(Hands) if Hands>Tails else print(Tails)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две 
# подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# print("Задача 12")
# sum =x+y p=x*y x=sum-y , x=p/y sum-y-p/y=0 sum-p/y=y sum*y-p=y^2     y^2-sum*y+p

print("Задача 12")
Input12=input("Введите сумму и произведение чисел: " )
array = Input12.split()
if len(array)==2:
    if  array[0].isdigit() and array[1].isdigit():
        b=float(array[0])
        c=float(array[1])
        D=(b**2)-4*c
        if D>0:
            x1=((b)+(D**0.5))/2
            x2=((b)-(D**0.5))/2
            print (f'x={x1}  y= {x2}=')
        elif D==0:
            x1=((b)+(D**0.5))/2
            print (f'x={x1}')
        elif D<0:print("Ошибка")
    else: print('Ошибка')
else: print('Ошибка')
    
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print("Задача 14")
Input14=input("Введите число N: " )
while not(Input14.isdigit()):
    Input14=input("Ведите число N" )
N=int(Input14)
if N>2:
    res=2
    print(res) 
    while res*2<N:
       res*=2
       print(res)
else: print('число слишком мало')
