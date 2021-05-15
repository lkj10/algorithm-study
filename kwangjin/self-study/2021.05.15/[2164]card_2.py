import sys
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())

# cnt = 0

# while 1:
#     cnt += 1
#     result = cnt + sum(map(int, str(cnt)))
#     if result == T:
#         print(cnt)
#         break
#     if cnt > 1000000:
#         print(0)
#         break

# 시간 320ms
##########################

k = max(T-9*len(str(T)), 0)

for i in range(k, T):
    result = i + sum(map(int, str(i)))
    if result == T:
        print(i)
        break
else:
    print(0)

# 시간 112ms
