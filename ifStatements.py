x=0
y=3
if x<y:
    print("Yes!")
x=30
if x>50:
    print("(First suite)")
    print("x is small")
else:
    print("(Second suite)")
    print("x is large")
print("*"*67)
name="grace".title()
if name=="Grace":
    print("Hello grace!")
elif name=="Davie":
    print("Hello Davie!")
elif name=="Karen":
    print("Hello Karen!")
elif name=="Kendi":
    print("Hello Kendi!")
else:
    print("I don't know you!")

Names={
    "Fred":"Hello Fred",
    "Grace":"Hello Grace",
    "Xander":"Hello Xander",
    "Davie":"Hello Davie"
}
print(Names.get("joyce", "I don't know who you are!"))
print(Names.get("Davie","I don't know who are you!"))
print("x"*67)
raining=False
print("Let's go to the beach.")
if True:
    pass
    print("Good")
if False:
    print("Python is such a vibe")
else:
    print("I love django more than python")



