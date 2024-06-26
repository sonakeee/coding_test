import sys
import math

input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

pSet = n // p
pValue = pSet * p
pAdd = n - pValue

arr = []



size = [num for num in size if num != 0]

for i in size:
    ans = math.ceil(i / t)
    arr.append(ans)

sumData = sum(arr)



print(sumData)
print(pSet, pAdd)
