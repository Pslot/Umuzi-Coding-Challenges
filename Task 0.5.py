import math
# program to find the area of a triangle when all three sides are known

side_a = int
side_b = int
side_c = int

def triangle_area(side_a, side_b, side_c):
  
  s = (side_a + side_b + side_b) / 2 # formular to calculate the semi-parameter of a triangle

  area = math.sqrt (s * (s-side_a)*(s-side_b)*(s-side_c)) #formular to calculating the area of a triangle
  return area

triangle_area(side_a, side_b, side_c) 