# 문자 같은거 개수
# sum([x==y fox x,y in zip(word1,word2)])
# 문자 다른거 개수
# sum([x!=y fox x,y in zip(word1,word2)])
# A 리스트를 for 문 돌릴 때 한개씩 pop 해야 하는 경우
# for word2idx in range(len(words)-1, -1, -1) # 마지막 인덱스부터 검사해서 pop을해도 상관없다

def solution(begin, target, words):
    answer = 0
    queue = [begin]
    while True:
        tmpQ = []
        for word1 in queue:
            if word1 == target:
                return answer
            for word2idx in range(len(words)-1, -1, -1):
                word2 = words[word2idx]
                difference = sum([x != y for x, y in zip(word1, word2)])
                if difference == 1:
                    tmpQ.append(words.pop(word2idx))
        if not tmpQ:
            return 0
        queue = tmpQ
        answer += 1