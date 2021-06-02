import sys
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())
List = [0] * 10001
for _ in range(T):
    List[int(sys.stdin.readline())] += 1

for i in range(len(List)):
    if List[i] > 0:
        for j in range(List[i]):
            sys.stdout.write(f"{str(i)}\n")