
class student:
    def __init__(self,r,n,ci,ag,c):
        self.roll = r
        self.name = n
        self.city = ci
        self.age = ag
        self.course = c

S = student(23,"vivek","pune",23,"Python")
print(type(S))
print(id(S))

class motorcycle:
    def __init__(self,b,e,f,s,c):
        self.brand = b
        self.engine_cc = e
        self.fuel_capacity = f
        self.speed = s
        self.colour = c

MC = motorcycle("TVS",125,10,120,"black")
print(type(MC))
print(id(MC))


class smartphone:
    def __init__(self,b,m,s,r,ba):
        self.brand = b
        self.model = m
        self.ROM = s
        self.RAM = r
        self.battery = ba

SM = smartphone("Vivo","T3x","128 GB","6 GB","5000 mah")
print(type(SM))
print(id(SM))


class coffeeshop:
    def __init__(self,n,l,fo,ot,ct):
        self.name = n
        self.franchisee_owner = fo
        self.location = l
        self.opening_time = ot
        self.closing_time = ct
cs = coffeeshop("Starbucks","pune","atharva","8 AM","11 PM")
print(type(cs))
print(id(cs))


class Institute:
    def __init__(self,n,a,c,co,e):
        self.Name = n
        self.address = a
        self.contact_no = c
        self.email = e
        self.Courses = co

I = Institute("The kiran Academy","Pune",8888809416,"xyz@thekiranacademy.com",["java","python","MARN"])
print(type(I))
print(id(I))



        
        




        
