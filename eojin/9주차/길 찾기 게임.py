import sys

sys.setrecursionlimit(10 ** 6)


def tree_order(arrY, pre_answer,post_answer):
    node = arrY[0]

    arrY1 = []
    arrY2 = []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    pre_answer.append(node[2])
    if len(arrY1) > 0:
        tree_order(arrY1,  pre_answer,post_answer)
    if len(arrY2) > 0:
        tree_order(arrY2,  pre_answer,post_answer)
    post_answer.append(node[2])
    return

def solution(nodeinfo):
    pre_answer = []
    post_answer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    arrY = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    tree_order(arrY,pre_answer,post_answer)
    return [pre_answer, post_answer]


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))