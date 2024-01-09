import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

arr = input().split()
pq = []

for i in arr:
    heapq.heappush(pq, int(i))


for _ in range(m):
    x = heapq.heappop(pq)
    y = heapq.heappop(pq)
    heapq.heappush(pq, x+y)
    heapq.heappush(pq, x+y)

ans = 0
for v in pq:
    ans += int(v)

print(ans)