from itertools import chain


def quad(arr):
    arr_len = len(arr)  # arr의 길이
    unit = arr_len // 2  # arr을 나누기위해 사용할 단위
    arr_sum = sum(chain(*arr))  # arr의 모든요소를 합한 값

    if arr_len == 1:  # 마지막까지 압축되지 않았을 경우
        return [arr[0][0]]
    elif arr_sum == arr_len * arr_len:  # 모든 요소가 1일 경우
        return [1]
    elif arr_sum == 0:  # 모든 요소가 0일 경우
        return [0]
    # arr을 4개의 배열로 나눔
    arr1, arr2, arr3, arr4 = (
        [ar[0:unit] for ar in arr[0:unit]],
        [ar[unit:] for ar in arr[0:unit]],
        [ar[0:unit] for ar in arr[unit:]],
        [ar[unit:] for ar in arr[unit:]],
    )
    test1=[ar[0:unit] for ar in arr[0:unit]]
    # 4개의 quad를 다시 나눔
    result = quad(arr1) + quad(arr2) + quad(arr3) + quad(arr4)
    return result
    #return list(chain(result))

def solution(arr):
    answer = quad(arr)
    return [answer.count(0), answer.count(1)]



print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))