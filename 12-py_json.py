import json

#sample JSON 
userJSON = '{"first_name":"Inae", "last_name":"park", "age":34}'

#parse to dict 
user = json.loads(userJSON)
print(user)
print(user['first_name'])

car = {'make': 'toyota', 'model':'soora', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)