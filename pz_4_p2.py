#Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
#деления определить, имеется ли в записи числа N цифра «2». Если имеется, то
#вывести TRUE, если нет — вывести FALSE.

n = input('Введите целое число: ')

while type(n) != int: # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число: ")

t = False

while n > 1:
    if n % 10 == 2:
        t = True
    n = n // 10

if t:
    print(t, ', в записи числа имеется цифра "2"')
else:
    print(t, ', в записи числа нет цифры "2"')