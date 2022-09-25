# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('enter x-> '))
y = int(input('enter y-> '))
z = int(input('enter z-> '))

left_side = not (x or y or z)
right_side = not x and not y and not z
result = left_side == right_side

if result:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

########################################################################
# 2 решение:
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)