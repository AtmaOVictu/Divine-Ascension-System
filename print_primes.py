primes = []
num = 2
while len(primes) < 10:
    for p in primes:
        if num % p == 0:
            break
    else:
        primes.append(num)
    num += 1

print(primes)
