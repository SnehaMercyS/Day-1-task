Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # a) list down all the error types and check  all the error using a python program for all errors
>>> #ZeroDivisionError:
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> #FileNotFoundError:
>>> open("imaginary.txt")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    open("imaginary.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'
>>> #SyntaxError:
>>> if a<3
SyntaxError: invalid syntax
>>> #TypeError:
>>> def print_list_element(thelist, index):
	print(thelist[index])

	
>>> print_list_element(1,2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print_list_element(1,2)
  File "<pyshell#11>", line 2, in print_list_element
    print(thelist[index])
TypeError: 'int' object is not subscriptable
>>> #IndexError:
>>> def favorite_ice_cream():
	ice_creams =['chocolate','vanilla','strawberry']
	print(ice_creams[3])

	
>>> favorite_ice_cream()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    favorite_ice_cream()
  File "<pyshell#17>", line 3, in favorite_ice_cream
    print(ice_creams[3])
IndexError: list index out of range
>>> # b) design a simple calculator app with try and except for all use cases
>>> print("1.add")
1.add
>>> print("2.subtract")
2.subtract
>>> print("3.multiply")
3.multiply
>>> print("4.divide")
4.divide
>>> def addition(num1,num2):
	try:
		result=num1+num2
		print(result)
	except Exception as e:
		print(e)

		
>>> addition(2,3)
5
>>> def subtract(num1,num2):
	try:
		result=num1-num2
		print(result)
	except Exception as e:
		print(e)

		
>>> subtract(3,2)
1
>>> def divide(num1,num2):
	try:
		result=num1/num2
		print(result)
	except Exception as e:
		print(e)

	    
>>> divide(4,2)
2.0
>>> def multiply(num1,num2):
	try:
		result=num1*num2
		print(result)
	except Exception as e:
		print(e)

		
>>> multiply(4,5)
20
>>> # c) print one message if the try block raises a nameerror and another for other errors
>>> try:
	print(x)
except NameError:
	print("variable x is not defined")
except:
	print("something went wrong")

	
variable x is not defined
>>> try:
	a=3
	b='0'
	print(a+b)
except TypeError:
	print('operation is not supported')
except:	
        print("out of try except blocks")

        
operation is not supported
>>> try:
	a=3
	b='0'
	print(a+b)
except TypeError:
	print('operation is not supported')
except ZeroDivisionError:
	print('division by zero is not defined')
except:
	print('out of try except blocks')

	
operation is not supported
>>> # c) when try-except scenario is not required?
>>> # Answer: when there is no code block try-except scenario is not required
>>> # d) try getting an input inside the try catch block
>>> try:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a/b
except:
	print("cannot be defined")

	
enter A:7
enter B:0
cannot be defined
