import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input().strip()))

ans = []

for v in arr:
    if not ans and v == 0:
        print(0)
    else:
        if v == 0:
            print(-1 * heapq.heappop(ans))
        else:
            heapq.heappush(ans, -v)
