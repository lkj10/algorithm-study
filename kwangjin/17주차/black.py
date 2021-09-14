# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())
List = list(map(int, input().split()))
temp = 1
cnt = 0
while(temp < N):
	temp += K-1
	cnt+=1
	
print(cnt)