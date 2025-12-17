#zacnem levo zgoraj
#20x20 grid
#lahko se premikam le desno in dol
#stevilo moznih poti
#na vsakem krizicu imam lahko 2 ali pa 1 moznost (ce sem ze na desnem ali spodnjem robu) ==> 
#moram simulirati?
#poskusim simulirat tako da najprej zacnem v (0,0) in preverim koliko je moznih premikov in nato rekurzivno za vsak mozni premik nazaj poklicem funkcijo
#break se zgodi ko pridem v (20, 20) takrat pristejem eno pot


dimenzija = 20

def possible_moves(x, y):
    if x == dimenzija and y == dimenzija:
        print("hit")
        return 1
    
    poti = 0
    if x < dimenzija:
        print('X')
        poti += possible_moves(x+1, y)
    elif y < dimenzija:
        print("Y")
        poti += possible_moves(x,y+1)
    
    return poti

total = possible_moves(0,0)
print(total)

