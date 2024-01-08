import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

state = m
for a in arr:
    check = 0

    for b in arr:
        if a == b:
            continue

        for c in arr:
            if c == b or a == c:
                continue

            check = a + b + c
            if check <= m:
                if state > int(m - check):
                    state = int(m - check)

print(m - state)
