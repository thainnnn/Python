n = int(input())
for i in range(n):
    t = i
    for i in range(1, i):
        if(i % i == 0):
            print(i, end = ' ')
    print(n)
