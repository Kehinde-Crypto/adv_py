def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    return sum_of_char % 10
print("Bob has a hash code of " + str(hash_function("Bob")))

   # to be able to add these values
# to be able to add these values
hash_table = {}

def add(name):
    index = hash_function(name)
    hash_table[index] = name

add("frank")
print(hash_table)
