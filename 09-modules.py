#core modules 
import datetime
from datetime import date
import time
from time import time

today = date.today() #short ver.
print(today)
timestamp = time()
print(timestamp)

#PIP modules <- includes Django 
# import camelcase
# from camelcase import camelcase
# c = Camelcase()
# print(c.hump('hello'))

#custom modules 
import validator
from validator import validate_email
email = 'test@mail.com'
if validate_email(email):
    print('Email is valid')
else :
    print('email is invalid')

