# 1. Create a list of five integers and print all elements using a for loop.
# num = [10,20,30,40,50]

# for i in num:
#     print(i)

# 2 2. Write a program to find the length of a list without using len().
# num = [10,20,30,40,50]
# count =0
# for i in num:
#     count+=1
# print(count)

# 3 3. Create a list of numbers and print the maximum and minimum values.
# numbers = [10,20,30,40,50]
# maximum=numbers[0]
# minimum=numbers[0]
# for num in numbers:
#     if num > maximum:
#         maximum=num
#     if num<minimum:
#         minimum = num
# print(minimum)
# print(maximum)


# 4 4. Write a program to append a new element to a list entered by the user.
# num = []
# new = input("enter the element to the add:")
# num.append(new)
# print(num)


# 5 5. Insert an element at a specific position in a list.
# num = [20,30,40,50]
# num.insert(5,400)
# print(num)

# 6 6. Remove an element from a list using remove() and pop().
# num = [20,30,40,50,60]
# num.remove(20)
# print(num)
# num = [20,30,40,50]
# num.pop()
# print(num)


# 7 7. Write a program to check whether a given element exists in a list.
# num =[10,20,30,40,50]
# new = int(input("enter the element:"))
# if new in num:
#     print("is exists")
# else:
#     print("dont exixts")



# 8 8. Reverse a list without using reverse().
# num = [10,20,30,40,50]
# print(num[::-1])

# 9 9. Sort a list of numbers in ascending and descending order.
# num = [10,20,830,40,59]
# asending =sorted(num)
# print(asending)
# num = [2877,663,664,67]
# disending = sorted(num,reverse=True)
# print(disending)

# 10 10. Create a list of numbers and prin t only the even numbers.
# num = [10,20,30,44,56,66,77,53]
# for i in num:
#     if i % 2 == 0:
#         print(i)



# 11 11. Count how many times a specific element appears in a list.
# num = [12,2,3,4,5,6,7,88,55]
# new = int(input("enter the element:"))
# count = num.count(new)
# print(count)


# 12 12. Write a program to copy one list into another list.
# original = [12,23,45,56,77,34]
# copied_list=original.copy()
# print(original)
# print(copied_list)

# 13 13. Concatenate two lists using the + operator.
# num =[12,23,4,56,7,8]
# num1 =[12,34,56,75,77]
# comined = num + num1
# print(comined)

# 14 14. Repeat a list three times using the * operator.
# num = [12,3,45,6,7,4,4,3,6,4,7,5]
# reap = 3* num
# print(reap)
# 15 15. Demonstrate positive and negative indexing in a list
# num = [10,29,30,32,47]
# print(num[0])
# print(num[-1])



"""Section 2: Intermediate Level"""
# 1 16. Write a program to remove duplicates from a list.
# num = [10,23,3,4,2,43,4,2,4]
# uniq = list(set(num))
# print(uniq)

# 2 17. Find the second largest element in a list.
# num = [10,23,3,4,2,43,4,2,41]
# num.sort()
# print(num[-2])

# 3 18. Write a program to rotate a list to the left by one position.
# num = [10,23,3,4,2,43,4,2,4]
# rotate =  num[1:] + num[:1]
# print(rotate)

# 4 19. Write a program to rotate a list to the right by one position.
# num = [10,23,3,4,2,43,4,2,4]
# rotate =  num[-1:] + num[:-1]
# print(rotate)
# 5 20. Move a specific element (e.g., 50) to the first position of a list.
# num = [10,20,30,50,40]
# num.remove(50)
# num.insert(0,50)
# print(num)

# 6 21. Create a list of squares of numbers from 1–10 using list comprehension.
# square = [a*a for a in range (1,11)]
# print(square)

# 7 22. Create a list containing only odd numbers from 1–50 using list comprehension.
# odd = [x for x in range(1,51) if x % 2 ==0 ]
# print(odd)

# 8 23. Write a program to merge two lists and remove duplicates.
# num = [12,3,45,6,7,7,8,8]
# num1 = [12,3,452,33,2,4,6637]
# nw = num + num1 
# uni = list(set(nw))
# print(nw)
# print(uni)
# 9 24. Find the sum of all elements in a list without using sum().


# 10 25. Write a program to find common elements between two lists.
# 11 26. Write a program to split a list into two halves.
# 12 27. Find the index of a given element without using index().
# 13 28. Write a program to flatten a nested list.
# 14 29. Create a program to find the frequency of each element in a list.
# 15 30. Reverse each element of a list of strings.