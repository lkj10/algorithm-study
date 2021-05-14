# set, slice로 구현
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
cnt = 0
for i in range(T):
    List = list(input())
    for i in set(List):  # List를 set으로 하여 중복값 제거
        # i값을 list 내의 갯수만큼 곱해서 리스트를 만들어준다.
        # 그리고 list 내부의 [인덱스값 : 인덱스값 + 카운트]로 슬라이싱하여 비교한다
        # 만약 두 값이 다르면 break
        if list(i*List.count(i)) != List[List.index(i): List.index(i) + List.count(i)]:
            break
    else:
        cnt += 1  # for문 다 돌아도 이상이 없으면 카운트 증가
print(cnt)

###########################################


# 딕셔너리로 구현
sys.stdin = open("input.txt", "r")

T = int(input())
cnt = 0
for i in range(T):
    List = list(input())
    dic = {}  # 딕셔너리 생성. for문 돌 때마다 초기화
    for i in range(len(List)):  # List의 길이만큼 for문 선언
        # List[i]가 딕셔너리 안에 있고 그 요소가 이전값의 i-1이 아닐 때
        if List[i] in dic and dic[List[i]] != i-1:
            break  # 포문 종료
        dic[List[i]] = i  # 딕셔너리 안에 i 입력
    else:  # for문 다 돌아도 이상이 없으면
        cnt += 1  # 카운트 증가
print(cnt)
