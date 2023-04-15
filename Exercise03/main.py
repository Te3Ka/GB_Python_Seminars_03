'''
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}] 
'''

_list_dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
                    {"VI": "S005"}, {"VII": "S005"},
                    {"V": "S009"}, {" VIII": "S007"}]
print(_list_dictionary)
_unique_list = []
for _v in _list_dictionary:
    for (_key, _value) in _v.items():
        _flag = True
        for j in range(len(_unique_list)):
            if _value == _unique_list[j]:
                _flag = False
        if _flag == True:
            _unique_list.append(_value)
print(_unique_list)