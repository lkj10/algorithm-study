import sys
sys.stdin = open("input.txt", "r")


def f(L, x, y):
    init = List[x][y]
    if L == 1:
        result.append(str(init))
    else:
        for i in range(x, x + L):
            for j in range(y, y+L):
                if List[i][j] != init:
                    result.append('(')
                    f(L//2, x, y)
                    f(L//2, x, y + L//2)
                    f(L//2, x + L//2, y)
                    f(L//2, x + L//2, y + L//2)
                    result.append(')')
                    return
        else:
            result.append(str(init))


N = int(input())
List = list()
result = list()
for _ in range(N):
    List.append(list(map(int, input())))

f(N, 0, 0)

print(''.join(result))
