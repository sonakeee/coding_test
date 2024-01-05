import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

def check(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

ans = check(m)

def filltering(x):
    return x >= n

filtered_list = list(filter(filltering, ans))

for i in filtered_list:
    print(i)