def flip(x):
    dolzina = len(str(x))
    digits = []
    for i in range(dolzina):
        digits.append(x%10)
        x = x // 10
    
    stevilo = 0
    i = dolzina -1
    for el in digits:
        stevilo += el * 10**i
        i -= 1
        
        

    return stevilo

pali = 0

for i in range (100, 1000):
    for j in range (100, 1000):
        x = i * j
        if x == flip(x) and x >= pali:
            pali = x
    
print(pali)

        
