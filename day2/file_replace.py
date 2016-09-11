import os, sys

print(sys.argv[1])
if len(sys.argv) <= 3:
    print("Usage : file_replace.py old_text new_text filename")

old_text, new_text = sys.argv[1], sys.argv[2]

file_name = sys.argv[3]

f = open(file_name, "r")
new_file = open("%s.bak" % file_name,"w+")
for line in f.readlines():
    new_file.write(line.replace(old_text, new_text))

f.close()
new_file.close( )