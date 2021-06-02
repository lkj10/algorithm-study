def solution(numbers, hand):
    
    def locations(pos, num, l_hand, r_hand, hand):
        lD = abs(pos[l_hand][0] - pos[num][0]) + abs(pos[l_hand][1] - pos[num][1])
        rD = abs(pos[r_hand][0] - pos[num][0]) + abs(pos[r_hand][1] - pos[num][1])
        # 왼쪽, 오른쪽 손의 위치가 같은 경우
        if lD == rD:
            if hand == 'left':
                return 'L'
            else:
                return 'R'
        
        # 거리 계산
        if lD < rD:
            return 'L'
        else:
            return 'R'
            # 키패드
    pos = {
        1:[0,0], 2: [0,1], 3: [0,2],
        4:[1,0], 5: [1,1], 6: [1,2],
        7:[2,0], 8: [2,1], 9: [2,2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    l_hand, r_hand = '*', '#'
    result = ''
    
    for num in numbers:
        # 1,4,7 인 경우 -> 왼쪽
        if num % 3 == 1:
            result += 'L'
            l_hand = num
        # 0이 아니고 3,6,9 인 경우 -> 오른쪽
        elif num != 0 and num % 3 == 0:
            result += 'R'
            r_hand = num
        else:
            # 거리가 같은 경우 계산
            result += locations(pos, num, l_hand, r_hand, hand)
            # 마지막 요소가
            if result[-1] == 'L':
                l_hand = num
            else:
                r_hand = num
    return result

# 시간복잡도 O(N)
# 키패드에 좌표 부여 + 디셔너리 구성
# 나머지는 구현 
