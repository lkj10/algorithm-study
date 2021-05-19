M, N = map(int, input().split())
cnt = 0
for i in range(1, M+1):
    if M % i == 0:
        cnt +=1
    if cnt == N:
        print(i)
        break
else:
    print(0)