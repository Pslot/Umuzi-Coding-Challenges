x = int
y = int
z = int

def maximum(x,y,z):
    
    if x > y and x > z or x == y > z or x == z > y:
        return x
    elif y > x and y > z or y == z > x:
        return y
    elif z > x and z > y:
        return z
    
maximum(x,y,z)