# Задача № 30 Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a1 = int(input('Введите число А1: '))
d = int(input('Введите шаг прогрессии: '))
n = int(input('Введите длину списка: '))

progression = []
for i in range(1, n + 1):
    el = a1 + (i - 1) * d
    progression.append(el)
print(f'Ваш массив арифметической прогрессии: {progression}')

