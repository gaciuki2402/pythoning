s={1, 2, 3, 4}
i = iter(s)
print(i)
a= next(i)
print(a)
b= next(i)
print(b)
c = next(i)
print(c)
print("XXXXXXXXXXXXXXXXXXXXXX")
#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
m= MyNumbers()
i= iter(m)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
class even_numbers:
    def __iter__(self):
        self.w =2
        return self
    def __next__(self):
        if self.w<=12:
            x = self.w
            self.w+=2
            return x
        else:
                raise StopIteration
e=even_numbers()
p=iter(e)
for x in p:
    print(x)
print("above are even numbers")

class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a +=1
            return x
        else:
            raise  StopIteration
n= Numbers()
i= iter(n)
for x in i:
    print(x)

print('*************************')
class odd_numbers:
    def __iter__(self):
        self.d=1
        return self
    def __next__(self):
        if self.d<=10:
            o=self.d
            self.d +=2
            return o
        else:
            raise StopIteration
odd=odd_numbers()
number=iter(odd)
for o in number:
    print(o)

class tens:
    def __iter__(self):
        self.t = 10
        return self
    def __next__(self):
        if self.t <=90:
            s=self.t
            self.t +=10
            return s
        else:
            raise StopIteration

T=tens()
r=iter(T)
for t in r:
    print(t)

