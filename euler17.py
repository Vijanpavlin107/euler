#number of letters (not counting hyphens or spaces) in all the numbers (writen with letters) from 1 to 1000

#every number is a compilatin of stotice, desetice and enice: a-hundread and b-ty c
#hundreds are just ones but with 'hundread' at the end so plus 8 chars

import errno


relations_ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 0:0}

relations_tens = {
    0: 0,
    1: 3,   # ten
    2: 6,   # twenty
    3: 6,   # thirty
    4: 5,   # forty
    5: 5,   # fifty
    6: 5,   # sixty
    7: 7,   # seventy
    8: 6,   # eighty
    9: 6    # ninety
}

# hundreds = ones + "hundred"
relations_hundreds = {
    k: v + 7 for k, v in relations_ones.items()
}

relacije = [
    relations_ones,
    relations_tens,
    relations_hundreds
]

#sestavim funkcijo ki za dano stevilo presteje stevilo znakov 
def stevilo_znakov(n):
    if n > 1000:
        raise ValueError("n is too large")
    if n == 1000:
        return 8
    
    stevilo = 0
    for l in range(1,len(str(n)) + 1):
        enota = n % 10
        stevilo += relacije[-l][enota]
        n = n//10
        print(l, enota, relacije[l][enota])
    
    return stevilo
        

print(stevilo_znakov(111))