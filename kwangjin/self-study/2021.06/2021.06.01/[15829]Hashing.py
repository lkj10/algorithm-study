import sys
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())

List = list(input())
SUM = 0 
for i in range(T):
    SUM += (ord(List[i])- 96) * 31**i

sys.stdout.write(str(SUM%1234567891))