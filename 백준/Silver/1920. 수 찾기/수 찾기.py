import sys
input = sys.stdin.readline


n = int(input())
m = set(map(int, input().split()))

k = int(input())

my_list = list(map(int, input().split()))

for i in my_list:
    if i in m:
        print(1)
    else:
        print(0)