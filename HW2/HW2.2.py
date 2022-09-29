# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

array = []

x = int(input('Enter digit -> '))
factorial = 1
for i in range(1, x + 1):
    factorial *= i
    array.append(factorial)
print(array)
