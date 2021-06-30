import sys
sys.stdin = open("input.txt", "r")


def f(Len, x, y):
    init = List[x][y]
    if Len == 1:
        result[init+1] += 1
        return
    else:
        for i in range(x, x+Len):
            for j in range(y, y+Len):
                if init != List[i][j]:
                    f(Len//3, x, y)
                    f(Len//3, x+Len//3, y)
                    f(Len//3, x+(Len//3)*2, y)
                    f(Len//3, x, y + Len//3)
                    f(Len//3, x + Len//3, y + Len//3)
                    f(Len//3, x + (Len//3) * 2, y + Len//3)
                    f(Len//3, x, y + (Len//3) * 2)
                    f(Len//3, x + Len//3, y + (Len//3) * 2)
                    f(Len//3, x + (Len//3) * 2, y + (Len//3) * 2)
                    return
        else:
            result[init+1] += 1


N = int(input())

List = list()
result = [0]*3

for _ in range(N):
    List.append(list(map(int, input().split())))
f(N, 0, 0)

for i in result:
    print(i)
