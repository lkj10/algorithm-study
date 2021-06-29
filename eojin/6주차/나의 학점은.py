score_list=list(map(int,input().split()))
score=int(input())
score_list.sort(reverse=True)
for i in range(50):
    if score_list[i]==score:
        result=i
        break
answer=""
if result<=4:
    answer="A+"
elif result<=14:
    answer="A0"
elif result<=29:
    answer="B+"
elif result<=34:
    answer="B0"
elif result<=44:
    answer="C+"
elif result<=47:
    answer="C0"
else:
    answer="F"

print(answer)
