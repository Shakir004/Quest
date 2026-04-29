"""34. Write a function `sum_all(*numbers)` that returns the sum of all given numbers.
"""
# def sum_all(*numbers):
#     return sum(numbers)

# print(sum_all(1,2,3,4))

"""35. Write a function `find_maximum(*numbers)`.
"""
# def sum_max(*numbers):
#     return max(numbers)

# print(sum_max(1,2,3,4,5))

"""36. Write a function `display_subjects(*subjects)` that prints all subject names.
"""
# def dis_subject(*subject):
#     for sub in subject:
#         print(sub)

# dis_subject("english","maths","zoology")



"""37. Write a function `average_marks(*marks)` that returns the average.
"""
# def average_marks(*marks):
#     if len(marks) ==0:
#         return 0
#     return sum(marks) / len(marks)

# print(average_marks(12,2,3,34,5,5,6,3,4,3,3))
    



"""38. Write a function `shopping_total(*prices)` that returns total amount.
"""
# def shopping_total(*price):
#     return sum(price)

# print(shopping_total(1000,299998,438876))


"""39. Write a function `student_profile(**details)` that prints all key-value pairs.
"""
# def student_profile(**details):
#     for key,value in details.items():
#         print(f"{key} : {value}")


# student_profile(name='shakir',age=25,course='python' )
          





"""40. Write a function `employee_record(**data)` to print employee details.
"""
# def employee(**data):
#     for key,values in data.items():
#         print(f"{key}:{values}")

# employee(name="shakir",salary=20000,age=20)


"""41. Write a function `product_details(**info)` for an ecommerce product.
"""
# def product_details(**info):
#     for key,values in info.items():
#         print(f"{key}:{values}")

# product_details(name="Laptop", price=50000, brand="Dell")



"""42. Write a function `user_settings(**settings)` to simulate app preferences.
"""
# def user_settings(**setting):
#     print("User Settings")
#     for key,values in setting.items():
#         print(f"{key}:{values}")

# user_settings(theme="dark", notifications=True, language="English")



"""43. Write a function `create_resume(**details)` to print formatted resume data.
"""
# def create_resume(**details):
#     for key,values in details.items():
#         print(f"{key}:{values}")

# create_resume(name="shakir",age=20,provesion='python full stck')



"""44. Write a function `report_card(name, *marks, **details)`.
"""
# def  report_card(name, *marks,**details):
#     print("------REPORT CARD------")

#     print(f"name: {name}")

#     if marks:
#         total = sum(marks)
#         average = total / len(marks)
#         print(f"mark: {marks}")
#         print(f"total : {total}")
#         print(f"average: {average}")
#     else:
#         print("no mark provided")


#     print("---details---")
#     for key,values in details.items():
#         print(f"{key}:{values}")

#     print("-------------") 

# report_card(
#     "Shakir",
#     85, 90, 78,
#     grade="A",
#     course="Python",
#     status="Pass"
# )






"""45. Write a function `invoice(customer_name, *items, **meta)`.
"""

# def invoice(customer_name,*items,**meta):
#     print(f"name:{customer_name}")

#     print("\nItems")
#     for item in items:
#         print(item)

#     for key,values in meta.items():
#         print(f"{key}:{values}")


# invoice(
#     "Shakir",
#     ("Laptop", 50000),
#     ("Mouse", 500),
#     ("Keyboard", 1500),
#     payment="UPI",
#     status="Paid"
# )

"""46. Write a function `validate_login(username, password)` that checks:
    - username should not be empty
    - password length should be at least 8"""
# def validate(username,password):
#     if not username:
#         print("Username should not be empty")
#         return False
    
#     if len(password) > 8:
#         print("password must be atleast 8 character")
#         return False
    
#     print("login data is valid")
#     return True
    
# validate("shakir", "12345678") 
# validate("", "12345678")        
# validate("shakir", "1234")       


    
    





"""47. Write a function `is_eligible_for_vote(age)`."""

"""48. Write a function `is_eligible_for_job(age, degree_completed)`."""

"""49. Write a function `calculate_overtime(hours_worked)`."""

"""50. Write a function `check_free_shipping(cart_total)`."""

"""51. Write a function `check_coupon_valid(amount)`:
    Apply coupon only if amount >= 1000."""

"""52. Write a function `calculate_mobile_bill(call_minutes, sms_count, data_used)`."""

"""53. Write a function `loan_eligibility(salary, cibil_score)`."""

"""54. Write a function `password_strength(password)`:
    Check length, digits, uppercase, lowercase."""

"""55. Write a function `username_validator(username)`:
    Rules:
    - minimum 5 characters
    - no spaces
    - must start with alphabet"""

"""56. Write a function `email_validator(email)` using simple conditions.
"""
"""57. Write a function `generate_username(first_name, last_name)`.
"""
"""58. Write a function `otp_generator(length)` using digits only.
"""
"""59. Write a function `masked_phone(number)` that returns masked phone like:
    9876543210 -> 987****210"""

"""60. Write a function `masked_email(email)`."""