# Задача №32 Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint

n = int(input('Введите число элементов массива: '))
min = int(input('Введите минимальное значение заданного диапазона: '))
max = int(input('Введите максимальное значение заданного диапазона: '))

my_lst = []
for i in range(n):
    my_lst.append(randint(-10, 11))
print(f'Заданный массив: {my_lst}')

sorted_lst = []
for i in range(len(my_lst)):
    if my_lst[i] >= min and my_lst[i] <= max:
        sorted_lst.append(i)

print(f'Элементы массива в заданном диапазоне: {sorted_lst}')
