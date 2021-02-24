name = 'inae'
age = 37

#concatenate

print('hello, my name is ' + name + ' and i am ' + str(age))


#string formatting 
#---arguments by position 
print('my name is  {name} and I am {age}'.format(name=name, age=age))

#---F string (3.6)
print(f'Hello, my name is {name} and I am {age}')

#string method 
s = 'hello world'
s2 = 'HELLO WOLRD'
s3 = 'hEllo WolRd'
s4 = 'helloworld'


#Capitalize 
print(s.capitalize())

#make uppercase
print(s.upper())

#make lowercase
print(s2.lower())

#swap case 
print(s3.swapcase())

#get length 
print(len(s))

#replace
print(s.replace('world', 'inae'))

#count 
sub = 'h'
print(s.count(sub))

#starts with 
print(s.startswith('hello'))

#end with
print(s.endswith('d'))

#split into a list
print(s.split())

#find position 
print(s.find('r'))

#is all alphanumeric space is not recognized
print(s4.isalnum())

#is all alphabetic space is not recognized
print(s4.isalpha())

#is all numeric
print(s.isnumeric())



