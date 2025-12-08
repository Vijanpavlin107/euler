


def next_in_colatz(x):
    if x%2==0:
        return x // 2
    else:
        return 3*x + 1


def len_colatz(n):
    intial_num = n
    dolzina = 0
    while n != 1:
        if n in spomin:
            dolzina += spomin[n]
            n = 1
        else:
            n = next_in_colatz(n)
            dolzina += 1
    
    spomin[intial_num] = dolzina
    return dolzina


spomin = {1:1, 2:2}

# najdaljsa_dolzina = 0
# najvecje_stevilo = 1

# for i in range(1, 1000001):
#     dolzina = len_colatz(i)
#     if dolzina > najdaljsa_dolzina:
#         najdaljsa_dolzina = dolzina
#         najvecje_stevilo = i
    

#morem implementirat cachanje

print(len_colatz(1000000))
