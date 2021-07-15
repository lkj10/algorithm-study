import collections
def solution(s: str, k: int) -> int:
    left = right = 0
    max_len = 0
    count = collections.Counter()
    dict={}
    for right in range(1, len(s) + 1):
        count[s[right - 1]] += 1

        # left부터 right까지 문자들 중 가장 많은 비중을 차지 하는 문자의 개수 ==> most
        most = count.most_common(1)[0][1]
        [("A",1)]
        #print(count.most_common(2))
        # 우리는 most 기준으로 나머지 문자들을 most문자로 바꿀 계획이다.
        remain = right - left - most  # 따라서 리메인(남은 문자)의 수가 바꿔야하는 수의 갯수라고 볼 수 있다.

        # 바꿔야 할 문자가 바꿀 수 있는 문자 수보다 많을 때 -> left를 증가시켜 윈도우크기를 줄인다.
        if remain > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(right - left, max_len)

    return max_len



#print(solution("ABAB",2))
print(solution("AABCBBA",2))