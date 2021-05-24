# N번쨰 큰 수
T = int(input())

for _ in range(T):
    number = list(map(int, input().split()))
    number.sort(reverse=True)
    print(number[2])

for _ in range(T):
    number = list(map(int, input().split()))
    number.sort()
    print(number[-3])
