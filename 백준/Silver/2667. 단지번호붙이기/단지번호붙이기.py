import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

n = int(input())

arr = []


for _ in range(n):
    a = list((map(int, input().strip())))
    arr.append(a)

visited = [[0] * n for _ in range(n)]

def bfs(graph, x, y):
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = 0
                    queue.append((next_x, next_y))
                    cnt += 1

    return cnt

ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans.append(bfs(arr, i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)
