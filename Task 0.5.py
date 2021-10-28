import math
# program to find the area of a triangle when all three sides are known

side_a = int(input("Enter any number: "))
side_b = int(input("Enter any number: "))
side_c = int(input("Enter any number: "))

def triangle_area(side_a, side_b, side_c):
  # To find the Semi-parameter
  s = (side_a + side_b + side_b) / 2

  # To find the area
  area = math.sqrt (s * (s-side_a)*(s-side_b)*(s-side_c))
  print(area)

triangle_area(side_a, side_b, side_c) 