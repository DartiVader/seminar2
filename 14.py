n = int(input())
i = 0
a = 0
while a <= n:
    a = 2**i
    i+=1
    if a > n:
        break
    print(a)