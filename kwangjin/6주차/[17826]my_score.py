import sys
sys.stdin = open("input.txt", "r")

List = list(map(int, input().split()))
my_score = List.index(int(input())) + 1
dic = {'A+': 5, 'A0': 15, 'B+': 30, 'B0': 35, 'C+': 45, 'C0': 48, 'F': 50}

for grade, rank in dic.items():
    if rank >= my_score:
        print(grade)
        break
