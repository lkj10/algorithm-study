# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
T = int(input())
for _ in range(T):
	N, K = map(int, input().split())
	List = []
	for _ in range(N):
		List.append(list(map(int, input().split())))

	MIN = 21e8
	for y in range(N-K+1):
		for x in range(N-K+1):
			SUM = 0
			for yy in range(y, K+y):
				for xx in range(x, K+x):
					SUM += List[yy][xx]
			MIN = min(SUM,MIN)

	print(MIN)