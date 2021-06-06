from collections import Counter


# 로또의 최고 순위와 최저 순위 - 프로그래머스
# 제한사항으로 유추 가능한 내용
# 알아볼 수 없는 번호를 0으로 표기
# 0을 제외한 다른 숫자들은 중복되지 않음 -> set 사용 가능
# 정렬이 되어 있지 않다.
# lottos = 민우가 구매한 로또 번호를 담은 배열
# win_nums = 당첨 번호를 담은 배열

# answer = 당첨가능한 최고 순위와 최저 순위를 배열에 담아서 return

def solution(lottos, win_nums):
    ranking = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    # lottos에서 0의 개수 찾기
    find_zero = Counter(lottos)
    # win_nums에 0은 안담기기 때문에
    same_nums = len(list(set(win_nums) & set(lottos)))
    if same_nums <= 1:
        min_rank = 6
    else:
        min_rank = ranking[same_nums]

    if find_zero[0] + same_nums <= 0:
        max_rank = 6
    else:
        max_rank = ranking[find_zero[0] + same_nums]

    answer = list([max_rank, min_rank])
    return answer
