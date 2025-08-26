# counter , namedtuple , ordered Dict , default , deque
#from collections import Counter
#from collections import namedtuple
#from collections import OrderedDict
from collections import defaultdict
from collections import deque
#a = "aaaaaaaabbbbbbbbbccccccc"
#my_counter = Counter(a)
#print(my_counter)
#print(my_counter.most_common(1)[0][0])
#print(my_counter.elements())

# named tuple is like  a struct
#Point = namedtuple('Point', 'x,y')
#pt = Point(4,5)
#print(pt)
# to be able to access it effectively you must be able to 
#print(pt.x , pt.y)
#d = defaultdict(int)
#d['a'] = 1
#d['b'] = 2
#print(d['a'])
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
d.popleft()





