from itertools import combinations
import math 
print(math.exp(1000))


numbers = [int(n) for n in input().split()]
k = int(input())
count = 0
for i in range(1, len(numbers)+1):
    for c in combinations(numbers, i):
        if sum(c) == k:
            count += 1
print(count)
try:
a = [1, 2, 3]
print (a[3]) except LookupError:
print ("Index out of bound error.")
