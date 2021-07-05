# 백준 - 회사에 있는 사람 - 7785

n = int(input())
punch = {}
people = []
for _ in range(n):
    k, p = input().split()
    punch[k] = p

for name, condition in punch.items():
    if condition == "enter":
        people.append(name)

print("\n".join(sorted(people, reverse=True)))
