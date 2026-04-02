"""1. Create a tuple containing five different data types (int, float, string, list, boolean)."""
# tuplecntr = (10,10.4,'shakir',[12,23,34],True)
# print(tuplecntr)
"""2. Write a script to check the type of a tuple with a single element. Show the difference between (5) and (5,)."""
# tuplecntr = (10)
# print(type(tuplecntr))
# tupple = (5)
# tupple1= (5,)
# print(type(tupple))
# print(type(tupple1))

"""3. Access the last element of a tuple without knowing its length."""
# tupple = (10,20,30,40,50)
# print(tupple[-1])

"""4. Access the second to last element of a tuple using negative indexing."""
# tupple = (10,20,30,40,50)
# print(tupple[-4:])

"""5. Given nested_tuple = ("Python", [10, 20, 30], (5, 15, 25)), print the number 20."""
# nested_tuple = ("Python", [10, 20, 30], (5, 15, 25))
# print(nested_tuple[1][1])
"""6. Check if the element 'Sreeraj' exists in a tuple using a membership operator."""
# tupple = ('shakir','sreeraj','sree','in')
# print('sreeraj'  in tupple  )
"""
7. Find the memory size of a list vs. a tuple with the same elements using the sys module."""
# my_list = [10,20,30,40,50]
# my_tupple = (10,20,30,40,50)


"""8. Unpack a tuple of 3 elements into three variables: x, y, and z."""
# tupple =(10,20,30,40)
# x,y, *z=tupple
# print(x)
# print(y)
# print(z)
"""9. Demonstrate what happens if you try to unpack a tuple of 4 elements into 3 variables."""
# tupple = (10,20,30,40)
# x,y,*z=tupple
# print(x)
# print(y)
# print(z)
"""10. Use the 'extended iterable unpacking' (using *) to grab the first element and the rest into a 
list."""
# tupple = (10,20,30,40,50)
# x,*y=tupple
# print(x,y)
# 11. Write code that attempts to change the first element of a tuple and handle the resulting 
# TypeError gracefully.

# 12. Given a tuple: t = (1, 2, [3, 4]). Change the value 3 to 30. Explain why this works despite 
# tuples being immutable.
# t = (1,2,[3,4])
# t[2][0] = 30
# print(t)
# 13. Create two tuples, concatenate them, and assign them to a new variable.
# new = (10,20,30,40,50,60)
# n= (92,30,40,587,23,45)
# tple = new + n
# print(tple)

# 14. Use the repetition operator (*) to create a tuple of ten zeros.
# zero = (0,) * 10
# print(zero)
# 15. Swap two variables a and b using tuple unpacking logic in a single line.
# a = (10,)
# b = (5,)
# a,b = b,a
# print(a,b)


# 16. Write a program to "add" an item to a tuple by converting it to a list first.
# tupple = (10,20,30,40,50,60)
# new = list(tupple)
# print(new.append(300))
# n = tuple(new)
# print(n)
# print(new)
# 17. Write a program to "remove" an item from a tuple.
# tupple = (10,20,30,40,50)
# new = list(tupple)
# new.remove(20)
# tupple = tuple(new)
# print(tupple)
# print(new)
# 18. Delete an entire tuple variable from memory and verify its absence using a try-except 
# block.
# persons = ('shakir','niyas','jasil','yaseen')
# del persons
# print(persons)
# 19. Sort a tuple of integers and return the result as a new tuple
# tupple = (10,333,20,30,40,50)
# new = list(tupple)
# new.sort()
# tupple = tuple(new)
# v = sorted(tupple)
# print(v)
"""20. Reverse a tuple using the slicing method [::-1].

--- PART 3: METHODS & AGGREGATION ---
21. Find the index of the first occurrence of the number 10 in a tuple.
22. Count how many times the string "Python" appears in a tuple of job roles.
23. Find the maximum and minimum values in a tuple of stock prices.
24. Calculate the sum of all numeric elements in a tuple.
25. Given a tuple of tuples: ((1, 2), (3, 4), (5, 6)), calculate the sum of the second element of 
each internal tuple.
26. Use the index() method to find the position of 'Apple' starting from index 3 in a large fruit 
tuple.
27. Write a function that takes a tuple and returns a new tuple containing only the even 
numbers.
28. Convert a list of tuples into a single flat list.
29. Create a tuple from a user-input string where each character is an element.
30. Check if all elements in a tuple are truthy using the all() function."""
