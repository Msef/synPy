import math

x = int(input())
count_divisors = 0

for i in range(1, int(math.sqrt(x))+1):
    if x % i == 0:
        count_divisors += 1
        if x // i != i:
            count_divisors += 1

print(count_divisors)
