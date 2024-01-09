import sys
input = sys.stdin.readline

n = int(input())

inArr = []
outArr = []

for _ in range(n):
    inArr.append(input().strip())

for _ in range(n):
    outArr.append(input().strip())

cnt = 0

for i in range(n):
    if inArr[cnt] == outArr[i]:
        cnt += 1
    else:
        inArr.remove(outArr[i])

print(n - cnt)
