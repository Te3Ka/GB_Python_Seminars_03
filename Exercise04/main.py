'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''

_list = [0, -1, 5, 2, 3, 4, 5, 3, 2, 5]
print(_list)
i = 1
_count = 0
for i in range(len(_list)):
    if _list[i - 1] < _list[i]:
        print(f"{_list[i - 1]} < {_list[i]}")
        _count += 1
print("Итого последующих элементов больше предыдущего: " + str(_count))