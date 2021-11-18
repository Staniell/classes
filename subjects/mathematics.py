class Arithmetic:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Add(self):
        return self.a+self.b
    def Subtract(self,a,b):
        return a-b


class Root:
    def __init__(self,a):
        self.a = a
    def square(self):
        return self.a*self.a
