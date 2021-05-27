# 테스트 케이스 7번 불통 
def solution(n, lost, reserve):

    # 예외 상황 처리
    for lost_s in lost:
        if lost_s in reserve:
            reserve.remove(lost_s)
            lost.remove(lost_s)
            
    result = n - len(lost)
    
    # 본 알고리즘
    for i in lost:
        if i + 1 in reserve:
            result += 1
            reserve.remove(i + 1)
        elif i - 1 in reserve:
            result += 1
            reserve.remove(i - 1)
    
    return result


# 복사를 따로 해주어야 테스트 케이스 통과

def solution(n, lost, reserve):
    reserve_c = [r for r in reserve if r not in lost]
    lost_c = [l for l in lost if l not in reserve]
    
    result = n - len(lost_c)
    
    for i in lost_c:
        if i + 1 in reserve_c:
            result += 1
            reserve_c.remove(i + 1)
        elif i - 1 in reserve_c:
            result += 1
            reserve_c.remove(i - 1)

    return result


# 배운 점

## 파이썬에서 필터링 하는 경우 filter함수가 있지만 리스트 컴프리헨션으로 하면 직관적으로 빠르게 할 수 있다.
## 람다식을 이용한 필터링 또한 있다.