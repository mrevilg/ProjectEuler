# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

# Prime Factorization is finding which prime 
# numbers X together to make the original number

import math

def isPrime(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x))):
        if not x%i:
           return False
    return True

def largest_factor(number):
    for i in range (2, int(math.sqrt(number))):
        if number%i == 0:
            number = number/i
            if isPrime(number) is True:
                max_val = number
                break
                print (max_val)
        else:
            i += 1
    return max_val

largest_factor(600851475143)