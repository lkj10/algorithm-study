# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
start, end = map(int, input().split())

for i in range(start, end+1):
	Int = i;
	SUM = 0
	for j in str(Int):
		SUM += int(j)*int(j)*int(j)
	if i == SUM:
		print(i, end=' ')