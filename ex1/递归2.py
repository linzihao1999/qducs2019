def haoi(a, b, c, k):
    if k == 1:
        print(a + '->' + c)
    else:
        haoi(a, c, b, k - 1)
        print(a + '->' + c)
        haoi(b, a, c, k - 1)


n = int(input())
haoi('a', 'b', 'c', n)
