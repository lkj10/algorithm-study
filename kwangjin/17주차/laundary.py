# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = map(int, input().split())
dic = {}
color = list(input().split())
for i in color:
	dic[i] = []
for i in range(M):
	min, clr = input().split()
	dic[clr].append(int(min))
	
res = 0
for key in dic:
	dic[key].sort(reverse = True)
	SUM = 0
	for i in range(len(dic[key])):
		if i % 2 == 0 : #2번째있는것만 뺌
			SUM += dic[key][i]
	res += SUM
print(res)