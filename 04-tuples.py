#a collection of ordered and unchangable values. allows duplicate members

#creat tuple
fruits = ('apple', 'orange', 'grape')
print(fruits)

#using a constructor 
fruits2 = tuple(('apple', 'orange', 'grape'))
print(fruits2)

#get a value
print(fruits[1])

# can not change value
# fruits[0] = 'pear'
# print(fruits)

#delete tuple 
del fruits2
#print(fruits2)

#get length
print(len(fruits))

#SET - unordered and unindexed. no duplicate members 

#creat set
fruits_set = {'apple', 'orange', 'grape'}
print(fruits_set)

#check if in set 
print('apple' in fruits_set)

#add to set 
fruits_set.add('pear')
print(fruits_set)

#remove from set 
fruits_set.remove('pear')
print(fruits_set)

#add duplicate
fruits_set.add('apple')
print(fruits_set)

#clear set 
fruits_set.clear()
print(fruits_set)

#delete set 
del fruits_set