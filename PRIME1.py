from math import sqrt
from bisect import bisect_left

__author__ = 'Nikhil'
from sys import stdin

file = stdin


def read_line():
    return file.readline().strip()


def read_int():
    return int(read_line())


def read_int_list():
    return string_list_to_int_list(read_line().split())


def string_list_to_int_list(x):
    return [int(e) for e in x]


def mark_false_in_multiples(prime_list, multiple):
    iter_value = multiple
    multiple += multiple
    while multiple < len(prime_list):
        prime_list[multiple] = False
        multiple += iter_value
    return prime_list


def sieve(n):
    n += 1
    primes = [True] * n
    primes[1] = primes[0] = False
    sq = sqrt(n)
    for (i, prime_boolean) in enumerate(primes):
        if prime_boolean:
            mark_false_in_multiples(primes, i)
        if i > sq:
            break
    return list(map(lambda x: x[1], filter(lambda x: x[0], zip(primes, range(n)))))


def sieve_range(start, end, prime_list):
    sq_end = sqrt(end) + 1
    sv = [True] * (end - start + 1)
    if start == 0:
        sv[0] = sv[1] = False
    if start == 1:
        sv[0] = False

    for prime in prime_list:
        if sq_end < prime:
            break
        else:
            prime_multiple = start - start % prime
            while prime_multiple <= end:
                if prime_multiple >= start and prime_multiple is not prime:
                    sv[prime_multiple - start] = False
                prime_multiple += prime
    return list(map(lambda x: x[1] + start, filter(lambda x: x[0], zip(sv, range(len(sv))))))


cases = read_int()
primes_cache_list = sieve(int(sqrt(pow(10, 9))))
for case in range(cases):
    [start, end] = read_int_list()
    print("\n".join(map(str, sieve_range(start, end, primes_cache_list))))
    print()


