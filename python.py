for x in "banana":
    print(x)

names=["grace","gaciuki","joyce","peni","belta"]
for name in names:
    print(name)
print(len(names))
text="The best things on life are free!"
print('free' in text) #free is present in text
print("by" in text)
if "life" in text:
    print("Yes,life is present.")
if "expensive" != text:
    print("No,expensive is NOT present.")
c="Grace loves python."
print(c.endswith("python."))
s="wwiwi"
print(s[0])
print(type(s))
u=s.encode("utf-8")
print(u)
s="www.realPython.com".strip("comw.")
print(s)
p="####hello###".lstrip("#").rstrip("#")
print(p)
t="Arthur: three!".removeprefix("Arthur: ")
print(t)
t="HelloPython".removesuffix("Python")
print(t)
s="string methods in python".replace(" ", "-")
print(s)
s="string methods in python".rsplit(" ", maxsplit=2)
print(s)















