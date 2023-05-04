# n=10
# fact=lambda n:[1,0][n>1] or fact(n-1)*n
# print(fact(5))

# def data():
#     with open("data.txt","r") as f:
#         yield f.readlines()
# for i in data():
#     print(i)

# from threading import Thread

# def func_():
#     for i in range(5):
#         print(i)
# t1=Thread(target=func_)
# t1.start()
# for j in range(10,14):
#     print(j)

# git :git is a version ctrl system.used to tracking changes in files and also allow several peoples work amongs simulteneously to 
# tracking progresss over time. installed locally on system. Does not support user management  system.
# github:github is service which is user for user management system and tracking changes overtime.it is hosted on the web and its also support 
# user management system

# git:version ctrl system,installed locally on system,does not support user management system,GUI desktop interface,no need internet
# Github:service,hosted on internet,support user management system,GITHUB desktop interface,Need internet

# push:push to local to remote repo
# pull:fetching the files in local repo and integrate with rmote repo.

# bare_repo:fetches all the changes in remote repo and saved in local repo sub folder repo instead of saved in remote repo

# def decorate(func):
#     def inner(word):
#         x=func(word)
#         return len(x)
#     return inner
# @decorate
# def sample(str_):
#     return str_
# print(sample("ankitketu"))

# protocol:it is set of rules and guidelines for communicating data.rules are defined for each step abd processes betn comm data in one or more 
# computers.Network uses this rules to transmit the data.

# payload :it is the json object which consist of one or more claims that each can be name /value pairs that desc various aspect of conext
# # where JWT was issued.

# import csv

# fields = ['Name', 'Branch', 'Year', 'CGPA'] 

# rows = [ ['Nikhil', 'COE', '2', '9.0'], 
#          ['Sanchit', 'COE', '2', '9.1'], 
#          ['Aditya', 'IT', '2', '9.3'], 
#          ['Sagar', 'SE', '1', '9.5'], 
#          ['Prateek', 'MCE', '3', '7.8'], 
#          ['Sahil', 'EP', '2', '9.1']]
# with open('main.csv',"w") as v:
#     writer=csv.writer(v)
#     writer.writerow(fields)
#     writer.writerows(rows)

# with open("main.csv","r") as f:
#     data=csv.reader(f)
#     for i in data:
#         print(i)


# inheritance in python: The mech of deriving new cls from an old one such that new class inherits all the properties of old class 
# this is called as an inheritance.
# There are 3 Typs of inheritance in python:single,Multiple,Multilevel,hierarchical
# 1.Single Inheritance:when child class inherits all the properties of only one parent class this is called as an single inheritance.


# class A:
#     def __init__(self,a,b):
#         self.b=b
#         self.a=a
#         print("hiie")
# class B(A):
#     def __init__(self,a,b,c,d):
#         super().__init__(a,b)
#         self.c=c 
#         self.d=d 
#     def display(self):
#         print(self.a+self.d)
# obj=B(10,20,30,40)
# obj.display()


# stateless protocol is protocol in which each particular cummunication is handeled as an independent event unrelated to other similar communication.
# http is also stateless protocol.

