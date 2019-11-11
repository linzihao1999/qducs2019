import random

num = random.randint(0, 300)
a = -1
while a != num:
    a = int(input('input:'))
    if a > num:
        print('Big')
    elif a < num:
        print('Small')
    else:
        print('yes')
