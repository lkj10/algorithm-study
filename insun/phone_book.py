# 전화번호 목록 - 첫번째 풀이 - 문제 잘못 이해해서 실패 뜸
def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j][0:1]):
                answer = False
                break
            else:
                answer = True
    return answer


# 두번째 풀이 - zip 함수 사용
def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True
