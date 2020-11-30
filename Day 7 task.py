Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1) create a python module with list and import the module in anoother .py file and change the value in list
>>> list=[1,2,3,4,5,6]
>>> import mymodule
>>> mymodule.list.append(7)
>>> print(mymodule.list)
[1, 2, 3, 4, 5, 6, 7]
>>> #2) install pandas package (try to import the package in a python file
>>> import pandas as pd
>>> import numpy as np
>>> import sys
>>> sys._stdout_=sys.stdout
>>> fruit = np.array(['apple','orange','mango','pear'])
>>> series = pd.Series(fruits)
>>> print(series)
0   apple
1   orange
2   mango
3   pear
dtype: object
>>> #3) import a module that picks random number and write a program to fetch a random number from 1 to 100 on every run
>>> import random
>>> print("random integer is :",random.randint(1,100))
random integer is : 93
>>> #4) import sys package and find the python path
>>> import sys
>>> sys.path
['C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\pandas', 'C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib', 'C:\\Users\\ELCOT\\Downloads\\python-3.9.0-amd64.exe', 'C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']
>>> #5)try to install a package and uninstall a package using pip
>>> 
