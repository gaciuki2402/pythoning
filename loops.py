n=5
while n>1:
    n-=1
    print(n)

m=10
while m>0:
    m-=1
    if m==6:
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







