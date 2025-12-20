#the sum of the digits of 2^1000

#brute force

# def sum_digits(n):
#     sestevek = 0
#     while n != 0:
#         digit = n % 10
#         sestevek += digit
#         n = (n - digit) / 10
#         print(sestevek, digit, n)
    
#     return sestevek


# print(sum_digits(2**1000))

def sum_digits(n):
    sestevek = 0
    while n != 0:
        digit = n % 10
        sestevek += digit
        n = n // 10
    return sestevek

print(sum_digits(2**1000))
