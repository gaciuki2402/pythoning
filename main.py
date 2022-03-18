print("Hello,{}".format("Bob"))
t="Hey {name} there is a 0x {errno} error!"
print(t.format(name="Grace", errno="badcoffee"))
g="Good morning {name}, welcome to {company_name} company."
print(g.format(name="Gaciuki", company_name="Microsoft"))
w="Hello {name}, their will be a {unit} class at {room}."
print(w.format(name="MCS Class", unit="Data Structures and Algorithms", room="AB6-004"))
a=254
b=300
print(f"the summation of a and b is {a+b} and the multiplication of a and b is {a*b}. ")
print("*"*67)
def greet(name,question):
    return f"Hello,{name}! How's is {question}?"
print(greet("Grace", "going"))

def quiz(name,question):
    return f"Hello {name}, is the {question} running"
print(quiz("David", "code"))
def about(institution,name):
    return f"is {institution} located at {name}? "
print(about("Taita Taveta University", "Voi-Mwatate Road"))
print("*"*78)
from string import Template
t=Template("Hey,$name!")
print(t.substitute(name="Bob"))
f=Template("Good afernoon,$name?")
print(f.substitute(name="Candidates"))
string="Hello,$name,helps alot.It solves an $errorno error perfectly!"
print(Template(string).substitute(name="Real Python", errorno=hex(3)))
print("x"*56)
def output(n):
    return f"The number is {n}"
number_list=[12,45,67,87]
m=map(output,number_list)
print(m)
for sentence in list(m):
    print(sentence)

from datetime import datetime
Time="North America:{dt:%m/%d/%Y}. ISO:{dt:%Y-%m-%d}.".format(dt=datetime.now())
print(Time)

