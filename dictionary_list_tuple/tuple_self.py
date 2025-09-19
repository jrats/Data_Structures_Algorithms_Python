new_tuple = ('a','b','c','d','e')
print(new_tuple)
single_tuple = ('a',)   # if it's a single element tuple a comma is needed at the end , elese it will be treated like a string
print(single_tuple)
tup =('a')
print(tup)   #wil be treated as a string

t = tuple('abcde')
print(t)

for i in range(len(new_tuple)):
    print(new_tuple[i])

print('c' in new_tuple)

print(new_tuple.index('c'))

#can perform linear search using for loop

t1 = (1,4,2,6,3,7)
t2 = (2,3,4,5,6,5,9)

print(t1+t2)
print(t1*3)
print(t2.count(5))

print(min(t1))
print(max(t2))

l1 = [1,5,3,4,6,3]
l2 = [6,2,6,3,6,4]

l1[2]=89

#l1=l2
print(l1)

# t1[2]=90  # gives error

t1 = t2
print(t1)

#del t1[4]  #gives error

del t1
print(t1)  # will say t1 not defined, since t1 is deleted

nested_tuple = ((1,2,3),(3,4,2),(8,9))
print(nested_tuple)