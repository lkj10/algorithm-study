import sys
import heapq
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
hq=array.copy()
heapq.heapify(hq)
dict={}
idx=0
while hq:
    value = heapq.heappop(hq)
    if dict.get(value) !=None:
        continue
    dict[value]=idx
    idx+=1
for x in array:
    print(dict[x],end=" ")