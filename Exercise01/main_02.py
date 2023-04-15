'''
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(_list)
_unique_set = set(_list)
_unique_list = list(_unique_set)
print(_unique_list)
print(len(_unique_list))