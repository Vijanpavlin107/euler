#zacnem levo zgoraj
#20x20 grid
#lahko se premikam le desno in dol
#stevilo moznih poti
#na vsakem krizicu imam lahko 2 ali pa 1 moznost (ce sem ze na desnem ali spodnjem robu) ==> 
#moram simulirati?
#poskusim simulirat tako da najprej zacnem v (0,0) in preverim koliko je moznih premikov in nato rekurzivno za vsak mozni premik nazaj poklicem funkcijo
#break se zgodi ko pridem v (20, 20) takrat pristejem eno pot


# dimenzija = 20

# def possible_moves(x, y):
#     if x == dimenzija and y == dimenzija:
#         return 1
#     else:

#         poti = 0
#         if x < dimenzija:
#             poti += possible_moves(x+1, y)
#         if y < dimenzija:
#             poti += possible_moves(x,y+1)
        
#         return poti


# total = possible_moves(1,1)
# print(total)
#zgornja koda je veliko pre pocasna

#namig: problem se preveda na iskanje stevila moznosti razporeditve n elementov na 2n mest
#to je zato ker je v vsaki poti ocitno 2n premikov n izmed katerih je dol in n desno
#sledi da se da vse poti zapisati kot pozicije premikov dol / desno izmed 2n skupnih premikov
#to se izracuna: 2n! / (n! * n!)

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

def stevilo_moznih_poti(dim):
    izraz = factorial(dim * 2) / (factorial(dim)^2)
    return izraz

print(stevilo_moznih_poti(20))
