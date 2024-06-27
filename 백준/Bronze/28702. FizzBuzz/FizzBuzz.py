import sys

input = sys.stdin.readline


n = [input().strip() for _ in range(3)]


add = 3
for i, v in enumerate(n):
    if v.isdigit():
        add -= i - int(v)
        break


result = ''

if int(add) % 3 == 0 and int(add) % 5 == 0:
    result = 'FizzBuzz'
elif int(add) % 3 == 0:
    result = 'Fizz'
elif int(add) % 5 == 0:
    result = 'Buzz'
else:
    result = int(add)
print(result)