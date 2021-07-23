
import sys
# sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
# read = lambda : sys.stdin.readline().strip()

n = int(input())
print(n)
cnt_one = 0
cnt_zero = 0
cnt_mone = 0
result = []
matrix = [list(map(int, input().split())) for _ in range(n)]

def same(x,y,n):
    #x,y서부터 n각형의 정사각형이 있는지 확인하는 것
    for i in range(x,x+n):
        for j in range(y,y+n):
            if matrix[x][y] != matrix[i][j]:
                return False
    return True
