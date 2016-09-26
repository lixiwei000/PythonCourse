import re

result = re.match("[A-Za-z]\w+", "asdasa21ndou__i1niuo12n1u2i")
print(result.group())
result = re.search("[A-Za-z]\w+", "asdasa21ndou__i1niuo12n1u2i asdcassd21")
print(result.group())
result = re.findall("[A-Za-z]\w+", "asdasa21ndou__i1niuo12n1u2i")
print(result)
