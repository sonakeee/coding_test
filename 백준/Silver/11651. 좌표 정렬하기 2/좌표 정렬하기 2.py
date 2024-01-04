import sys
input = sys.stdin.readline

num = int(input())


a = []
for i in range(num):
    a.append(list(map(int, input().split())))


sort_arr = sorted(a, key=lambda x: (x[1], x[0]))

for v in sort_arr:
    ans = ' '.join(map(str, v))
    print(ans)

