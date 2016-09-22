'''
员工信息模糊查询
1.将员工信息加载到内存
2.输入需要查询的信息
3.匹配到相关信息  将查询部分高亮后插入到结果集
'''



infos = open('/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/day3/members.info')
search_text = input("Please Input The Text You Wanna Search:")
result = []
for member in infos.readlines():
    # print(member.strip())
    if member.strip().find(search_text) > -1:
        result.append(member.strip().replace(search_text,'\033[32;1m ' + search_text + '\033[0m'))

print("The Result Are :\n")
for res in result:
    print(res)
