# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = []
# for x in fruits:
#   if "a" in x:
#     newList.append(x)
#     print(newList)

# def myFunc(n):
#   return abs(n - 50)
# thislist = [100 , 50 , 65 , 82 , 23]
# thislist.sort(key=myFunc)
# print(thislist)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])


# # to be able to convert a set to a list
# # thistuple = ("apple", "banana", "cherry")
# # y = list(thistuple)
# # y.append("orange")
# # thistuple = tuple(y)

# # fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# # (green, yellow, *red) = fruits

# # print(green)
# # print(yellow)
# # print(red)

# # fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# # (green, *tropic, red) = fruits

# # print(green)
# # print(tropic)
# # print(red)


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# # set3 = set1.symmetric_difference(set2)

# print(set3)

# class Person:
#   def __init__(self , name , age):
#     self.name = name
#     self.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()
 # the self parameter is an instance of the the current class , which is used to get variables from the class 

# class Person:
#   def __init__(self, fname , lname):
#     self.fname = fname
#     self.lname = lname
#     def printname(self):
#       print(self.fname , self.lname)
#       x =Person("John Doe")
#       x = printname()

class Student(Person):
   def __init__(self, fname, lname, year):
      Person.init__(self, fname, lname)
