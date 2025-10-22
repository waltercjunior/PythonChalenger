# Write a function to find the prime factors that compose a number
# Takes a positive integer n as input
# Returns a list of n's prime factors
# The rationale for finding the prime numbers to determine the value should be:
# Takes 630 as input
# Returns the list [2, 3, 3, 5, 7] because 2 * 3 * 3 * 5 * 7 = 630
# Another example:
# Takes 13 as input
# Should return 13, because it is a prime number

# Usage example:
# Takes 60 as input
# Divides 60 / 2 = 30   list 
# Divides 30 / 2 = 15  list [2, 2]
# Divides 15 / 3 = 5   list [2, 2, 3]
# Divides 5 / 5 = 1    list [2, 2, 3, 5]

import sys


def find_prime_factors(n):
    factors = []
    divisor = 2

    if type(n) == int and n > 0:
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
        
        return factors
    else:
        
        return "Wrong value"


print(find_prime_factors(int(sys.argv[1])))