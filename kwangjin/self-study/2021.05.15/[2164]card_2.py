import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())
List = deque([i for i in range(1, T+1)])

while len(List) > 1:
    List.popleft()
    List.append(List.popleft())

print(List[0])
