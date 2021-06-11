import sys
sys.stdin = open("input.txt", "r")

N, r, c = map(int, input().split())

x_size, y_size = 2**N, 2**N
x_start, y_start = 0, 0

answer = 0


def DFS(N):
    global answer, x_size, y_size, x_start, y_start
    if N == 1:
        for i in range(4):
            if y_start+(i//2) == r and x_start + (i % 2) == c:
                print(answer)

            answer += 1
    else:
        if r >= y_size//2 + y_start:
            y_start += y_size//2
            answer += 2**(2*N-1)

        if c >= x_size//2 + x_start:
            x_start += x_size//2
            answer += 2**(2*N-2)

        y_size = y_size//2
        x_size = x_size//2
        DFS(N-1)


DFS(N)
