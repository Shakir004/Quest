"""Create a set containing 5 numbers and print the set"""
# no = {1,2,3,4,5}
# print(no)
"""Create a set with mixed data types and print each element."""
# mixed = {1,'shakir','set',12,23}
# print(mixed)
"""Write a program to create a set from a list."""
# no = ['shakir',12,23,34,45]
# new = set(no)
# print(new)
"""Write a program to remove duplicate elements from a list using a set"""
# no = [1,2,4,56,67,56,5,6,1,2,34]
# new = set(no)
# print(new)
"""Create an empty set and add three elements to it."""
# new = set()
# new.update(['shakir'],['sha'],['ma'])
# print(new)
"""6. Write a program to check if an element exists in a set."""
# new = {'shakir', 12,23,'ma'}
# print('shakir' in new)
"""7. Create a set and print all elements using a for loop."""
# fruits = {'mango','apple','banana'}
# for items in fruits:
#     print(items)
"""8. Write a program to find the length of a set without using len()."""
# new = {12,'mango','apple','rose'}
# count = 0
# for i in new:
#     count+=1
# print(count)
"""9. Write a program to convert a tuple into a set."""
# tupples = (12,239,49934,98238,98488,344,55)
# new = set(tupples)
# print(new)
"""10. Write a program to convert a set into a list."""
# seti = {'mango','pinapple','straberry','apple'}
# new = list(seti)
# print(new)
"""Section 2 – Adding and Removing Elements"""
"""11. Create a set and add a new element using add()."""
# new = {'apple','mango','berry','jackfruits'}
# new.add('banana')
# print(new)
"""12. Write a program to add multiple elements to a set using update()."""
# new = {10,'jacj','mango','apple','savarjill'}
# new.update(['jack',2004])
# print(new)
"""13. Write a program to remove an element using remove()."""
# new = {12,23,34,45,45,56,56,56,76}
# new.remove(12)
# print(new)
"""14. Write a program to remove an element using discard()."""
# new = {12,23,34,45,45,56,56,56,76}
# new.discard(12)
# print(new)
"""15. Write a program to remove a random element using pop()."""
# new = {12,23,34,45,45,56,56,56,76}
# new.pop()
# print(new)
"""16. Write a program to clear all elements from a set."""
# new = {12,23,34,45,45,56,56,56,76}
# new.clear()
# print(new)
"""17. Write a program to copy a set into another set."""
# new = {12,23,34,45,45,56,56,56,76}
# n = new.copy()
# print(new)
# print(n)
"""18. Write a program to add elements from a list into a set."""
# new = [12,23,34,45,45,56,56,56,76]
# n = set(new)
# n.add(1)
# print(n)
"""19. Write a program to add elements from a tuple into a set."""
# new = (12,23,34,45,45,56,56,56,76)
# n = set(new)
# n.add(1)
# print(n)
"""20. Write a program to update a set with another set."""
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# set1.update(set2)
# print(set1)
"""Section 3 – Set Operations"""
"""21. Write a program to find the union of two sets."""
# set1 = {1,2,3,4,5}
# set2 ={3,4,5,6,7}
# print(set1.union(set2))
"""22. Write a program to find the intersection of two sets."""
# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# print(set1.intersection(set2))
"""23. Write a program to find the difference between two sets."""
# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# print(set1.difference(set2))
"""24. Write a program to find the symmetric difference between two sets."""
# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# new = (set1.symmetric_difference(set2))
# print(new)
"""25. Write a program to update a set using intersection_update()."""
# set1 ={1,2,3,8,4,5}
# set2 ={4,5,6,7,8,9}
# set2.intersection_update(set1)
# set2&=set1
# print(set2)
"""26. Write a program to update a set using difference_update()."""
# set1 ={1,2,3,8,4,5}
# set2 ={4,5,6,7,8,9}
# set2.difference_update(set1)
# print(set1)
"""27. Write a program to update a set using symmetric_difference_update()."""
# set1 ={1,2,3,8,4,5}
# set2 ={4,5,6,7,8,9}
# set1.symmetric_difference_update(set2)
# print(set1)
"""28. Write a program to check if one set is a subset of another set."""

"""29. Write a program to check if one set is a superset of another set."""
"""30. Write a program to check if two sets are disjoint."""


# list1 = [1,2,3,4,5,6,7,8]
# list2 = [2,4,5,6,7,8,9]
# common = []
# for items in list1:
#     if items in list2 and items not in common:
#         common.append(items)
# print(common)
