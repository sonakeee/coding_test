import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

n = int(input())

visited = []
num = 0


while len(visited) < n:
    num += 1
    c = 0

    check = [int(digit) for digit in str(num)]
    for i in check:
        if c == 3:
            break
        if i == 6:
            c += 1
        else:
            c = 0
    if c >= 3:
        visited.append(num)



print(visited[-1])

