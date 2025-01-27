# dictonary = a changeable, unordered collection of uniq keys: value pairs
#             Fast becouse they use hashing, allow us to access a value quckly


capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Pekin',
            'Russia': 'Moscow'}

print(capitals['Russia'])
print(capitals.get('Germany'))
keys = capitals.keys()
values = capitals.values()

print(keys)
print(values)

for i in keys:
    print(i)

for j in values:
    print(j)

print(capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')
#capitals.clear()

print(capitals.items())


























