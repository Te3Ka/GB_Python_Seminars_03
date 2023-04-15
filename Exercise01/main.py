'''
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(_list)
_unique_list = []
for i in range(len(_list)):
    _flag = True
    for j in range(len(_unique_list)):
        if _list[i] == _unique_list[j]:
            _flag = False
    if _flag == True:
        _unique_list.append(_list[i])
print(_unique_list)
print(len(_unique_list))