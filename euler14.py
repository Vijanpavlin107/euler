

# pre pocasno ker cacham vsako vrednost ??
# def next_in_colatz(x):
#     if x%2==0:
#         return x // 2
#     else:
#         return 3*x + 1


# def len_colatz(n):
#     initial_num = n
#     dolzina = 0
#     while n != 1:
#         if n in spomin:
#             dolzina += spomin[n]
#             n = 1
#         else:
#             n = next_in_colatz(n)
#             dolzina += 1
    
#     spomin[initial_num] = dolzina
#     return (initial_num, dolzina)


spomin = {1:1}
def dolzina_colatz(n):
    original = n
    pot = []

    while n not in spomin:
        pot.append(n)

        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1

    dolzina = spomin[n]
    for vrednost in reversed(pot):
        dolzina += 1
        spomin[vrednost] = dolzina
        
    return spomin[original]


 


#morem implementirat cachanje
naj_dolzina = 1
naj_stevilo = 1

# rez = len_colatz(234)
# print(type(rez[0]))

for i in range(1, 1000001):
    rez = dolzina_colatz(i)
    if rez > naj_dolzina:
        naj_dolzina = rez
        naj_stevilo = i 

print(naj_dolzina, naj_stevilo)