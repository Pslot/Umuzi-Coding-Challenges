x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

def max_of_three(x, y, z):
    
    if x > y and x > z or x == y > z or x == z > y:
        print (f"The highest number out of {x}, {y} and {z} is: ", x)
    elif y > x and y > z or y == z > x:
        print (f"The highest number out of {x}, {y} and {z} is: ", y)
    elif z > x and z > y:
        print (f"The highest number out of {x}, {y} and {z} is: ", z)
    elif x == y == z:
        print ("All numbers are equal")

max_of_three(x, y, z)