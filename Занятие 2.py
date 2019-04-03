#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

#def input_num(a,b,znak):
#    a1_b1_znak=input("Введите a, b, знак через ; (a;b;знак): ")
 #   a1=int(a1_b1_znak[0])
 #   b1=int(a1_b1_znak[1])
 #   znak=int(a1_b1_znak[2])
#    return [a,b,znak]

def check_znak(znak):
    if znak=="+" or znak=="-" or znak=="*" or znak=="/":
        znak_confirmed=True
    else:
        print("Введен неверный знак")
        znak_confirmed=True
    return znak_confirmed

def check_num(a,b):
    if a.isnumeric() == False:
        print ("a не число, повторите ввод")
        num_confirmed=False
    else:
        if b.isnumeric() == False:
            print ("b не число, повторите ввод")
            num_confirmed=False
        else:
            num_confirmed=True
    return num_confirmed


task_exist=True

while task_exist:
    a1_b1_znak=input("Введите a, b, знак через ; (a;b;знак): ").split(";")
    a1=a1_b1_znak[0]
    b1=a1_b1_znak[1]
    znak=a1_b1_znak[2]
    if znak=="0":
        task_exist=False
        print("Расчет закончен")
    else:
        znak_confirmed=check_znak(znak)
        if znak_confirmed:
            num_confirmed=check_num(a1,b1)
            if num_confirmed:
                if znak=="+":
                    print(int(a1)+int(b1))
                elif znak=="-":
                    print(int(a1)-int(b1))
                elif znak=="*":
                    print(int(a1)*int(b1))
                else:
                    if b1=="0":
                        print("Деление на 0 невозможно")
                    else:
                        print(int(a1)/int(b1))
        else:
            print("Введен неверный знак")

#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a2=input("Введите натуральное число: ")

num_chet=0
num_nechet=0


for i in range(0,len(a2)):
    if int(a2[i])%2==0:
        num_chet+=1
    else:
        num_nechet+=1

print("Нечетных цифр ", num_nechet)
print("Четных цифр ", num_chet)

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

a3=input("Введите число: ")
a3_rev=""

if a3[len(a3)-1]=="0":
    last_len=len(a3)-2
else:
    last_len=len(a3)-1

for i in range(last_len,-1,-1):
        a3_rev=a3_rev+a3[i]

print("Обратное число ", a3_rev)

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

a4=int(input("Введите нужное количество элементов: "))

sum_chet=0
sum_nechet=0

for i in range(1,a4+1):
    if i%2==1:
        sum_nechet=sum_nechet+1/2**(i-1)
    else:
        sum_chet+=1/2**(i-1)

print(sum_nechet-sum_chet)

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

razn=127-32
str_count=razn//10+1

cur_num_chr=32

for i in range(1,str_count+1):
    j=1
    cur_str=""
    while j<=10 and cur_num_chr<=127:
        cur_str=cur_str+str(cur_num_chr)+chr(cur_num_chr)+" "
        j+=1
        cur_num_chr+=1
    print(cur_str)

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

count_pop=1
answer_true=False

import random

write_answer=random.randint(1,100)
print(write_answer)

def check_user_answer(user_answer):
    local_answer_true=False
    if user_answer==write_answer:
        local_answer_true=True
        print("Верно!")
    elif user_answer<write_answer:
        print("Нужное число больше")
    else:
        print("Нужное число меньше")
    return local_answer_true

while count_pop<=10 and answer_true==False:
    print("Попытка ", count_pop)
    answer_true=check_user_answer(int(input("Число: ")))
    count_pop+=1

if answer_true==False:
    print("Правильный ответ был: ", write_answer)




