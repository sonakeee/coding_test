import sys
input = sys.stdin.readline

n, m = map(int, input().split())

id_dict = {}
for _ in range(n):
    key, value = map(str, input().split())
    id_dict[key] = value

arr = []
for v in range(m):
    arr.append(input().strip())

for v in arr:
    print(id_dict[v])