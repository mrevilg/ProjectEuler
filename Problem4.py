# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

Max = 0
for i in range(100,1000):
	for j in range(100,1000):
		result = i * j
		length = len(str(result))
		re_result = str(result)[::-1] # 3 - digit numbers to obtain reversal of a string
		if re_result == str(result): # Description string and the strings are equal is inverted palindrome
			if result > Max: 
				Max = result # Assign the result to the large Max

print(Max)