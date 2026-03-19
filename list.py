# sample_list = []
# print(type(sample_list))

# sample_list = list()
# print(type(sample_list))

# sample_list = [1,2,3,'Quest',10,25,[7,8,9], True,None]
# print(sample_list)
# print(type(sample_list))

# sample_list = list(1,2,3)
# print(type(sample_list))
# print(sample_list)

# sample_list = ([1,2,3,'Quest',10,25,[7,8,9], True,None])
# print(type(sample_list))
# print(sample_list)
# print(len(sample_list)) 

# print(sample_list[3])
# print(sample_list[-2])



# s = [1,2,3,'Quest', 10.25 ,[7,5,6],True,None]
# print(s[5][1])
# print(s[5[1]])

# path = "C:\Users\shakir\OneDrive\Desktop\python\str.pdf"
# print(path.removesuffix('.pdf'))


"""operations"""
"""assignment operator"""
# numbers = [1,2,3,4,5,6,7]
# numbers += 10

# numbers +=[10]
# print(numbers)

# numbers += 'shakir'
# print(numbers)

# number = [1,2,3,4,5,6,7,8,9]
# number[2] = 300
# print(number)

"""+ operator"""
# numbers = [1,2,3,4,5,6,7,8]
# sample = [20,21,22,23,24,25]
# new = numbers + sample
# print(new)


"""repetition"""
# numbers = [1,2,3,4,5,6,7,8]
# new = numbers * 10
# print(new)


# list1 = [1,2,3,4,5,6,7,8,9]
# list1 *= 10
# print(list1)

# number = [1,2,3,4,5,6,7,8,9]
# number[2] = 300
# print(number)


"""membership operator"""

# nu = [1,2,3,4,5,6,7,8,9]
# print(3 in nu)
# print(1999 in  nu)

# nu = [1,2,3,4,5,6,7,8,9,[10,20,30]]
# print(30 in nu [9])
# print(len(nu[-1]))

"""indexing"""
# nu = [1,2,3,4,5,6,7,8,9,[10,20,30]]
# print(nu[9])
# print(nu[10])
# print(nu[-5])
# print(nu[-1][-1])

# nu = [1,2,3,4,5,6,7,8,9,[10,20,30],[100,200,300,[400,500,600],700,100,300]]
# print(nu[10][3][1])
# print(nu[10][5])



# nu = [1,2,3,4,5,'richu','sarath',6,7,8,9,[10,20,30],[100,200,300,[400,500,600],700,100,300]]
# print(nu[5][2])


"""slicing"""
# nu = [1,2,3,4,5,'richu','najad',6,7,8,9,[10,20,30]]
# print(nu[5 : 7])
# print(nu[::2])
# print(nu[3:])
# print(nu[3 : -1])
# print(nu[:-1])
# print(nu[::-1])


# print(nu[6][1:4])



# matrix = [[0,1,2],[3,4,5],[6,7,8]]
# print(matrix)
# for matrix in matrix:
#     print(matrix)
# for mat in matrix:
#     for m in mat:
#         print(m)
# for mat in matrix:
#     for m in mat:
#         print(m,end=" ")


"""append is used to add to last to the list"""
# sample = [1,2,3,45,6,67,8]
# print(dir(sample))
# sample.append(3000)
# sample.append(1,3000)
# sample.append()
# sample.append('quest')
# sample.append([100,200,300])
# print(sample)



"""insert is used to insert a specific place"""
# sample = [1,2,3,45,6,67,8]
# sample.insert('python')
# sample.insert(1,'python')
# print(sample)

"""pop is used to remove from want to you want to remove """
# sample = [1,2,3,45,6,67,8]
# sample.pop()
# print(sample)

# sample.pop(1)
# print(sample)

# sample.pop(-2)
# print(sample)

"""remove is revome the specified the value"""
# sample = [1,2,3,45,6,67,8]
# sample.remove()
# print(sample)

# sample.remove(3)
# print(sample)

# sample.remove(1999)
# print(sample)


"""clear"""
# sample = [1,2,3,45,6,67,8]
# sample.clear()
# print(sample)

# sample.clear(1)
# print(sample)


"""count is used to find how Many times to find it"""
# sample = [1,2,3,45,6,6,67,8]
# print(sample.count(6))


"""copy"""
# sample = [1,2,3,45,6,67,8]
# copy_list = sample.copy()
# print(copy_list)
# copy_list[2] = 600
# print(copy_list)
# print(sample)

# sample = [1,2,3,45,6,67,8,[100,200,3000,7]]
# copy_list = sample.copy()
# print(copy_list)

# copy_list[-1][-1] = 700
# print(copy_list)

# print(sample)

"""sort it is modify the total list"""
# sample = [1,2,3,45,6,67,8]
# sample.sort()
# print(sample)

# sample.sort(reverse=True)
# print(sample)
"""key,reverse"""
# s = ['my','mame','is','hi']
# s.sort()
# print(s)

# s.sort(key=len)
# print(s)

"""extent"""
# sample = [1,2,3,45,6,67,8]
# s = ['my','mame','is','hi']
# s.extend(sample)
# print(s)
# sample.extend(s)
# print(sample)

# sample.extend('Quest in calicut')   
# print(sample)

"""index"""
# sample = [1,2,3,45,6,67,8]
# print(sample.index(2))

# sample = [1,2,3,7,7,45,


"""reverse function"""
# sample = [1,2,3,45,6,67,8]
# sample.reverse()
# print(sample)


"""function"""
"""len"""
# sample = [1,2,3,45,6,67,8]
# print(len(sample))
"""min"""
# sample = [1,2,3,45,6,67,8]
# print(min(sample))

# s = ['my','mame','is','hi']
# print(min(s))
"""max"""
# sample = [1,2,3,45,6,67,8]
# print(max(sample))

# s = ['my','mame','is','hi']
# print(max(s))
"""sum"""
# sample = [1,2,3,45,6,67,8]
# print(sum(sample))

# s = ['my','mame','is','hi']
# print(sum(s))
"""sorted"""
# s = [2883,432,5656,566]
# sample = [1,2,3,45,6,67,8]                  #
# print(sorted(sample))
# s = sorted(sample)
# print(s)








