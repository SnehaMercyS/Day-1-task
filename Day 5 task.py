Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #create a function getting two integer inputs from user.& print the following:
>>> # a) Addition of two number is + value
>>> def addition(a,b):
	add=a+b
	print("addition of two numbers:",a+b)

	
>>> addition(70,60)
addition of two numbers: 130
>>> # b) Subraction of two numbers is + value
>>> def subraction(a,b):
	sub=a-b
	print("subraction of two numbers:",a-b)

	
>>> subraction(70,60)
subraction of two numbers: 10
>>> # c) Division of two numbers is + value
>>> def division(a,b):
	div=a/b
	print("division of two numbers:",a/b)

	
>>> division(70,60)
division of two numbers: 1.1666666666666667
>>> # d) Multiplication of two numbers is + value
>>> def  multiplication(a,b):
	mul=a*b
	print("multipication of two numbers:",a*b)

	
>>> multiplication(70,60)
multipication of two numbers: 4200
>>> #create a function covid()& it should accept patient name,and body temperature,by default the body temperature should be 98 degree
>>> def covid(patient_name,body_temperature):
	print("covid statement:"+patient_name+","+body_temperature)

	
>>> covid('sneha','98 degree')
covid statement:sneha,98 degree
>>> #OR
>>> def covid(patient_name):
	print("Name of the patient:"+patient_name+"")

	
>>> covid('sneha')
Name of the patient:sneha
>>> def covid(body_temperature):
	print("Body temperature of the patient:"+body_temperature+"")

	
>>> covid('98 degree')
Body temperature of the patient:98 degree 
