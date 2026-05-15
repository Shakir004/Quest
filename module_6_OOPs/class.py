'class'
# class student:
#     pass
# print(type(student))                       #<class 'type'>


# class student:
#     pass

# richu= student()
# print(type(richu))    #object                                #<class '__main__.student'>



# class student:
#     pass

# richu =student()
# print(id(richu))                      #memory adress=2042412500704

# shakir=student()
# print(id(student))                    #memory adress=3013197793984



'methods'
# class student:
#     """method"""
#     def exam(self):                                       
#         print('exam conducted on 8/5/2026')

# """object"""
# richu = student()
# shakir= student()

# richu.exam()                 #exam conducted on 8/5/2026
# shakir.exam()                #exam conducted on 8/5/2026


"""self is used to define the current object reference parameter"""



# class student:
#     school_name= "Quist Inovative Solutions"


# class student:
#     school_name = 'Quest Inovative Solutions'            #"""class atributtes"""

# richu = student()
# yaseen = student()
# print(student().school_name)


# print(student.school_name)
# print(richu.school_name)
# print(yaseen.school_name)

# student.school_name = "qis"
# print(richu.school_name)
# print(yaseen.school_name)


# richu.school_name = 'xavio'
# print(richu.school_name)
# print(yaseen.school_name)

# del student.school_name
# print(richu.school_name)
# print(student.school_name)            #removed by class level
# print(yaseen.school_name)

# del richu.school_name
# print(richu.school_name)                #removed by object level



"""instance attribute"""

# class student:
    # school_name = 'QIS'
    # course = 'Python Full Stack'                        #class atributes

    # def __init__(self):                                #constructor
        # print("constructor is created")


# shahal = student()                                     #object
# sha = student()                                        #object



# class student:
    # school_name = 'QIS'
    # course = 'Python Full Stack'                        #class atributes

    # def __init__(self,s_id,name,age,email):                                #constructor
        # self.Student_id = s_id                                         #instance attributes
        # self.s_name = name                                             #instance attributes 
        # self.s_age = age                                               #instance attributes
        # self.s_mail = email                                            #instance attributes

    # def get_details(self):
        # print(f"Student id : {self.Student_id}\nStudent name : {self.s_name}\nAge : {self.s_age}\nEmail {self.s_mail}")                                 #fuction



# shahal = student(23,"shahal",23,"shahal@gmail.com")                                     #object
# sha = student()                                        #object
# shahal.get_details()
# niyas = student(s_id=243,name='niyas',age=23,email='niys@gmail.com')
# niyas.get_details()


class employee:
    company = "mahindra"
    brand = 'FCJD'

    def __init__(self,e_id,name,salary,email):
        self.emp_id= e_id
        self.e_name=name
        self.salary=salary
        self.mail=email

    def details(self):
        print(f"employee id : {self.emp_id}\nName : {self.e_name}\nSalary : {self.salary}\n Email : {self.mail}")

    def update(self):
        if self.salary>100000:
            increment = self.salary * 0.15
            self.salary += increment
            print(f"updated salary : {self.salary}")


    def update_company(self):
        self.company='GOOGLE'
        print(self.company)   

         
            

detailsss = employee(e_id=234,name='shakir',salary=230000,email='shakir@gmail.com')
detailsss.details()
# detailsss.update_company()
# de = employee(23,'sha',2330,'sha@gamil.com')
# de.details()  
 
shhhha= employee(12,'sha',1000000,'sha@gmail.com')
shhhha.update()
# shhhha.update_company()
