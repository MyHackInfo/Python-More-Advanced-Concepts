from functools import singledispatch

class calcul:
    @singledispatch
    def add(self,a,b):
        self.a=a
        self.b=b
        return a+b
    @singledispatch
    def sub(self,a,b):
        self.a=a
        self.b=b
        return a-b

val=calcul()
print(val.add(3,4))
print(val.sub(8,4))
