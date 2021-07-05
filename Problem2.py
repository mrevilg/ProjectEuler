# Even Fibonacci Numbers (each # is prior two #'s added)
# 1, 2, 3, 5, 8, 13, 21, ...
# Q: Find the sum of the even-valued terms, no term exceeding 4M

x, y, z = 1, 1, 0
result = 0

while z < 4000000:
    z = (x+y)
    if z % 2 == 0:
        result = result + z

    x = y
    y = z

print(result)