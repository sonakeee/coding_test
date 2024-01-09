import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

stack = []
ans = [0] * len(arr)

arr.reverse()
for idx, val in enumerate(arr):
    if not stack:
        stack.append((idx, val))
    while stack and stack[-1][1] < val:
        check_idx, _ = stack.pop()
        ans[check_idx] = n - idx

    stack.append((idx, val))


ans.reverse()
answer = ' '.join(map(str, ans))
print(answer)