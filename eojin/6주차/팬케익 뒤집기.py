import sys
sys.stdin = open("input.txt")


for tc in range(int(input())):
    answer=[]
    temp=list(map(int,input().split()))
    count,cake_list = temp[0],temp[1:]

    for i in range(count,0,-1):
        if i==cake_list[count-1]:
            continue
        for j in range(i-1):
            if cake_list[j]==i:
                if j != 0:
                    cake_list= list(reversed(cake_list[:j+1])) +cake_list[j+1:]
                    answer.append(j+1)
                cake_list = list(reversed(cake_list[:i])) + cake_list[i:]
                answer.append(i)
                break
    print(len(answer),end=" ")
    for i in answer:
        print(i,end=" ")
    print()


'''
4 2 5 3 1
5 2 4 3 1
1 3 4 2 5
4 3 1 2 5
2 1 3 4 5
'''