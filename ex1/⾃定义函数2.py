def pri(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


for i in range(1, 101):
    if pri(i):
        print(i)
