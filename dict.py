# details = {}
# print(type(details))

# details = {'name' : 'richu','age ': 22,'place':'CLCT'}
# print(details)


"""it allow to duplicATE value but if we put another same value output will be the last value will get"""
# details = {'name' : 'richu','age ': 22,'place':'CLCT','name':'shakir'}
# print(details)
"""only in keys"""
"""key is get numbers"""
# new = {1 : 'a',2 : 'b',3 :'c'}
# print(new)
# new = {1.2 : 'a',2.44000 : 'b',3.7765 :'c'}
# print(new)

"""tuple is allowed"""
# new = {1 : 'a',2 : 'b',3 :'c',(1,2,3): 'tupple'}
# print(new)

"""list not allowed"""
# new = {1 : 'a',2 : 'b',3 :'c',[1,2,3]: 'list'}
# print(new)

""""set not allowed"""
# new = {1 : 'a',2 : 'b',3 :'c',{1,2,3}: 'set'}
# print(new)

"""dict not allowed"""
# new = {1 : 'a',2 : 'b',3 :'c',{1:"shakir"}: 'dict'}
# print(new)


"""values"""
"""in values list,tuple,set,dict all alloweded"""
# new = {1 : [1,2,3,'ABC'],2 : (100,200,300,'abc'),3 :{10,20,'abc'},3:{'name':'shony'}}
# print(new)

# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# print(student1)

"""len"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# print(len(student1))

"""in this we is update or the add to the dictionary """
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# print(student1)
# student1['place'] = 'calicut'
# print(student1)
"""update"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# student1.update({'rollno':12})
# student1.update({'name':'yaseen'})
# print(student1)

"""append in only list case"""
# student1 = {'name' : 'shakir','age':20,'batch':['python']}
# print(student1['batch'].append('men'))
# print(student1)


"""dictionary element access"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# print(student1['age'])
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# print(student1.get('name','key doest\t exits'))
# print(student1.get('teacher','key doest\t exits'))


"""remove"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# del student1
# print(student1)

"""del"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# del student1['age']
# print(student1)

"""pop()"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# student1.pop('batch')
# print(student1)


# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# student1.pop()
# print(student1)


# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# new=student1.pop('batch')
# print(new)
# print(student1)

"""pop items it remove the last item"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# student1.popitem()
# print(student1)

"""clear it clear all the element"""
# student1 = {'name' : 'shakir','age':20,'batch':'python'}
# student1.clear()
# print(student1)

student1 = {'name' : 'shakir','age':20,'batch':'python'}
# for i in student1:
#     print(i)

# for key in student1.keys():
#     print(key)

# for value,key in student1.items():
#     print(value,key)

# for value in student1.values():
#     print(value)

# print(student1.keys())
# print(student1.values())
# print(student1.items())
