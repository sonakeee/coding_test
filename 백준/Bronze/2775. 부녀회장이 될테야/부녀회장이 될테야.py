import sys

input = sys.stdin.readline


t = int(input())

for i in range(t):

    c = int(input())
    h = int(input())
    people = [i for i in range(1, h+1)]


    for x in range(c):
        new = []
        for y in range(h):
            new.append(sum(people[:y+1]))

        people = new.copy()
    print(people[-1])


