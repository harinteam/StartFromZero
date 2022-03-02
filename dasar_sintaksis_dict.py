users = {
    'id': 1,
    'name': 'John Joselvi',
    'username': 'jonijon',
    'email': 'joni1@gmail.com',
    'address': {
        'street': 'Holliwood Street',
        'suite': 'Apt. 99',
        'city': 'Tokyo',
        'zipcode': '239120',
        'geo': {
            'lat': '-34.3159',
            'lng': '81.149'
        }
    }
}
print(users)
print(users['email'])
print(users['address']['suite'])
print(users['address']['geo']['lat'])

print('\n')
print(users)
print(type(users))

print('\n# Ubah dict ke json')
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)