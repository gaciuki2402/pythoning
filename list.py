p=[1,2,3,4,5]
print(p)
p.insert(0,6)
print(p)
p.append(7)
print(p)
y=[9,70]
p.append(y)
print(p)
p.pop()
print(p)
p.extend(y)
print(p)
p.extend(range(2))
print(p)
print(p.index(6,0))
print(p.pop(0))
print(p.remove(3))
print(p.count(1))
print(p.sort())

class Person(object):
    def __init__(self, name, height):
        self.name=name
        self.height=height

    def __repr__(self):
        return self.name
l = [Person("John Cena", 176),
   Person("Chuck Norris", 180),
   Person("Jon Doe",127)]
l.sort(key=lambda item: item.name)

my_list=['foo','bar', 'baz']
for item in my_list:
    print(item)

for (index, item) in enumerate(my_list):
    print('The item in position {} is: {}'.format(index, item))

print("***************")
