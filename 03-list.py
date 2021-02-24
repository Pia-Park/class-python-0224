#a list is a collocetion of orderd and changabel

#Create list 
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'banana', 'grape', 'kiwi']

#use a constructor dont recommand 
# number2 = list((1,2,3,4,5))
print(numbers)
# print(number2)

#get a value 
print(fruits[1])

#get last value
print(fruits[-1])

#length
print(len(fruits))

#append to list 
fruits.append('strawberry')
print(fruits)

#remove fron list 
fruits.remove('grape')
print(fruits)

#insert into position 
fruits.insert(1, 'ddalgi')
print(fruits)

#change the value 
fruits[0] = 'gala apple'
print(fruits)

#remove with pop 
fruits.pop(2)
print(fruits)

#reverse sort 
fruits.reverse()
print(fruits)

#sort list 
fruits.sort()
print(fruits)

#reverse sort
fruits.sort(reverse=True)
print(fruits)