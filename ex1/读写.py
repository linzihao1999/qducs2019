l = ['GOOGLE Inc', 'Microsoft Corporation', 'Apple Inc', 'Facebook']
with open(r'./companies.txt', 'w') as f:
    for i in l:
        f.write(i + '\n')
with open(r'./scompanies.txt', 'w') as f:
    for num, i in enumerate(l):
        f.write(str(num) + ' ' + i + '\n')
