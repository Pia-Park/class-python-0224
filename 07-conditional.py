x = 20
y = 21
z = 9

#conparison operator (==, !=, >, <. >=, <=)

#simple if
if x > y:
    print(f'{x} is greater than {y}')

#if else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

#elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

#nested if 
if x > 2:
    if x <=10:
        print(f'{x} is greater 2 and less than or equal to 10')


#logical operators (and, or , not)
if z > 2 and z <= 10:
    print(f'{z} is greater 2 and less than or equal to 10')

#or 
if z > 2 or y <= 10:
    print(f'{z} is greater 2 or less than or equal to 10')

#not 
if not(x==y):
    print(f'{x} is not equal to {y}')

#membership operator (not, not in )

numbers = [1,2,3,4,5]
#in
if x in numbers:
    print(x in numbers)

#not in 
if x not in numbers:
    print(x not in numbers)

#identity operator( is , is not)
if x is y:
    print('IS: ', x is y)

if x is not y :
    print('IS NOT: ', x is not y)