import math
from pickle import TRUE

def tri_num_gen(n):
    return n * (n + 1) // 2

def count_divisors(n):
    if n <= 1:
        return 1
    cnt = 1
    x = n
    d = 2
    while d * d <= x:
        exp = 0
        while x % d == 0:
            x //= d
            exp += 1
        if exp:
            cnt *= (exp + 1)
        d += 1 if d == 2 else 2
    if x > 1:
        cnt *= 2
    return cnt

a = 1
while True:
    t = tri_num_gen(a)
    if count_divisors(t) > 500:
        print(a, t)  # index and triangular number
        break
    a += 1







#no ai solution
def faktorizationation(n):
    current_num = 2 #prvo stevilo s katrim delimo
    factorizacija = []
    x = n

    if n <= 1:
        return 1
    
    while x > 1:
        current_num_exp = 0
        while x % current_num == 0:
            current_num_exp += 1
            x = x / current_num
        
        factorizacija.append((current_num, current_num_exp))
        current_num += 1

    return factorizacija


#vsako prastevilo v faktorizaciji lahko zavzame exponente od 0 do maximuma ki ga doloca faktorizacija
#za eno prastevilo p v faktorizaciji ki ima v faktorizaciji exponent n obstaja n+1 deliteljev (1, p, p*p, p*p*p,..)
#za dve so vse kombinacije 



def st_deiteljev(x):
    return math.prod([i[0] + 1 for i in x])

x = 2
while True:
    if st_deiteljev(faktorizationation(tri_num_gen(x))) >= 500:
        print(st_deiteljev(faktorizationation(tri_num_gen(x)))) 
        break
    x += 1