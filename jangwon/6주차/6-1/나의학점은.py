import sys
sys.stdin = open("input.txt", "r")

def score(s):
  if s <= 5:
    print('A+')
  elif s <= 15:
    print('A0')
  elif s <= 30:
    print('B+')
  elif s <= 35:
    print('B0')
  elif s <= 45:
    print('C+')
  elif s <= 48:
    print('C0')
  elif s <= 50:
    print('F')

nums = list(map(int, input().split()))
result = 0
target = int(input())
for idx, num in enumerate(nums):
	if num == target:
		result = idx

score(result + 1)