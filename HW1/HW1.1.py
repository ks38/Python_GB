# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет


day = int(input('Enter day number -> '))

if day not in range(1, 8):
    print('error')
elif day in range(1, 5):
    print('будний день :(')
    if day == 1:
        print('Monday')
    elif day == 2:
        print('Tuesday')
    elif day == 3:
        print('Wednsday')
    elif day == 4:
        print('Thursday')
    elif day == 5:
        print('Friday')
elif day in range(6, 8):
    print("Rock'n'Roll!")
    if day == 6:
        print('Saturday')
    elif day == 7:
        print('Sunday')

################################################
# 2 вариант:
# day = int(input('Enter day number -> '))
#
# if day == 7 or day == 8:
#     print('Workday')
# elif day >= 1 or day < 7:
#     print('Weekend')
# else:
#     print('You entered incorrect date')
