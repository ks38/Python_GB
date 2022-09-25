# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Enter X -> '))
y = int(input('Enter Y -> '))

if x > 0 and y > 0:
    print("It's a 1 quarter")
elif x < 0 and y > 0:
    print("It's a 2 quarter")
elif x < 0 and y < 0:
    print("It's a 3 quarter")
elif x > 0 and y < 0:
    print("It's a 4 quarter")
else:
    print("ERROR")

