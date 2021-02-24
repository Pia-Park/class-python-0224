#create class 

class User:
    #constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        # self._private = 1000

    def printMe(self):
        return f'{self.name}'
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    # def print_encap(self)
    #     print(self._private)

inae = User('Inae Park', 'inae@mail.com', '34')
print(inae.printMe())
print(inae.greeting())


# inae.print_encap()
# inae._private = 800
# inae.print_encap()

#extend class
class Customer(User):
    def __init__(self, name, email, age):
        User.__init__(self, name, email, age)
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    def set_balance(self, balance):
        self.balance = balance

huntory = Customer('Huntory Park', 'huntory@mail.con', '36')
huntory.set_balance(400)
print(huntory.greeting())
    
