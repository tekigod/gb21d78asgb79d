# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def summ_my_list(my_list):
    summ = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            summ += my_list[i]
    return summ

from random import randint
my_list = []
for i in range(5): 
    my_list.append(randint(0, 16)) 

print(my_list)
print(f'На нечётных позициях элементы {my_list[1]} и {my_list[3]}, ответ: {summ_my_list(my_list)}')