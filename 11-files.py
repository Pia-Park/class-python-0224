#open file 

myFile = open('myFile.txt', 'w')

#get some info 
print('File name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

#write to file 
myFile.write('Inae wants to eat something.')
myFile.write('hungry!!!!!!')
myFile.write(' hungry!!!!!!')
myFile.close()

#append to file 
myFile = open('myFile.txt', 'a')
myFile.write('append!')
myFile.close()

#Read from file 
myFile = open('myFile.txt', 'r+')
text = myFile.read(100) 
print(text)