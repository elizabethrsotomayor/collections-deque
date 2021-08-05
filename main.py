# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

N = int(input())
for i in range(0, N):
    operation = input()
    lst = operation.split()

    if lst[0] == "append":
        d.append(int(lst[1]))
    elif lst[0] == "appendleft":
        d.appendleft(int(lst[1]))
    elif lst[0] == "pop":
        d.pop()
    elif lst[0] == "popleft":
        d.popleft()

for item in d:
    print(item, end=" ")
