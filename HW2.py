# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

n = float(input('Введите дробь: '))
n = n * 10
n = n % 10
if n != 0:
    print(int(round(n, 1)))
else:
    print('нет')