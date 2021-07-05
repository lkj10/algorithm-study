import sys
sys.stdin = open("input.txt", "r")


NUM_0 = 0
NUM_1 = 0
result = [0]*41

#memoriale로 풀어야함.

def fibonacci(N):
    global NUM_0
    global NUM_1
    if result[N] != 0:
        NUM_0 += result[N][0]
        NUM_1 += result[N][1]
    else:
        if N == 0:
            NUM_0 += 1
        elif N == 1:
            NUM_1 += 1
        else:
            fibonacci(N-1)
            fibonacci(N-2)


for i in range(41):
    fibonacci(i)
    result[i] = (NUM_0, NUM_1)
    NUM_0, NUM_1 = 0, 0

T = int(input())

for _ in range(T):
    N = int(input())
    print(result[N][0], result[N][1])
