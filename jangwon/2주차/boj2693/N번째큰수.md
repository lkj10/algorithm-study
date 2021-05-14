# N번째 큰 수

## boj 2693 [:link:](https://www.acmicpc.net/problem/2693)

```py
n = int(input())

for i in range(n):
  print(sorted(list(map(int, input().split())))[-3])
```