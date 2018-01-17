print("------------------------------------")
class parent:
    p_attr=100
    def __init__(self):
        print("Base Class")
    def pr_method(self):
        print("parent method")
    def setAttr(self,attr):
        parent.p_attr=attr
    def getAttr(self):
        print(parent.p_attr)
class child(parent):
    def __init__(self):
        print("child class")
    def c_method(self):
        print("child method")
c=child()
c.c_method()
c.pr_method()#e
c.setAttr(150)#e
c.getAttr()#e

print("-----------------------------------------")
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print(self.name)
        print(self.age)
class teacher(person):
    def __init__(self,name,age,exp,r_area):#extensibility
        person.__init__(self,name,age)
        self.exp=exp
        self.r_area=r_area
    def disp(self):
        person.disp(self)
        print(self.exp)
        print(self.r_area)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def disp(self):
        person.disp(self)
        print(self.course)
        print(self.marks)
print("----Teacher Details----")
ob=teacher("xyz",43,20,"python")
ob.disp()
print("----Student Details-----")
obj1=student("Mehak",20,"CSE",123)
obj1.disp()

print("------------------------------------------------")
class base1:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(self.name)
class base2:
    def __init__(self,name1):
        self.name1=name1
    def disp(self):
        print(self.name1)
class base3(base1,base2):
    def __init__(self,name,name1):
        base1.__init__(self,name)
        base2.__init__(self,name1)
    def disp(self):
        base1.disp(self)
        base2.disp(self)
ob=base3("Mehak","sachdeva")
ob.disp()
            
