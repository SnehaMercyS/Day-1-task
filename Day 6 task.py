Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # a) write a program to loop through a list of numbers and add +2 to every value to elements in list
>>> list=[3,5,6,7,8,9]
>>> for i in list:
	print(i,i+2)

	
3 5
5 7
6 8
7 9
8 10
9 11
>>> # b) write a program to get the below program 54321 4321 321 21 1
>>> for i in range(5,0,-1):
	for j in range(i,0,-1):
		print(j,end="")
		print()

		
5
4
3
2
1
4
3
2
1
3
2
1
2
1
1
>>> # c) python program to print the fibonacci sequence
>>> x,y=0,1
>>> 
>>> while y<50:
	print(y)
	x,y = y,x+y

	
1
1
2
3
5
8
13
21
34
>>> # d) explian armstrong number and write a code with a function
>>> num= int(input("enter a number:"))
enter a number:153
>>> sum=0
>>> temp=num
>>> while temp >0:
	digit=temp%10
	sum+=digit**3
	temp//=10

	
>>> if num==sum:
	print(num,"it is an Armstrong number")
else:
	print(num,"it is not an Armstrong number")

	
153 it is an Armstrong number
>>> # e) write a program to print the multiplication table of 9
>>> num = int(input("display the multiplication table of :"))
display the multiplication table of : 9
>>> for i in range(1,11):
	print(num,'x',i,'=',num*i)

	
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
>>> # f) check if the program is positive or negative
>>> num=int(input("enter a number:"))
enter a number:13
>>> if num>0:
	print("{0} is a positive number".format(num))
else:
	print("{0} is a negative number".format(num))

	
13 is a positive number
>>> # g) write a program to convert the number of days to ages
>>> days=7665
>>> age=days/365
>>> print("age of the person is :")
age of the person is :
>>> print(age)
21.0
>>> # h) solve the trigonometry problem using math function write a program to solve using math function
>>> import math
>>> a=math.pi/6
>>> print("the value of the sin of pi/6:",end="")
the value of the sin of pi/6:
>>> print(math.sin(a))
0.49999999999999994
>>> print(math.cos(a))
0.8660254037844387
>>> print(math.tan(a))
0.5773502691896257
>>> # i) create a calculator only on a code level by using if condition (basic arithmetic calculation)
>>> print("calculator")
calculator
>>> print("1.Add")
1.Add
>>> print("2.subtract")
2.subtract
>>> print("3.multiply")
3.multiply
>>> print("4.divide")
4.divide
>>> choice=int(input("enter choice(1-4):"))
enter choice(1-4):3
>>> if choice==1:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a+b
	print("sum=",c)
elif choice==2:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a-b
	print("difference = ",c)
elif choice==3:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a*b
	print("product = ",c)
elif choice==4:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a/b
	print("Quotient = ",c)

	
enter A:10
enter B:20
product =  200
>>> 
