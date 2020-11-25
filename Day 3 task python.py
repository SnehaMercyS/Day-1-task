Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #pyton program to map two list into a dictionary
>>> keys=['name','age','job']
>>> values=['sneha','21','python']
>>> myDict=dict(zip(keys,values))
>>> print(myDict)
{'name': 'sneha', 'age': '21', 'job': 'python'}
>>> 
>>> #python script to merge two python dictionaries
>>> dict1={'a': 10, 'b': 20}
>>> dict2={'c': 30, 'd': 40}
>>> dict=dict1.copy()
>>> dict.update(dict2)
>>> print(dict)
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> 
>>> #python program to remove a key from a dictionary
>>> dict.pop('a')
10
>>> print(dict)
{'b': 20, 'c': 30, 'd': 40}
>>> 
>>> #python program to find a length of a set
>>> set={'1','2','3','4','5','6'}
>>> print(len(set))
6
>>> 
>>> #python program to remove the intersection of a 2nd set from the 1st set
>>> set1={'1','2','3','4','5','6'}
>>> set2={'7','8','9','1','2','4'}
>>> print(set2.intersection(set1))
{'4', '2', '1'}
>>> 