import sys
sys.stdin = open("input.txt", "r")

dic = {}

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

for i in N_list:
    dic[i] = dic.get(i, 0) + 1

for i in M_list:
    try:
        print(dic[i], end=' ')
    except:
        print(0, end=' ')
