# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

num = input('Enter your number, mortal ->')
sum = 0
for i in num:
    if i != '.':
        sum += int(i)
print(sum)
