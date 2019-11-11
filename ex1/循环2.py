import random

num = random.randint(0, 300)
a = -1
while a != num:
    a = input('input(\'q\' to quit):')
    if a == 'q':
        break
    else:
        a = int(a)
    if a > num:
        print('Big')
    elif a < num:
        print('Small')
    else:
        print('yes')
