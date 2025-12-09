


def next_in_colatz(x):
    if x%2==0:
        return x // 2
    else:
        return 3*x + 1


def len_colatz(n):
    initial_num = n
    dolzina = 0
    while n != 1:
        if n in spomin:
            dolzina += spomin[n]
            n = 1
        else:
            n = next_in_colatz(n)
            dolzina += 1
    
    spomin[initial_num] = dolzina
    return (initial_num, dolzina)


spomin = {1:1, 2:2}


#morem implementirat cachanje
naj_dolzina = 1
naj_stevilo = 1

# rez = len_colatz(234)
# print(type(rez[0]))

for i in range(1000001):
    rez = len_colatz(i)
    if rez[1] > naj_dolzina:
        naj_dolzina = rez[1]
        naj_stevilo = rez[0]

print(naj_dolzina, naj_stevilo)