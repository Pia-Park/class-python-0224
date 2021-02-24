people = ['ami', 'inae', 'kideok', 'marina']

#simple loop 
for person in people:
    print(f'Current person: {person}')

#break 
for person in people:
    if person == 'kideok':
        break
    print(f'Break Current person: {person}')

#continue 
for person in people:
    if person == 'inae':
        continue #skip 
    print(f'Continue Current person: {person}')

#Range 
for i in range(len(people)):
    print('range: ', people[i])

for i in range(0, 3):
    print(f'Numbers: {i}')

#while loops
count = 0 
while count < 10:
    print(f'count: {count}')
    count += 1
