class Rectangle():
    def __init__(self, w, h):
        self.w=w
        self.h=h
    def area(self):
        print( self.w * self.h)
    def perimeter(self):
        print(2 * (self.w + self.h))

r=Rectangle(w=20, h=30)
r.area()
r.perimeter()
class Details(object):
    def __init__(self,name, age, gender, county):
        self.name=name
        self.age= age
        self.gender= gender
        self.county= county

    def details(self):
        print(f"my name is {self.name}.My age is {self.age}.My gender is {self.gender}.My county is {self.county}")

d=Details(name="Jon Doe", age=29, gender="Male", county="Mombasa")
d.details()

class Patient_Details(object):
    def __init__(self,name, gender, weight,diagnosis):
        self.name= name
        self.gender = gender
        self.weight = weight
        self.diagnosi = diagnosis

    def details(self):
        print("Patient Details :")
        print(f"Name : {self.name} \nGender : {self.gender} \nWeight : {self.weight} \nDiagnosis : {self.diagnosi}")

p=Patient_Details("Chuck Batwoski ", "Male", "179 Pounds", "Malaria")
p.details()

class Books(object):
    def __init__(self,name, isbNo, pages, author):
        self.name= name
        self.isbNo= isbNo
        self.pages= pages
        self.author= author

    def Date_Published(self, date_published):
        print(f"Name Of The Book : {self.name} \nISBNO : {self.isbNo} \nDate Published : {date_published}")

    def Chapters(self, chapters):
        print(f"Pages : {self.pages} \nChapters : {chapters} \nAuthor : {self.author}")

b=Books("Blossoms of Savannah", "12354567", 298, "Resian Taiyo")
b.Date_Published("24th December, 2015")
b.Chapters(26)

class Rectangle(object):
    def __init__(self, width, height, color='blue'):
        self.width = width
        self.height = height
        self.color = color

    def area(self):
        print(self.width * self.height)

r=Rectangle(24, 12)
r.area()

