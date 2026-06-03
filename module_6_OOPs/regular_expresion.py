# import re

# data = "my phone number is 4783927483"

# pattern = r"\d\d"

# result = re.search(pattern, data)

# print(result)


# import re

# data = "my phone number is 4783927483"

# pattern = r"\d\d"                                                     #47

# result = re.search(pattern, data)

# print(result.group())


# import re

# data = "my phone number is 4783927483"

# pattern = r"\d\d"

# result = re.search(pattern, data)                                #['47', '83', '92', '74', '83']

# result2= re.findall(pattern,data)

# print(result.group())

# print(result2)

# import re

# data = "535663 my phone number is 4783927483"

# pattern = r"\d\d"

# result = re.search(pattern, data)

# result2= re.findall(pattern,data)                                                             #<re.Match object; span=(0, 2), match='53'>
# result3 =re.match(pattern,data)

# print(result)

# print(result3)

"""numbers are not allowed"""
# import re
# data = 'my 236 phone number is  👌873283283823893'

# pattern = r"\D"                                                      #['m', 'y', ' ', ' ', 'p', 'h', 'o', 'n', 'e', ' ', 'n', 'u', 'm', 'b', 'e', 'r', ' ', 'i', 's', ' ', ' ', '👌']
# result=re.findall(pattern,data)

# print(result)


"""alphanumeric only gives the output"""
# import re

# data = "my phone 😊 number is 4783927483"                               #['m', 'y', 'p', 'h', 'o', 'n', 'e', 'n', 'u', 'm', 'b', 'e', 'r', 'i', 's', '4', '7', '8', '3', '9', '2', '7', '4', '8', '3']

# pattern = r"\w"

# result = re.findall(pattern, data)

# print(result)


"""any character not alphaumeric"""
# import re

# data = "my phone number is 4783927483"                     #[' ', ' ', ' ', ' ']

# pattern = r"\W"

# result = re.findall(pattern, data)

# print(result)




"""any white space"""
# import re

# data = "my phone number is 4783927483"                         #[' ', ' ', ' ', ' ']

# pattern = r"\s"

# result = re.findall(pattern, data)

# print(result)



"""any character that is not white space"""
# import re

# data = "my phone number is 4783927483"                        #['m', 'y', 'p', 'h', 'o', 'n', 'e', 'n', 'u', 'm', 'b', 'e', 'r', 'i', 's', '4', '7', '8', '3', '9', '2', '7', '4', '8', '3']

# pattern = r"\S"

# result = re.findall(pattern, data)

# print(result)


"""any character exept newlline """
# import re

# data = "my phone number is 4783927483"

# pattern = r"."

# result = re.findall(pattern, data)

# print(result)

"""anu """
# import re

# data = "my phone number is 4783927483"                      #phone

# pattern = r"p...e"

# result = re.findall(pattern, data)

# print(result)



# import re

# data=  "call me on +91-74632-98347 or +91-88332-87654"

# pattern=r"\+91-\d\d\d\d\d-\d\d\d\d\d"
# pattern1=r"\+91-\d{5}-\d{5}"

# result=re.findall(pattern1,data)

# print(result)




# import re

# data = "My name is shakir,i'm from calicut.My phone number is 6282728191"

# result= re.search(r"shakir", data)

# print(result)

# print(result.group())                

# print(result.start())                #starting index from given input

# print(result.end())                  #ending index from given input

# print(result.span())                  #starting and ending index in given input in tupple format


# import re

# data = "My name is shakir,i'm from calicut.My phone number is 6282728191"

# result= re.findall(r"\d{5}", data)                                    #['6', '2', '8', '2', '7', '2', '8', '1', '9', '1']

# print(result)


# import re

# data = "My name is shakir,i'm from calicut.My phone number is 6282728191"                         #\w is not

# result= re.findall(r"\w{2}", data)

# print(result)

"""Quantiefiers"""

# import re

# data= "My name is shakir,i'm from calicut.My phone number is 6282728191"

# result= re.findall(r"\w{5,}", data)                                       #minimum 5 and more

# print(result)

# import re

# data= "My name is shakir,i'm from calicut.My phone number is 6282728191"                 #['My', 'name', 'is', 'shaki', 'from', 'calic', 'ut', 'My', 'phone', 'numbe', 'is', '62827', '28191']

# result= re.findall(r"\w{2,5}", data)                                      #minimum 2 and maximum 5

# print(result)

# import re

# data= "My name is shakir,i'm from calicut.My phone number is 6282528191"

# result= re.findall(r"\w+", data)                                          #one or more

# print(result)

# import re

# data= "My name is shakir,i'm from calicut.My phone number is 6282728191"

# result= re.findall(r"\w*", data)                #zero or more
                                     
# print(result)


# import re

# data= "My name is shakir,i'm from calicut.My phone number is 6282728191"

# result= re.findall(r"\w?", data)                                       #zero or one

# print(result)

