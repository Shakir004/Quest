""""""
# s = "niyas"
# print(s)
# s[::-1]


# place="calicut"
# place+="dist"
# print(place)

# place="calicut"
# place+=5
# print(place)


# place="calicut"
# place+="dist"
# print(place*place)



# place="calicut"
# # place+="dist"
# print(place*5)



# place="calicut"
# # place+="dist"
# print(place-"cut")



"""string methods"""
# company="Quest"
# print(dir(company))


"""upper case"""
# company = "quest calicut"
# print(company.upper())


""""lower case"""
# company = "QUEST CALICUT"
# print(company.lower())


# name = "SHAkir"
# print(name.lower())

"""title is used to convert first letter of all line will be capitile"""
# s = "my name is shakir"
# print(s.title())



"""capitilize is used to capitilize first word oof the line"""
# s = "my name is shakir"
# print(s.capitalize())


"""swapcase is used to get uppercase to lower and lowercase to upper"""
# name = "SHAkir"
# print(name.swapcase())


"""2.searching and finding"""
"""find() is used too find the intex of the line"""
# stack = "python Django"
# print(stack.find('o'))



"""rfind() is used to find in right to first index"""
# stack = "python Django"
# print(stack.rfind("a"))


"""index() is used to find the index position and got a more than 2 word from line starting index"""
# stack = "python Django"
# print(stack.index('o'))
    

"""rindex() is used to get right to left index"""
# stack = "python Django"
# print(stack.rindex('o'))



"""count() is used to how amany reapeated word have get"""
# stack = "bananaaa"
# print(stack.count('a'))


#  Write a Python program to take a string from the user and print the
#     first character using slicing.

# name=input("enter a string:")
# name[::]
# print(name)


"""validation and checking"""
# s = '123.34'
# print(s.isdecimal())



"""modification and replacement"""

"""replacement is used to replace old to new """
# s = "Python Django"
# print(s.replace('D','d'))

"""strip is used to remove the white space in starting and ending"""
# string = '     Python Django@@@@'
# print(string.strip('@'))

"""lstrip is used to remov the left side values are remove"""
# string = '@@@@@@@@@@@@@@@@@@@@@ Python Django @@@@@@@@@@@@@@@@@@'
# print(string.lstrip('@'))

"""rstrip is used to remove the right side values"""
# string = '@@@@@@@@@@@ Python Django @@@@@@@@@@@@'
# print(string.rstrip("@"))


"""removeprefix is used to remove string what you need in lef to right"""
# name = 'Mr.Sha'
# print(name.removeprefix('Mr.Sh'))


"""removesuffix is usde to remove to right to left"""

# name = 'Mr.Sha'
# print(name.removesuffix('Sha'))


"""formating and alignment"""

"""center method"""
# s = 'shakir'
# print(s.center(25,"*"))

"""ljust is used to justify to left side"""
# s = 'shakir'
# print(s.ljust(25,'😊'))

"""rjust is  used to justify to right side"""
# s = 'shakir'
# print(s.rjust(25,'😊'))


"""isasci"""
# s = 'python@123'
# print(s.isascii())


"""zfill is used to fill all the 0 with our string"""
# s = 'python'
# print(s.zfill(6))

"""format method"""
# name = 'shakir'
# age = 20
# print('my name is {} and i am {} year old'.format(name,age))

# name = 'shakir'
# age = 20
# print('my name is {1} and i am {0} year old'.format(age,name))

# name = 'shakir'
# age = 20
# print('my name is {} and i am {:05} year old'.format(name,age))

"""fstring is format string"""
# name = 'shakir'
# age = 20
# print(f"my name is {name} i am {age} year old")



# print("my name is shakir \ni am age year old")

# print("\"")



"""splitting and joining"""

# s = 'welcome to world of python'
# print(s.split())

# s = 'welcome1to1world1of1python'
# print(s.split('1'))

# print("Hello".split('l'))

# s = 'welcome_to_world_of_python'
# print(s.split('_',3))



"""rsplit is used to split right to left"""
# s = 'welcome to world of python'
# print(s.rsplit(" ",3))



"""join method is used to join the line of code"""
# s = 'welcome to world of python'
# splited = s.split()
# print(splited)
# joined_string = "".join(splited)
# print(joined_string)
# joined_string = "_".join(splited)
# print(joined_string)


"""partitioning is used to partitining a given word"""

# s = "job = python"
# print(s.partition('='))

# s = "job = python"
# print(s.partition('python'))

# s = "python"
# print(s.partition('python'))

# s = "python"
# print(s.partition('x'))

# s = 'my name is shakir'
# print(s.partition(" "))

"""rpartition"""
# s = 'my name is shakir'
# print(s.rpartition(" "))

"""encoding and decoding"""
"""Encoding it is used to convert to byte code thats why its output will be   b'shakir' """
# name = 'shakir'
# print(name.encode())

# name = 'shakir'
# print(name.encode(encoding="utf-8"))

# name = 'shakir'
# print(name.encode(encoding="utf-8",errors="strict"))



"""decoding is used to convert to byte code to string format"""
# name = "shakir"
# encoded_name = name.encode()
# print(encoded_name)
# decoded_name = encoded_name.decode()
# print(decoded_name)


"""miscelneus"""
# print("hello\tpython")

# print("hello\tpython".expandtabs())

# print("hello\tpython".expandtabs(10))

# print("hello\tpython".expandtabs(15))

"""expandtabs"""
# s = "hello\tpython"
# print(s.expandtabs(15))

"""equation= spaces=tabsize(current_position % tabsize)"""


"""translate and maketranslate"""
# print("banana".translate({97:"x"}))
# print("hello world".translate({111:'0'}))

# print(chr(111))

"""maketrance"""
# text = 'xxxxxxxxxxyyyyyyyyyyyyyyyzzzzzzzzzzzzzzz'
# table = text.maketrans('x','a')
# print(text.translate(table))


# text = 'xxxxxxxxxxyyyyyyyyyyyyyyyzzzzzzzzzzzzzzz'
# table = text.maketrans('x','a','a')
# print(text.translate(table))


"""split,join,replace,strip,prifix,suffix,isalpha,isdigit,index,find,count,upper,lower,title"""





