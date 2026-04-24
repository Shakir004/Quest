# def add(a,b):
#     return a + b

# result = add(2,3)
# print(result)







# def add(a,b):
#     return a + b

# print(add(25,25))

# def add(a,b,c):
#     return a + b + c

# print(add(25,25,23))

"""arbitary arguments"""
"""define by *args"""
# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total

# print(add(26,26,24,26,29,762))


"""**keywords arguments"""
"""arbitary keyword arguments is allow a function to accept any number of keyword arguments,even if you don't know the parameter name in advance"""
"""** is tells python to accept any number of keywords arguments"""
"""kwargs is store all keywords arguments in a dictionary"""
# def details(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
    
# # details(name = 'sha',age=23)
# details(name = 'sha',age=23,place = 'clt',phone = 299832888828)


# def numbers(*args):
#     for i in args:
#         if i%2==0:
#             print(i)

# print(numbers(24,4,2,43,52,52,4,32,11,11,1,5,6,79,9))

"ways to pass values to function"
"""pass by value"""
"""*the function get a copy of the data. if the function changes that copy,the orginal variable outside the function stays the same.
*analogy:you give a friend a photocopy of a map they can draw on their copy,but your original map remains clean
*common in:c,java(primitive),and python (for number/string)"""

# x = 25
# def modify():
#     global x
#     print(x)
#     x = 200

# modify()
# print(x)

# a=[1,2,3]
# b=a
# b.append(4)
# print(id(a))
# print(id(b))

# def fact(n):
#     if  n == 1:
#         return 1
#     return n * fact(n -1)

# print(fact(5))


# def revers(n):
#     if len(n) == 0:
#         return n
#     return revers(n[ 1: ]) + n[0]

# print(revers('sha'))


"""lamda function"""
# f=lambda x:x+5
# print(f(10))


# def square(a):
#     return a**2
# print(square(5))

# sq = lambda a: a**2
# print(sq(6))

# total = lambda a,b,c: a+b+c
# print(total(12,11,23))

# tot = lambda a : a**2 if a % 2 ==0 else a**3
# print(tot(4))

# a = input("enter a string:")
# a1 = lambda a: len(a)
# print(a1(a))

# a = input("enter a number")
# b= input("enter the second number")


# a1 = lambda a,b: f"greater is {a}" if a>b else f"lesser is {b}"            lesser is 12
# print(a1(1,12))

# to = lambda x,y,z:x if x>y and x>z else(y if y>x and y>z else z)
# print(to(12,34,111))

# total = lambda a,b: a if a>b  else(b if b>a else "equal")
# print(total(11,11))

# total = lambda a,b: "multiple of 5" if a%5==0 and a%3==0 else
