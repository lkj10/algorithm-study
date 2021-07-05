import sys
sys.stdin = open("input.txt", "r")
dic = {}
M, N = map(int, input().split())

for i in range(M):
    word = input()
    dic[word] = i+1
    dic[str(i+1)] = word

for i in range(N):
    print(dic[input()])
