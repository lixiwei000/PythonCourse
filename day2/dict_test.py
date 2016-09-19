student_info = {
    'name':'Niko',
    'age':18,
    'salary':19999.0,
    'address':'BJ',
    'gender':'Male'
}
# Remove a item
# print(student_info.popitem())

# 遍历字典2种方式
# for (k,v) in student_info.items():
#     print(k,v)
# print('\n')
# for item in student_info:
#     print(item,student_info[item])

student_info.setdefault("size",0.0)
student_info['ex_list'] = ['武藤兰']
# 引用传递  &  深拷贝
print("=========== 浅Copy ============")
stu2 = student_info
stu_cp = student_info.copy()
stu2['name'] = 'Belic'
student_info['ex_list'].append('泷泽萝拉')
print(student_info)
print(stu2)
print(stu_cp)
print("=========== 深Copy ============")
import copy
stu_deep_cp = copy.deepcopy(student_info)
student_info['ex_list'].append('樱井莉亚')
print(stu_deep_cp)
print(student_info)
