numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    for j in range(2, i-1):
        is_prime = True
        if i % j == is_prime:
            primes.append(i)
        else:
            not_primes.append(i)


print(f"Primes: {primes}")
print(f"Not primes: {not_primes}")









