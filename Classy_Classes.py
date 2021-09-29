class Person:
    def __init__(self,name,age):
        self.info="#{name}s age is #{age}"
    def __str__(self):
        return self.info
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
    