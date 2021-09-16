import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        Clothes, Type = input().split()
        dic[Type] = dic.get(Type, 0) + 1
    res = 1
    for key, val in dic.items():
        res *= (val + 1)
    print(res-1)  

