import sys
input = sys.stdin.readline

def val(n):
    stack = []
    for i in n:
        if i == '(':
            stack.append(')')
        elif i == '[':
            stack.append(']')
        elif i == ')' or i == ']':
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append('z')

    if not stack:
        print('yes')
    else:
        print('no')
        
while True:
    try:
        n = list(input())
        if n[0] == '.':
            break
        val(n)

    except:
        break
