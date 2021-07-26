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


n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print (n)


# Our number to factor
number = 600851475143

# Our pretty cool trick limiting the number of things we need to test:
# (int(number**(0.5)) is the closest truncated integer to square root of
# whatever number we are testing)
for prime_factor in range(2, int(number**(0.5)) + 1):
    # test each number until we find one that has no remainder
    # (thus is a factor of number), the while loop will not run
    # if the iteration we are on does not factor into number
    while number % prime_factor == 0:
        # Since we have a factor, divide number by the factor and test the new
        # (smaller) number
        number /= prime_factor
        # if dividing number by prime_factor results in 1, then
        # number cannot be divided any further, and we have our answer
        # if dividing by prime_factor equals prime_factor, we need to prevent
        # while loop from running an extra time and yielding the wrong answer
        # (can you guess what will happen without this clause?)
        # if neither of these cases exist, we'll continue with our main loop if
        # number cannot be factored further, or continue in the while loop if it
        # can
        if number == 1 or number == prime_factor:
            print(prime_factor)
            break