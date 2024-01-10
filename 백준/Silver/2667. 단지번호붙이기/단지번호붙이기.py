import sys
n = int(sys.stdin.readline())

apart = []

for i in range(n):
    apart.append(list(map(int, sys.stdin.readline().rstrip())))

home = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

rows, cols = len(apart), len(apart[0])

cnt = 0

def dfs(row, col):
    global home_cnt
    if row < 0 or row >= rows or col < 0 or col >= cols or apart[row][col] != 1:
        return

    apart[row][col] = 0
    home_cnt += 1
    for i in range(4):
        dfs(row + dx[i], col + dy[i])
    return home_cnt

for row in range(rows):
    for col in range(cols):
        node = apart[row][col]
        if node != 1:
            continue

        home_cnt = 0
        home.append(dfs(row, col))
        cnt += 1

home.sort()
print(cnt)
for i in home:
    print(i)