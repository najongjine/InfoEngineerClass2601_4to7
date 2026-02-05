class Animal:
    def __init__(self,leg=4,fur=True):
        self.leg=leg
        self.fur=fur
        print("animal 탄생")

class Dog(Animal):

    def make_sound():
        print("멍멍")


a=Animal()
a=Dog()

#print(a.leg)


""" 연습문제 """
class Parent:
    def __init__(self, val):
        self.val=val
        self.show()

    def show(self):
        print(f"P:{self.val}",end=' ')

class Child(Parent):
    def __init__(self,val):
        super().__init__(val+10)
        self.val=val
        self.show()
    
    def show(self):
        print(f'C:{self.val}', end=' ')

obj=Child(5)