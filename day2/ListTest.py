name_list = ["Niko","Tom","Helen","Zoo "]
name_list.append("Marry")
# print(name_list.count("Niko"))
# name_list.remove('Niko')
name_list.extend([1,2,3,4])
# name_list.sort()
name_list += [2,3,6,2,5,2,2,2]
# name_list.reverse()
print(name_list)

tmp_list = name_list.copy()
first_pos = 0
# for x in range(name_list.count(2)):
#     new_list = name_list[first_pos:]
#     next_pos = new_list.index(2) + 1
#     print("Find:" , first_pos + new_list.index(2))
#     first_pos += next_pos
print(name_list[::4])
