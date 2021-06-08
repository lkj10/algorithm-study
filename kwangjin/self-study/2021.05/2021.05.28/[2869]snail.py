import sys
import math
sys.stdin = open("input.txt", "r")

A, B, V = map(int, input().split())
day = (V - A)/(A - B)

print(math.ceil(day+1))