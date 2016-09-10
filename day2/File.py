


f = open("E:\IdeaProjects\PythonCourse\README.md","r+")
# for line in f.readlines():
#     print(line.strip())

# print(f.truncate(10))
f.seek(16)
print(f.tell())
# print(f.readline())