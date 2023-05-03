import random
import math


def is_prime(number: int):
    primes_less_then_half = [i for i in range(2, number // 2 + 1)]
    size_of_array = [number // i // 2 + 1 for i in range(2, number // 2 + 1)]
    for i in primes_less_then_half:
        if number % i == 0:
            return False
        else:
            for k in range(2, size_of_array[primes_less_then_half.index(i)]):
                if i * k in primes_less_then_half:
                    pos = primes_less_then_half.index(i*k)
                    del primes_less_then_half[pos]
                    del size_of_array[pos]
                else:
                    continue
    return True


def create_prime():
    out = 10
    while not is_prime(out):
        out = random.randint(1000, 10000)
    return out


G = random.randint(10, 50)
P = create_prime()

