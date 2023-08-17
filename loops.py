n=5
while n>1:
    n-=1
    print(n)

m=10
while m>3:
    m-=1
    if m==2:
        break
    print(m)
print("Loop ended")
# names=["Grace","Lizzy","Fortress","Valencia","Elsy","Janet"]
# while names:
    # if names=="Elsy":
        # continue
    # print(names)
# print("LOOP ENDED.")

names=["Grace","Lizzy","Fortress","Valencia","Elsy","Janet"]
for name in names:
    # print(name)
    if name=="Elsy":
        continue
    print(name)
def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i*j ==6:
                return (i)
            print(i*j)
break_all()
print("x"*78)
for i in range(5):
    print(i)

animals=["Cow","Dog","Giraffe","Lion","Cat"]
for index, animal in enumerate(animals):
    print(index,"....>",animal)

for i in range(3):
    print(i)
else:
    print("done")
i=0
while i<3:
    print(i)
    i+=2
else:
    print("done")
print("x"*67)
for t in range(5):
    print(t)
    if t==3:
        break
else:
    print("done")
a=[12,36,47,89,6]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("No exception")
for x in range(10):
    pass#we don't want to do anything
d={1:"Grace",2:"Davie",3:"Risper",4:"Gaciuki",5:"Peni"}
for key, value in d.items():
    print(key,":", value)

a=10
while True:
    a=a-2
    print(a)
    if a<4:
        break
print("DONE.")
while True:
    break
print("Infinite Looop")
while int:
    print(int)
    break
print("####################")

r= 0
while r<4:
    print(r)
    if r == 4:
        print("breaking from loop")
        break
    r +=1

t=1
while t<8:
    print(t)
    if t ==6:
        print("breaking")
        break
    t+=1

print("xxxxxxxxxxxxxxxxxxxxxxx")
p= 1
while p<15:
    print(p)
    if p==11:
        print("i know numbers.")
        break
    p+=2

y=(0,1,2,3,4)
for x in y:
    print(x)
    if x==2:
        break

w=["goat","cow", "pig", "cat", "sheep"]
for m in w:
    print(m)
    if m== "pig":
        print("these are domestic animals")
        break
print("************************")
for m in w:
    if m == "cow" or m=="cat":
        continue
    print(m)

students={"grace", "agnes","sharon","kezzy", "mirriam"}
for s in students:
    print(s)
    if s=="agnes" or s== "kezzy":
        continue
    print(s)

#nested loops
def break_loop():
    for j in range(1,5):
        for i in range(1,4):
            if i*j==8:
                return(i)
            print(i*j)

#for loops
for i in [0,1,2,3,4]:
    print(i)

for i in range(5):
    print(i)

for x in ['one','two','three', 'four']:
    print(x)

details={"key":"value",
   "name":"grace",
   "gender":"female",
   "age":"22years",
   "city":"nairobi"}
for key, value in details.items():
    print(key,":", value)
for b in range(5,10):
    print(b)

positions={1:"jon doe",
           2:"purity murugi",
           3:"aiden mirugi"}
for key, value in positions.items():
    print(key,':',  value)

#loops with clause
for i in range(3):
    print(i)
    if i==1:
        continue
else:
    print('done')


print("*****************8")
while t<3:
    print(t)
else:
    print("done")

list=[1,2,3,4,5,6,'dog',50,59.94,('grace')]
for a in list:
    if type(a) is not int:
        print(a)
        continue
else:
    print("no exception")
for a in list:
    if type(a) is int:
        print(a)
        continue
else:
    print("no exception")

#iterating over dictionary
pets={1:'lizzy',
      2:'skyler',
      3:'jon',
      4:'emmy'}
for value in pets.values():
    print(value)
for key in pets:
    print(key)
for key, value in pets.items():
    print(key, ':', value)
#half loop
y=10
while True:
    y=y-1
    print(y)
    if y<8:
        break
print("DONE.")
list=['alpha','bravo', 'charlie','delta','echo']
for s in list:
    print(s[:2])
for idx, s in enumerate(list):
    print("%s has an index of %d" % (s, idx))
for i in range(2, 4):
    print("list at %d contains %s"% (i,list[i])) #iterating over a sublist
