#!/usr/bin/python3

import sys
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def factorize_rsa(n):
    for i in range(2, n//2 + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: rsa_factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        n = int(file.readline().strip())

    factors = factorize_rsa(n)

    if factors:
         print(f"{n}={factors[0]}*{factors[1]}")
    else:
        print(f"Unable to find prime factors for {n}")

if __name__ == "__main__":
    main()
