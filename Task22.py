'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''

from random import randint

def rand_fill(len1):
    return [randint(1,100) for i in range(len1)]

def manual_fill(len1):
    list1 = []
    for i in range(len1):
        list1.append(int(input()))
    return list1

try:
    print("Меню: \n 1 - автоматическое заполнение; \n 2 - ручное заполнение.")
    menu = int(input())
    if menu > 2:
        raise Exception("")
    n, m = int(input("Введите размерность 1 списка: ")), int(input("Введите размерность 2 списка: "))
    if menu == 1:
        list_n = rand_fill(n)
        list_m = rand_fill(m)
    elif menu == 2:
        print(f"Введите значения для 1 списка ")
        list_n = manual_fill(n)
        print(f"Введите значения для 2 списка ")
        list_m = manual_fill(m)

    print(f"1 список: {list_n}")
    print(f"2 список: {list_m}")
    print(f"Ответ: \n{sorted(list(set(list_n).union(set(list_m))))}")
except:
    print("Error! Некорректный ввод данных")


