
#from itertools  import product
#from itertools  import permutations
#from itertools  import combinations , combinations_with_replacement
#from itertools  import accumulate
import operator
from functools import reduce
#from itertools import groupby
#myList = [1 ,2 -17 ,-7 ,8 ,19 ,24 ,96 ,77  ]
#print(myList)


#if 'banana' in myList:
 # print('yes')
#else:
 # print('no')
#for i in myList:
 # print(i)
#item = myList[-1]
#print(item)
#myList2 = [5 ,True , "apple" , "cherry" ]
#print(myList2)
#print(len(myList))
#myList.append('lemon')
#print(myList)
#item = myList.sort()
#new_list = sorted(myList)
#print(myList)
#print(new_list)

#list_org = ['banana','cherry','apple']
#list_cpy = list_org.copy()
#list_cpy.append('lemon')

#print(list_cpy)
#myList = [1 ,2 ,3 ,4,5 ,6]
#b = [i + i for i in myList]
#print(myList)
#print(b)
# iter tools
#a = [1 , 2 , 3, 4]
#prod = product(a,  repeat=2)
#print(list(prod))
#perm = permutations(a,2)
#print(list(perm))
#comb= combinations(a ,2)
#print(list(comb))
#comb_wr = combinations_with_replacement(a , 2)
#print(list(comb_wr))
#acc = accumulate(a , func=operator.mul)
#print(a)
#print(list(acc))
#def smaller_than_three(x):
 # return x < 3 
#group_obj = groupby(a ,key=lambda #x:smaller_than_three)
#for key , value in group_obj:
 # print(key , list(value))

#  Lambda arg : expressions
#add10 = lambda x: x + 10
#calling it with an argument and call it with a value
#print(add10(5))
#def add10 (x):
 # return x + 10
#mult = lambda x, y: x*y
#print(mult(2 ,7))
#points2D = [(1 ,2), (15 ,1) ]
#def sort_by_y(x):
 # return x[1]
#points2D_sorted = sorted(points2D,#key=lambda x:x[1])
#print(points2D)
#print(points2D_sorted)
# using the map function  map(func , seq)
a = [ 1,2,3 ,4,5,6]
b = map(lambda x:x *2,a)
b = filter(lambda x: x % 2 ==0)
print(list(b))
l = [x + 2 for x in a]
print(l)
# filter
c = [x for x in a if x % 2 == 0]
print(c)


product_a = reduce(lambda x, y: x*y ,a)
print(product_a)


