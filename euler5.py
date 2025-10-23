num = 2520
while True:
    for i in range(1, 21):
        if num % i != 0:
            num += 2520
            break
    else:
        print(num)
        break
