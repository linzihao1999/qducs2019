a = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
b = ['Saturday', 'Sunday']
for i in b:
    a.append(i)
for i, j in enumerate(a):
    print(str(i) + ' ' + j)
