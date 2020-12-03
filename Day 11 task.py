Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # a) write a program using zip() function and list() function ,create a merged list of tuples from the two lists given ?
>>> list1 =[1,2,3,4]
>>> list2 =['a','b','c','d']
>>> def merge(list1, list2):
	merged_list = tuple(zip(list1, list2))
	return merged_list

>>> print(merge(list1, list2))
((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

>>> # b) first create a range 1 to 8 the using zip, merge the given list and the range together to create a new list of tuples ?
>>> list1 = [1,2,3,4]
>>> list2 = [5,6,7,8]
>>> list(zip(list1, list2))
[(1, 5), (2, 6), (3, 7), (4, 8)]
>>> tuple(zip(list1, list2))
((1, 5), (2, 6), (3, 7), (4, 8))

>>> # c) using sorted() function, sort the list in ascending order ?
>>> list = [2,3,6,5,1,4,7,8]
>>> x=sorted(list)
>>> print("sort the list in ascending order :",x)
sort the list in ascending order : [1, 2, 3, 4, 5, 6, 7, 8]

>>> # d) write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list ?
>>> list = [1,2,3,4,5,6,7,8,9]
>>> def even_numbers(num):
	if(num%2 == 0):
		return True
	else:
		return False

	
>>> evenNums = filter(even_numbers, list)
>>> print("even numbers:")
even numbers:
>>> for num in evenNums:
	print(num)

	
2
4
6
8
>>> 
