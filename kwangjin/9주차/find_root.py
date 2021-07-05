import sys
sys.setrecursionlimit(10**6)


def solution(nodeinfo):

    answer = []

    preorder = []
    postorder = []

    def foo(List):
        if List == []:
            return
        else:
            root = max(List, key=lambda x: x[1])
            L_List = []
            R_List = []
            preorder.append(root)
            for i in List:
                if root[0] > i[0]:
                    L_List.append(i)
                elif root[0] < i[0]:
                    R_List.append(i)

            foo(L_List)
            foo(R_List)

            postorder.append(root)

        return

    foo(nodeinfo)

    answer.append(list(map(lambda x: nodeinfo.index(x)+1, preorder)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1, postorder)))

    return answer
