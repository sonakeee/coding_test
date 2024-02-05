import sys
from collections import defaultdict, deque
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

end = max(arr)
start = 1

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in arr:
        cnt += i // mid

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)