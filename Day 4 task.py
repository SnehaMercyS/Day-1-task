Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #write a program to create a list of n integer values and do the following
>>> L1=['2','3','4','5','6']
>>> # a) add an item in to the list (using function)
>>> L1.append('7')
>>> print(L1)
['2', '3', '4', '5', '6', '7']
>>> # b) delete(using function)
>>> L1.remove('3')
>>> print(L1)
['2', '4', '5', '6', '7']
>>> # c) store the largest number frrpm the list to a variable
>>> print(max(L1))
7
>>> # d) store the smallest number from the list to a variable
>>> print(min(L1))
2
>>> #create a tuple and point the reverse of the created tuple
>>> tuple = ('1','2','3','home','3.14')
>>> reversedtuples = tuple[::-1]
>>> print(reversedtuples)
('3.14', 'home', '3', '2', '1')
>>> #create a tuple and convert tuple into list
>>> tuple = ('45','56','67','3.45','home')
>>> list = list(tuple)
>>> print(type(list))
<class 'list'>
>>> print(list)
['45', '56', '67', '3.45', 'home']
>>> 
