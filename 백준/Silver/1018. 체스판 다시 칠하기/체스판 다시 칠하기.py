import sys
from collections import defaultdict, deque
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(input().strip()))

ans = []

for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if arr[x][y] != 'W':
                        cnt1 += 1
                    if arr[x][y] != 'B':
                        cnt2 += 1
                else:
                    if arr[x][y] != 'W':
                        cnt2 += 1
                    if arr[x][y] != 'B':
                        cnt1 += 1

        ans.append(cnt1)
        ans.append(cnt2)

print(min(ans))