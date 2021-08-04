import sys
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())
List = [0]
visit = [0]*(T+1)
for i in range(T):
    List.append(int(sys.stdin.readline()))

visit[1] = List[1]

if len(List) > 2:
    visit[2] = List[2] + List[1]

for i in range(3, len(List)):
    visit[i] = max(List[i] + List[i-1] + visit[i-3],List[i] + visit[i-2])

print(visit[-1])


