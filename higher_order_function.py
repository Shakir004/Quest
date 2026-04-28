"""map()"""
# def square(nums : int)-> int:
#     return nums**2

# numbers=[1,3,45,67,6,7,32,5,98,45]

# result = list(map(square, numbers))
# print(result)

# result2 = list(map(lambda a: a**2, numbers))
# print(result2)


# elements = [1,2,3,5,67,8,42,23,90]
# new = list(map(lambda a: a%5==0,elements))
# print(new)



# elements = [1,2,3,5,67,8,42,23,90]                             
# new = list(filter(lambda a: a%5==0,elements))                      #[5, 90]
# print(new)


# string = ['shakir','eye','mango','m']
# wovels='aeiouAEIOU'
# new = list(filter(lambda a:  (char in wovels for char in a), string ))
# print(new)




# def has_wovels(word):
#     for ch in word:
#         if ch in 'aeiou':
#             return True
#     return False

# names= ['shakir','eye','mango','m']                              #['shakir','eye','mango']

# s = list(filter(has_wovels,names))
# print(s)



# sample = [0,[],{},5]
# print(any(sample))
# print(all(sample))



# names= ['shakir','eye','mango','m']  
# wovels = 'AEIOUaeiou'
# rslt=list(filter(lambda x: any(ch in wovels for ch in x),names))
# print(rslt)



# user = str(input("Enter Your Email:"))
# new = list(user)


 
# names= ['[shakir@gmail.com]','[eye@yahoo.com]','[mango@gmail.com]','[m]']                    #['shakir@gmail.com', 'mango@gmail.com']                                                                                                    #['shakir@gmail.com', 'mango@gmail.com']
# rslt=list(filter(lambda x: 'gmail' in x,names))
# print(rslt)


# emails = ['shakir@gmail.com','eye@yahoo.com','mango@gmail.com']
# r=list(filter(lambda x: any(x.endswith(d) for d in ['gmail.com']),emails))                     #['shakir@gmail.com', 'mango@gmail.com']
# print(r)


# lst=[12,23,44,556,78,9,9]
# new=list(filter(lambda a: a%3==0,lst))                                                      #[12, 78, 9, 9]
# new1=list(map(lambda a: a**3,new))                                                          #[1728, 474552, 729, 729]
# print(new)
# print(new1)



# lst=[12,23,44,556,78,9,9]
# rslt = list(map(lambda x: x**3,filter(lambda y: y%3 ==0,lst)))                                 #[1728, 474552, 729, 729]
# print(rslt)




# lst = ['shakir','jasil','niyas','naaaaaa']
