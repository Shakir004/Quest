"""Create a string and print it."""

#  Write a Python program to take a string from the user and print the
    # first character using slicing.

# name = input("enter a string:")
# print(name[0:1])


# Write a program to display the last character of a string using
    # slicing.

# name = input("enter the string:")
# print(name[-1:])


#  Given a string, print the first 5 characters using slicing.

# name  = input("enter the string:")
# print(name[:5])

# Write a program to print all characters of a string except the first one.

# name = input("enter the string:")
# print(name[1::])


#   Write a program to print all characters of a string except the last one.

# name = input("enter the string:")
# print(name[:-1])

#  Given a string, print characters from index 2 to index 6.

# name = input("enter the string:")
# print(name[1:6])

# Write a program to print every character at even index positions using slicing.

# name = input("enter the string:")
# print(name[::2])

# Write a program to print every character at odd index positions using slicing.

# name = input("enter a string:")
# print(name[1::2])

#   Write a program to reverse a string using slicing.
# name = input("enter a string:")
# print(name[::-1])


# Given a string, print the middle character(s) using slicing (assume length can be even or odd).

# name = input("enter a string:")
# length = len(name)
# mid = length // 2

# if length % 2 != 0:
#     middle = name[mid : mid + 1]
# else:
#     middle = name[mid - 1 : mid + 1]
# print(f"The middle character(s): {middle}")


#  Write a program to check whether a string is a palindrome using  slicing.
# word = input("Enter a word:")
# if word == word[::-1]:
#     print("its a palintrome")
# else:
#     print("its not a palitrome")


#  Given a string, extract the first half and second half using slicing
    # and print them separately.


# word = input("enter a string:")
# middle = len(word) // 2 
# first_half = word[:middle]
# second_half = word[middle:]
# print(first_half)
# print(second_half)


# Write a program to remove the first and last two characters from a
    # string using slicing.

# str = input("enter a string:")
# print(str[2:-2])

# Given a string, print characters from index 1 to the second last
    # character.

# str = input("enter a str:")
# print(str[1:-1])


# Write a program to extract every third character from a string using
    # slicing.

# str = input("enter a string:")
# print(str[::3])


# 16. Given a string, reverse only the first half of the string using
    # slicing.

# str  = input('enter a string:')
# mid = len(str) // 2
# result = str[:mid][::-1] + str[mid:]
# print(result)



# str = input('enter astring:')
# mid = len(str) // 2
# result = str[:mid][::-1] + str[mid:]
# s = result
# print(s)

# 17. Write a program to extract the domain name from an email ID using # slicing

# str = input('enter a mail id:')
# domain = str.index("@")
# index_1 = str[domain + 1:]
# print(index_1)



# p= (input('enter a str:'))
# domain = p.index('@')
# in = p[domain + 1:]
# print(in)








