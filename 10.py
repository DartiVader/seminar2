n = int(input())
counter_1 = 0
counter_0 = 0
for i in range(n):
    m = int(input())
    if m == 1:
        counter_1 += 1
    elif m == 0:
        counter_0 +=1
    else:
        print('Введено некоректное значение')
        break
if counter_0 < counter_1:
    print(counter_0)
else: 
    print(counter_1)