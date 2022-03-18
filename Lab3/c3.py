class class3(): 
    def __init__(self): 
        pass 
    def area(self): 
        return 0 
class Rectangle(class3): 
    def __init__(self, a,b): 
        class3.__init__(self) 
        self.a = a 
        self.b = b 
    def area(self): 
        return self.a*self.b 
 
n,m = map(int,input().split()) 
answer= Rectangle(a = n,b =m) 
print (answer.area())