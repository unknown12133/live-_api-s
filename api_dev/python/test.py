# print("Hello World")
# name=input("Enter your name: ")
# age=input("Enter your age: ")
# print(type(age))
# age=int(age)
# print(type(age))
# print("Name:", name)
# print("Age:", age)

# ==============list============

# a=[1,2,3,'a','b','c']
# print(a[1])
# try:
#     print(type(a[7]))
# except :
#     print("Index out of range")

# print(type(a[1]))

# ==============dictionary(json)============
# a={
#     1:1,
#     'a':2,
#     'c':'hi'
# }
# print(a)
# print(a['a'])
# print(a[1])
# print(a['c'])

# ==============if condition============

# if 10<20:
#     # print("10 is greater than 20")
#     raise Exception("10 is greater than 20")
    

# else:
#     print("20 is greater than 10")

# print("Hello World")

# ==============loops============

users=['a','b','c']
# for user in users:
#     if user=='a':
#         print(user)
#     else:
#         print("User not found")
#         # raise Exception("User not found")
# print("Hello World")

# a={
#     'a':1,
#     'b':2,
#     'c':3
# }
# for key in a.values():
#     print(key)
# for key in a.keys():
#     print(key)
# for key,value in a.items():
#     print(key,value)

# ==============functions============
# def add(a,b):
#     return a+b
# print(add(1,2))

# def add(a,b):
#     return a+b
# print(add(1,2))

# def add(a,b):
#     return a+b
# print(add(1,2))

# ==============classes============

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(a,b):
#         return a+b
# a=A(1,2)
# print(a.add(1,2))

# ==============inheritance============

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self,a,b):
#         return a+b

# class B(A):
#     def __init__(self,a,b):
#         super().__init__(a,b)
#     def sub(self,a,b):
#         return a-b
# a=B(1,2)
# print(a.a)
# print()
# print(a.b)
# print()
# print(a.add(1,2))
# print()
# print(a.sub(1,2))

# ==============task============

def add_user(name,age):
    if age <18:
        return "Age must be greater than 18"
    return{
        'name':name,
        'age':age
    }

print(add_user('sai',17))

