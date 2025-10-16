Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
length=2
breadth=3
area=1/2*length*breadth
>>> print("area")
area
>>> area=1/2*2*3
>>> print("area")
area
>>> print(area)
3.0
>>> 
================================ RESTART: Shell ================================
>>> num=4
>>> if num%2==0
SyntaxError: expected ':'
>>> if num%2==0:
...     print"num is even"
...     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print("num is even")
num is even
>>> else
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> num=6
>>> if num%2==0:
...     print("num is even")
... else
SyntaxError: expected ':'
>>> else
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> num=6
>>> if num%2==0:
...     print("num is even")
... else:
...     print("num is odd")
... 
...     
num is even
