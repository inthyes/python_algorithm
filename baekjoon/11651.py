import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))

li.sort(key = lambda x: (x[1], x[0]))
for i in li:
    print(i[0], i[1])
