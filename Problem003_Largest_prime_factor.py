# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def variant_1():
    number = 600851475143
    sequence_of_numbers = list(range(2, 10000000))
    while number > 1:
        for prime_factor in sequence_of_numbers:
            if number % prime_factor == 0:
                break
        number = number / prime_factor
    return prime_factor


def variant_2():
    number = 600851475143
    prime_factor = 1
    while number > 1:
        prime_factor += 1
        if number % prime_factor == 0:
            number /= prime_factor
    return prime_factor


print("Variant 1. The largest prime factor is:", variant_1())
print("Variant 2. The largest prime factor is:", variant_2())
