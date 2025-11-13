
def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False

    return sum(i for i in range(limit) if is_prime[i]), sum(is_prime)

result = sieve_of_eratosthenes(2000000)
print(result)


