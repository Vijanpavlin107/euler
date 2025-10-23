#find the 10001st prime number

seznam = list(range(3, 200000, 2))
num = 0
for i in range(10009):
    stevilo = seznam[0]
    print(stevilo)
    print('index stevila je:', num)
    num += 1
    for j in seznam:
        if j % stevilo == 0:
            seznam.remove(j)

