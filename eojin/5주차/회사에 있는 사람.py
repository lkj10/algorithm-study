
company_dict={}
for i in range(int(input())):
    name,status=input().split()
    company_dict[name]=status

result=[name for name,status in company_dict.items() if status=="enter"]
result.sort(reverse=True)
for i in result:
    print(i)
