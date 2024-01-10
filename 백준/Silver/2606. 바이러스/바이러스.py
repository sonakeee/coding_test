import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = []

queue = deque()
queue.append(1)

while queue:
    cur = queue.popleft()
    for v in graph[cur]:
        if v not in visited:
            visited.append(v)
            queue.append(v)


if len(visited)-1 == -1:
    print(0)
else:
    print(len(visited)-1)