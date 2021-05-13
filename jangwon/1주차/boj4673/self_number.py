# 풀이 1
def solution() -> int:
  numbers = list(range(1, 10001))
  remove_list = []  
  for num in numbers :
      for n in str(num):
          num += int(n)  
      if num <= 10000:  
          remove_list.append(num) 

  for remove_num in set(remove_list) :  # set 집합 함수를 통해 중복 처리 -> 중복 처리 안 할시 같은 값에 대해 에러 발생 
      numbers.remove(remove_num)

  for num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
      print(num)

# 풀이 2
def solution() -> int:
  numbers = set(range(1, 10000))
  remove_set = set() # 생성자가 있는 숫자 set
  for num in numbers:
    for n in str(num):
      num += int(n)
    remove_set.add(num) # set이기 때문에 중복 값 해결이 된다.

  remove_target = numbers - remove_set

  for num in sorted(remove_target):
    print(num)