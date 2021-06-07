def solution(lottos, win_nums):
    result = []
    # 맞은 개수 
    correct = 0
    # 제로의 개수
    zero = 0
        
    # 로또 몇개 맞았는지 판별 함수 -> 동일 코드 모듈화 
    def lotto_validation(correct):

        if correct == 6:
            result.append(1)
        elif correct == 5:
            result.append(2)
        elif correct == 4:
            result.append(3)
        elif correct == 3:
            result.append(4)
        elif correct == 2:
            result.append(5)
        else:
            result.append(6)
    
    # 기존에 맟춘 개수 구하기
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
            
    # 잠정적으로 맞춘 개수
    for lotto in lottos:
        if lotto == 0:
            zero += 1
    
    # 등수 구하기 correct + zero의 개수가 최대의 개수
    # 최소의 개수 correct의 개수 
    max_correct = correct + zero
    
    lotto_validation(max_correct)
    lotto_validation(correct)
        
    return result

# for문에 in문이 겹쳐 있으므로 시간 복잡도 O(N^2)
    
    
    