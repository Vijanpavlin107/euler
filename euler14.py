from re import I


def next_in_colatz(x):
    if x%2==0:
        return x // 2
    else:
        return 3*x + 1


def len_colatz(n):
    dolzina = 1
    while n!= 1:
        n = next_in_colatz(n)
        dolzina += 1
    return dolzina


najdaljsa_dolzina = 0
najvecje_stevilo = 1

for i in range(1, 1000001):
    dolzina = len_colatz(i)
    if dolzina > najdaljsa_dolzina:
        najdaljsa_dolzina = dolzina
        najvecje_stevilo = i
    
print(najvecje_stevilo)
