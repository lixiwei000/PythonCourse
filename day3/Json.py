import pickle


li = ['Niko',12,52,'BJ']
dumped = pickle.dumps(li)
print(dumped)
print(type(dumped))
loadsed = pickle.loads(dumped)
print(loadsed)
# 将序列化结果存储到文件中
f = open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/day3/serialization.txt","wb+")
pickle.dump(li,f)

# Json

import json
d = {"name":"李熙伟","age":18,"gender":"Male"}
json_str = json.dumps(d)
print(json_str)
print(json.loads(json_str))