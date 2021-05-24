# 약수 구하기
# 1. 값을 입력 받는다.
# 2. 약수를 구한다.
# 3. 약수를 리스트에 담는다.
# 4. k번째 수를 출력한다.(k에 대해서는 예외처리 해주기)
n, k = map(int, input().split())
number = []

for i in range(1, n + 1):
    if n % i == 0:
        number.append(i)
if k <= len(number):
    print(number[k - 1])
else:
    print(0)

# 참고할만한 풀이 방법
# 리스트를 만들지 않고 k를 감소시키고, k가 0이 되는 순간 출력함.
result = 0
for i in range(1, n + 1):
    if n % i == 0:
        k -= 1
        if k == 0:
            result = i
print(result)
