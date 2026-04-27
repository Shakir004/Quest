"""" **Python Lab – Lambda Function (Beginner to Intermediate)**

## *(Without Higher-Order Functions like map, filter, reduce)*

---

## **Section A: Basic Lambda Functions**

1. Write a lambda function to add two numbers."""

# ab = lambda a,b: a+b
# print(ab(12,23))                            output-35


"""2. Write a lambda function to subtract two numbers."""

# sub = lambda a,b: a-b
# print(sub(20,4))

"""3. Write a lambda function to multiply two numbers."""

# multi = lambda a,b: a*b
# print(multi(2,3))


"""4. Write a lambda function to divide two numbers."""

# divide = lambda a,b: a/b 
# print(divide(10,23))


"""5. Write a lambda function to find the square of a number."""

# square = lambda a: a**2
# print(square(2))

"""6. Write a lambda function to find the cube of a number."""

# cube = lambda a: a**3
# print(cube(3))

"""7. Write a lambda function to find the remainder of two numbers"""

# remainter = lambda a,b: 



"""8. Write a lambda function to calculate power (a^b)."""

# power = lambda a,b: a^b
# print(power(2,3))




"""## **Section B: Conditional Lambda Functions**

9. Write a lambda function to check whether a number is even or odd."""

# ori = lambda a,b:f"number is  {a} even"  if a%2==0 else  f"number is {b} odd"
# print(ori(2,3))

"""10. Write a lambda function to check whether a number is positive or negative."""

# posi=lambda a: f"positive {a}" if a>=0 else  "negative"
# print(posi(0))

"""11. Write a lambda function to check whether a number is positive, negative, or zero."""

# posi = lambda a: f"positive {a}" if a>0 else ( "negative" if a<0 else "zero" )
# print(posi(0))


"""12. Write a lambda function to find the greater of two numbers."""

# great = lambda a,b: f"greater is {a}" if a>b else f"lesser is {b}"
# print(great(21,12))


"""13. Write a lambda function to find the smaller of two numbers."""

# new = lambda a,b: a if a<b else b
# print(new(10,1))


"""14. Write a lambda function to find the maximum of three numbers."""

# new = lambda a,b,c:a if a>=b and a>=c else (b if b>=c else c)
# print(new(10,4,3))


"""15. Write a lambda function to find the minimum of three numbers."""

# new = lambda a,b,c: a if a<=b and a<=c else(b if b<=c else c)
# print(new(1,23,3))


## **Section C: Number-Based Problems**

"""16. Write a lambda function to check whether a number is divisible by 5."""

# new = lambda a:f"{a} number is divisible by 5" if a%5==0 else "not"
# print(new(9))

"""17. Write a lambda function to check whether a number is divisible by both 3 and 5."""

# new = lambda a:f"{a} number is divisible by 3 and 5" if a%3==0 and a%5==0 else "not"
# print(new(1))


"""18. Write a lambda function to find the last digit of a number."""

# new = lambda a: a % 10
# print(new(10))

"""19. Write a lambda function to remove the last digit of a number."""

# new = lambda a: a // 10
# print(new(19))


"""20. Write a lambda function to check whether a number is a multiple of 10."""

# new = lambda a: a %10 ==0
# print(new(12))

## **Section D: Formula-Based Problems**

"""21. Write a lambda function to calculate simple interest.

22. Write a lambda function to calculate the area of a rectangle.

23. Write a lambda function to calculate the area of a square.

24. Write a lambda function to calculate the perimeter of a rectangle.

25. Write a lambda function to calculate the area of a triangle.

26. Write a lambda function to convert Celsius to Fahrenheit.

27. Write a lambda function to convert Fahrenheit to Celsius.

---

## **Section E: String-Based Problems**

28. Write a lambda function to convert a string to uppercase.

29. Write a lambda function to convert a string to lowercase.

30. Write a lambda function to find the length of a string.

31. Write a lambda function to get the first character of a string.

32. Write a lambda function to get the last character of a string.

33. Write a lambda function to reverse a string.

34. Write a lambda function to check whether a string is a palindrome.

35. Write a lambda function to count vowels in a string.

36. Write a lambda function to check whether a string starts with 'A'.

---

## **Section F: Intermediate Level Problems**

37. Write a lambda function to calculate the average of three numbers.

38. Write a lambda function to swap two numbers.

39. Write a lambda function to return the absolute value of a number.

40. Write a lambda function to check whether a character is a vowel.

41. Write a lambda function to check whether a character is an alphabet.

42. Write a lambda function to check whether a character is a digit.

43. Write a lambda function to join two strings.

44. Write a lambda function to repeat a string n times.

45. Write a lambda function to calculate the discounted price.

---

## **Section G: Output-Based Questions**

# 46. What is the output of the following?"""


# x = lambda a: a + 5
# print(x(10))             output-15


"""47. What is the output of the following?"""


# x = lambda a, b: a if a > b else b
# print(x(7, 12))                                 b


"""48. What is the output of the following?

```
x = lambda s: s[::-1]
print(x("hello"))
```

49. What is the output of the following?

```
x = lambda n: "Even" if n % 2 == 0 else "Odd"
print(x(14))
```

50. What is the output of the following?

```
x = lambda a, b, c: a + b * c
print(x(2, 3, 4))
```

---

## **Section H: Debugging Questions**

51. Identify and correct the error:

```
add = lambda a, b: a + b
print(add(5))
```

52. Identify and correct the error:

```
square = lambda x: x * x
print(square())
```

53. Find the output:

```
x = lambda a: a if a > 10 else a * 2
print(x(6))
```

54. Find the output:

```
x = lambda s: s.upper()
print(x("hello"))
```

---

## **Section I: Short Lab Test**

55. Write a lambda function to add two numbers.

56. Write a lambda function to find the square of a number.

57. Write a lambda function to check whether a number is even or odd.

58. Write a lambda function to reverse a string.

59. Write a lambda function to check whether a string is a palindrome.

60. Write a lambda function to calculate simple interest.

61. Write a lambda function to convert Celsius to Fahrenheit.

62. Write a lambda function to find the last digit of a number.

63. Write a lambda function to count vowels in a string.

64. Write a lambda function to find the greater of two numbers.

"""