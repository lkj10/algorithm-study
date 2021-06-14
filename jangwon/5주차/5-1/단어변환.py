result = 100
check = []

# 단어 차이 판별 함수
def diffrent_Letter(word1, word2):
    diff = 0
    for idx, word in enumerate(word1):
        if word != word2[idx]: diff += 1
    
    return diff == 1

def dfs(begin, target, words, depth, check):
    if begin == target and result > depth:
        # 최소 값 바꿔 주기
        result = depth
        return
    else:
        for idx, start in enumerate(words):
            if diffrent_Letter(begin, start[idx]) and check[idx] == False:
                # 방문 처리
                check[idx] = True
                # 깊이 더 해주기
                depth += 1
                dfs(start, target, words, depth, check)
                # 백 트래킹이기 때문에 방문 해제 
                check[idx] = False
                # 다시 돌아갔기 때문에 depth 해제
                depth -= 1

def solution(begin, target, words):
    # 바꿀 단어가 하나도 없는 경우
    if begin not in words:
        return 0
    
    # 방문 배열 만들어 주기
    check = [False for i in range(len(words))]
    
    dfs(begin, target, words, depth, check)
    
    if result != 100:
        return result
    else:
        0