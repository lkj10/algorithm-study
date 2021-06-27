import sys
import collections
sys.stdin = open('input.txt', 'r')

T = int(input())
N, M, K = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [0 for _ in range(N) for _ in range(M)]

print(graph)
