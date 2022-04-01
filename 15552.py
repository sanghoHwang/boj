import sys

s = int(input())
for i in range(s):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

