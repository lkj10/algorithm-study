def solution() -> int:
  n = int(input())

  for _ in range(n):
    word = input()
    for i in range(len(word) - 1):
      if word[i] != word[i + 1] and \
          word[i] in word[i + 1:]:
          n -= 1
          break
  print(n)

def solution() -> int:
  cnt = 0
  for _ in range(int(input())):
      word = input()
      cnt += list(word) == sorted(word, key=word.find)

  print(cnt)