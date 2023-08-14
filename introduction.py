print("hello world")
#integer
a=2
print(a)
d=2739
print(d)
t=35367
print(t)

#floating point
pi=3.14237
print(pi)

#strings
name="jonDoe"
print(name)
school="Taita"
print(school)
#boolean
r=True
print(r)

#null data type
x=None
print(x)

a=2
print(type(a))
pi=3.1437
print(type(pi))
r=True
print(type(r))
name="jonDoe"
print(type(name))
school="Taita"
print(type(school))
t=None
print(type(t))
a, b, c=1, 2, 3
print(a, b, c)
a, b, c="cow,", "goat,", "pig"
print(a, b, c)
a=b=c=1
print(a, b, c)
x=y=[17,34,45]
y=[21,14,37]
print(x)
print(y)
#nested lists
x = [1, 2, [3, 4, 5,], 6, 7]
print (x[1])
print(x[2][0])
p=[1, 2, 3, 4, 5, [21, 34, [23, 78, 199, 2976, [2134, 345, 311, 443,],21], 8, 9, 60,], 235]
print(p[5][2][5])
#indentation
def my_function():
    a=2
    return a
print(my_function())
def my_function():
    name="goat"
    return name
print(my_function())
def my_function():
    pi=3.12467
    return pi
print(type(my_function()))

c=[1,2,3]
print(c)
f=["a", 1, "python",(1,2,3),[1, 2]]
print(f[4][1])
print(3)
a={1,2,'q'}
print(a)
a={1:"goat",
    2:"piggy",
    3:"cow"}
print(a)
#lists
names=["alice","craig","diana","bob"]
print(names[2])
print(names[-1])
names[0]="ann"
print(names)
names.append("nia")
print(names)
names.insert(3, "nikki")
print(names)
names.remove("bob")
print(names)
print(names.index("diana"))
print(names)
print(len(names))
names.reverse()
print(names)
names.pop()
print(names)
names.reverse()
print(names)
import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))




