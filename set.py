# mutable , duplicates , unordered
myset = set([1 ,2 ,3])
myset.add(1)
myset.add(2)
myset.add(3)


for i in myset:
  print(i)
  if 1 in myset:
    print("yes")

#myset.discard()
print(myset.pop())
# union and intersection
odds = {1 ,3,5 ,7,9}
evens = {0 ,2 ,4 ,6 ,8}
primes = {2 ,3 ,5 ,7}
u = odds.union(evens)
#print(u)
# difference of two sets
setA = {1 ,2 ,3 ,4 ,5 ,6 }
setB = {1 ,2,3}
diff = setA.difference(setB)
#print(diff)
# symmetric difference
diff = setA.symmetric_difference(setB)
print(diff)
setA.update(setB)
print(setA)
setA.symmetric_difference_update(setB)
print(setA.issubset(setB))
print(setA.issuperset(setB))
print(setA.isdisjoint(setB))

setB = setA# you will have to use the original copy method
# frozen set
a = frozenset([1 ,2 ,3,4])
# you can not change any thing inside it either change or remove


