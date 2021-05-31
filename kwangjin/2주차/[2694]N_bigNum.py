import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for _ in range(T):
    List = list(map(int, input().split()))
    print(List)
    #List.sort(reverse=True)
    #print(List[2])
 