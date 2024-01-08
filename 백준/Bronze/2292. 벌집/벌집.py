import sys
input = sys.stdin.readline

n = int(input())

nums, cnt = 1, 1
while n > nums:
    nums += 6 * cnt
    cnt += 1

print(cnt)