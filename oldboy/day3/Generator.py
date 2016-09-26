# def foo():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# print(type(foo()))
# for item in foo():
#     print(item)


def my_xreadlines(file_path):
    seek = 0
    f = open(file_path,"r")
    while True:
        # f.seek(seek)
        data = f.readline()
        # seek = f.tell()
        if data:
            yield data
            print("Hey")
        else:
            return
import time
for line in my_xreadlines("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day2/hadoop.txt"):
    print(line.strip())
    time.sleep(1)