#zacnem levo zgoraj
#20x20 grid
#lahko se premikam le desno in dol
#stevilo moznih poti

#na vsakem krizicu imam lahko 2 ali pa 1 moznost (ce sem ze na desnem ali spodnjem robu) ==> 
#moram simulirati?
#poskusim

moznosti = ['desno', 'dol']
poz = (0,0)
num = 0

while poz != (20, 20):
    