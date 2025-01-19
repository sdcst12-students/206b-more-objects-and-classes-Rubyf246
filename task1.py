#!python3
#Task 1:
#Use the comments in the template to create the program that will use the quadratic formula to find out all kinds of things about a quadratic equation in the format:
#ax^2 + bx + c = 0
import math
class quadratic:
    a = 0
    b = 0
    c = 0
    roots = []

    def discriminant(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the discriminant which is calculated as 
        # b^2 - 4ac
        # return value should be a float type decimal
        d =  ((self.b)**2) - (4 * self.a * self.c)
      
        return   d
    
    def hasRealRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic has real roots
        # defined when the discriminant is non negative
        # return value should be True or False
        if self.discriminant() < 0:
            return False
        else:
            return True

    def isFactorable(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic can be factored
        # quadratic can be factored if the discriminant is a perfect square
        # return value is True or False
        i = self.discriminant() 
        if i < 0:
            return 0
        else: 
            return i == math.sqrt(i) ** 2
       
    
    def calcRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the roots of the quadratic if
        # the quadratic has real roots
        # should make use of the class methods:
        # self.hasRealRoots()
        # self.discriminant
        # method does not have a return value
        # but should store the values of the roots in the 
        # list self.roots
        # list should be sorted in ascending order
        # roots should be rounded to 2 decimal places
        # Solve the quadratic equation ax**2 + bx + c = 0
        d = self.discriminant() 
        if d>=0: 
            r1 = (-self.b - math.sqrt(d))/(2*self.a)
            r2 = (-self.b + math.sqrt(d))/(2*self.a)
               
            round_r1 = round(r1,2)
            round_r2 = round(r2,2)
            self.roots= [round_r1, round_r2]
            self.roots.sort
       
        return
        
    def axisOfSymmetry(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the x value that is for the equation
        # of the axis of symmetry
        # should return the x value for the axis of symmetry
       
        b = self.b
        a = self.a
        x = -b/2*a
         
        return x

    def vertex(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the x,y value of the vertex
        # should return the a list with the x and y coordinates of the vertex
        b = self.b
        a = self.a
        c = self.c
        
        xcoord = -b/2*a
        ycoord = a*(xcoord**2) + b*xcoord +c
        vertex = [xcoord, ycoord]
       
        return vertex
        
    def __init__(self, inputa, inputb, inputc):
        # this should require 3 positional arguments and assign the values
        # to self.a, self.b and self.c
        self.a = inputa
        self.b = inputb
        self.c = inputc
        self.calcRoots()
        
        pass



if __name__ == "__main__":
    q1 = quadratic(1,4,4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.roots == [-2,-2]
    assert q1.axisOfSymmetry() == -2
    assert q1.vertex() == [-2,0]

 
    q2 = quadratic(1,1,-6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    #print (q2.roots)
    assert q2.roots == [-3,2]
    assert q2.axisOfSymmetry() == -0.5
   # print (q2.vertex() )
    assert q2.vertex() == [-0.5,-6.25]

    q3 = quadratic(1,1,10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.roots == []
    assert q3.axisOfSymmetry() == -0.5

    q4 = quadratic(1,10,1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    
    assert q4.roots == [-9.90,-0.10]
    print (q4.axisOfSymmetry())
    assert q4.axisOfSymmetry() == -2.5 # the correct answer is -5
 