"""
# 문제 해결 

1) 아스키 코드를 바꿀 생각을 먼저 함 ord 함수 사용
2) 조이스틱 위 아래 변경 사항을 min을 통해 비교하여 코드를 줄임
3) count 함수를 통해 조이스틱을 통해 모두 바뀌었는지 확인  
   기존에 A가 있으면 바꿀 필요가 없다.
4) 커서 이동 체크 
5) 투 포인터를 통해 커서 비교 
6) 기존에 변경 단어에 A가 있는 쪽으로 이동하도록 -> 그래야 최소 값이 도출
7) 초기 name 인덱스 i를 i + left or i + right로 하여 인덱스 변경 사항을 합침

> 총 3개의 포인터를 사용하여 풀이한거 처럼 됐다.
"""

def solution(name):
    name = list(name)
    print(name)
    answer = 0
    i = 0
    
    while True:
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        # 조이스틱 조종 한 경우 name의 인덱스 값 조정 => 'A'
        name[i] = 'A'
        
        # 반복문 탈출 조건 , 조이스틱을 조종을 모두 완료했을 때 answer 값 반환
        if name.count('A') == len(name) : return answer
        
        left, right = 1, 1
        
        # 커서 이동, 우측 좌측 체크
        for l in range(1, len(name)):
            if name[i - l] == 'A': left += 1
            else: break
        
        for r in range(1, len(name)):
            if name[i + r] == 'A': right += 1
            else: break
                
        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right
            
    return answer

# 오른쪽 왼쪽 이동거리가 같은 경우 -> 우측으로 이동