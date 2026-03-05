# for i in range(1,4):
#     for j in range(i):
#         print(j,end="")
#     print()


# raw = 3
# for i in range(raw):
#     for j in range(raw):
#         print("*",end="  ")
#     print()


# length = 4
# bredth = 3
# for i in range(bredth):
#     for j in range(length):
#         print("*",end="   ")
#     print()


# n = 3
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==1 or row==n or col==1 or col==n:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print() 

 
# square = 4
# for i in range(square):
#     for j in range(square):
#         print(i,end="  ")
#     print()



# square = 3
# count = 1
# for i in range(square):
#     for j in range(square):
#         print(count,end="  ")
#         count+=1
#     print()


# square = 3
# count = 5
# for i in range(square):
#     for j in range(square):
#         print(count,end="  ")
#         count+=5
#     print()



# r = 6
# c = 5
# for i in range(r):
#     for j in range(i):
#         print("*",end="  ")
#     print()




# for i in range(1,5):
#     for j in range(i):
#         print(i,end="  ")
#     print()




# r = 5
# c = 5
# count = 1
# for i in range(r):
#     for j in range(i):
#         print(count,end="  ")
#         count+=1
#     print()


# r = 4
# c = 4
# for j in range(r,0,-1):
#     for i in range(j):
#         print("*",end="  ")
#     print()



# row = 6
# for  i in range(row):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*",end=" ")
#     print()


# row = 6
# for i in range(row,0,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*",end=" ")
#     print()



# n = 5
# for row in range(0,n):
#     for col in range(0,n):
#         if row==0 or row==n-1 or col==0 or col==n-1 or row==col or row+col==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 5
# for row in range(0,n):
#     for col in range(0,n):
#         if row==col or row+col==n-1:
#             print("*",end="")
#         else:
#             print(" ",end=" ")
#     print()





# n = 6
# for row in range(n,-1):
#     for col in range(n):
#         print(" ",end=" ")
#     for k in range(row,col):
#         print("*",end="")
#     print()


# row = 6
# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()


# row = 6
# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()



# n =5 
# for i in range(n):
#     print(" " * (n-i-1) + "*" * (2 * i + 1))
# for i in range(n-2,-1,-1):
#     print(" " * (n-i-1) + "*" * (2 * i + 1))


# n = 5
# for i in range(n,0,-1):
#     print("*" * i)
# for i in range(2,n+1):
#     print("*"* i)


