class class2(): 
    def __init__(self): 
        pass 
    def area(self): 
        return 0 
class kvadrat(class2): 
    def __init__(self, a): 
        class2.__init__(self) 
        self.a = a 
 
    def area(self): 
        return self.a*self.a 
 
sq= kvadrat(int(input())) 
print (sq.area())