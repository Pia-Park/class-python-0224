#create a function  
def sayHello(name='Stranger'):
    print('Hello,', name)

sayHello('inae')
sayHello() #print default 

#return values 
def getSum(num1, num2) :
    total = num1 + num2 #total is only belongs in the function 
    return total
print(getSum(2,5))

#LAMBDA function - a small anomymouse function 
# () => {}
# functino()=>{} javascript 
#JS: getSum = (num1, num2) => num1 + num2
#only have 1 expression 
getSum = lambda num1, num2: num1 + num2
print(getSum(10,2))
