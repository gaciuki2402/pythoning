d={'a':1, 'b':2, 'c':3}
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

from collections import OrderedDict
fish=OrderedDict()
dog=OrderedDict()
fish={'name':'Nemo', 'hands':'Fins', 'special':'Gills'}
dog={'name':'Clifford', 'hands':'paws', 'color':'red'}
fish.update(dog)
print(fish)
print(fish.keys())
print(dog.values())
print(fish['special'])
print(dog['name'])
for key in fish:
    print(key, fish[key])
    
