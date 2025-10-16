import math

class Line:
    
 def __init__(self,coordinateA,coordinateB):
  self.coordinateA = coordinateA
  self.coordinateB = coordinateB
 
 def distance(self):
  x1,y1=self.coordinateA
  x2,y2=self.coordinateB
  d = math.sqrt((x2-x1)**2 +(y2-y1)**2)
  return d
 
 def slope(self):
  x1,y1=self.coordinateA
  x2,y2=self.coordinateB
  s=(y2-y1)/(x2-x1)
  return s

c1 = (3, 2)
c2 = (8, 10)
myline = Line(c1, c2)

print("Distance:",myline.distance())
print("slope:",myline.slope())
