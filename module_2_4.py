numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if (i % j) == 0:
            not_primes.append(i)
            prime = False
            break
        if (i % j) != 0:
            primes.append(i)
            break
print(f"Primes: {primes}")
print(f"Not primes: {not_primes}")









