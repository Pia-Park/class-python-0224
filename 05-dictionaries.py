#a collection of unordered, changable and indexed. no duplicate members 

#create a dict 
person = {
    'first_name' : 'inae',
    'last_name' : 'park',
    'age' : 34
}
print(person)

# use constructor 
# person2 = dict(first_name='ami', last_name='tanaka', age='17')
# print(person2)

#get value 
print(person['first_name'])
print(person.get('last_name'))

#get dict key 
print(person.keys())

#get dict items
print(person.items())

#copy dict
person2 = person.copy()
print('person2: ', person2)
person2['city'] = 'seoul'
print('person2: ', person2)

#remove item
del(person['age'])
print(person)
person2.pop('city')
print(person2)

#clear 
person.clear()
print(person)

#get length
print(len(person2))

#list of dict 
people = [
    {'name' : 'dan', 'age' : 18},
    {'name' : 'nico', 'age' : 24}

]

print(people[1]['age'])