Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> # a) create a lambda function that multiplies argument x with argument y
>>> r=lambda x,y : x*y
>>> print(r(24,4))
96

>>> # b) write a python program to create fibonacci series to n using lambda
>>> from functools import reduce
>>> fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2),[0,100])
>>> print(fib(6))
[0, 100, 100, 200, 300, 500]

>>> # c) write a python program that multiply each number of given list with a given number
>>> nums =[2,3,4,5,6,7,8,9]
>>> n=2
>>> flitered_numbers=list(map(lambda number:number*n,nums))
>>> print(' '.join(map(str,flitered_numbers)))
4 6 8 10 12 14 16 18

>>> # d) write a python program to find numbers divisible by 9 from  list of  numbers
>>> nums=[9,27,18,63,45,79,100,47,109]
>>> result = list(filter(lambda x: (x % 9==0), nums))
>>> print("the number divisable by 9 is :",result)
the number divisable by 9 is : [9, 27, 18, 63, 45]

>>> # e) write a python to count the even numbers in a given list of integers
>>> nums = [2,4,5,6,7,8,9,10]
>>> odd = len(list(filter(lambda x: (x%2 != 0), nums)))
>>> even = len(list(filter(lambda x: (x%2 == 0), nums)))
>>> print("number of even numbers :", even)
number of even numbers : 5
>>> print("number of odd numbers :", odd)
number of odd numbers : 3
 
