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

    def count(n: int) -> int: # type hints
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

print(euler17())  

# 