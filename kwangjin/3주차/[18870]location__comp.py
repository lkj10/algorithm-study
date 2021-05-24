import sys
import heapq
sys.stdin=open("input.txt", "r")

T = int(input())
List = list(map(int, input().split()))
List2 = set(List)
hq = list()
dic = {}
for i in List2:
    heapq.heappush(hq, i)

for i in range(len(List2)):
    temp = heapq.heappop(hq)
    dic[temp] = dic.get(temp, i)

for i in List:
    print(dic[i], end=' ')