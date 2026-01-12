# #number of letters (not counting hyphens or spaces) in all the numbers (writen with letters) from 1 to 1000

# #every number is a compilatin of stotice, desetice and enice: a-hundread and b-ty c
# #hundreds are just ones but with 'hundread' at the end so plus 8 chars

# import errno


# relations_ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 0:0}

# relations_tens = {
#     0: 0,
#     1: 3,   # ten
#     2: 6,   # twenty
#     3: 6,   # thirty
#     4: 5,   # forty
#     5: 5,   # fifty
#     6: 5,   # sixty
#     7: 7,   # seventy
#     8: 6,   # eighty
#     9: 6    # ninety
# }

# # hundreds = ones + "hundred"
# relations_hundreds = {
#     k: v + 7 for k, v in relations_ones.items()
# }

# relacije = [
#     relations_ones,
#     relations_tens,
#     relations_hundreds
# ]

# #sestavim funkcijo ki za dano stevilo presteje stevilo znakov 
# def stevilo_znakov(n):
#     if n > 1000:
#         raise ValueError("n is too large")
#     if n == 1000:
#         return 8
    
#     stevilo = 0
#     for l in range(1,len(str(n)) + 1):
#         enota = n % 10
#         stevilo += relacije[-l][enota]
#         n = n//10
#         print(l, enota, relacije[l][enota])
    
#     return stevilo
        

# print(stevilo_znakov(111))


#chat resitev

def euler17():
    # letter counts (no spaces/hyphens)
    ones = {
        0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
        10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8
    }
    tens = {20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

    HUNDRED = 7      # "hundred"
    THOUSAND = 8     # "thousand"
    AND = 3          # "and"

    def count(n: int) -> int:
        if n < 20:
            return ones[n]
        if n < 100:
            return tens[n - n % 10] + ones[n % 10]
        if n < 1000:
            h, r = divmod(n, 100)
            base = ones[h] + HUNDRED
            return base + (AND + count(r) if r else 0)
        # n == 1000
        return ones[1] + THOUSAND

    return sum(count(i) for i in range(1, 1001))

print(euler17())  # 21124
