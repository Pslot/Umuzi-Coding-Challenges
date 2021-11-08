a = int
b = int
c = int
d = int

def maximum(a,b,c):
    
    if a > b and a > c or a == b > z or a == c > b:
        return a
    elif b > a and b > c or b == c > a:
        return b
    elif c > a and c > b:
        return c
    
maximum(a,b,c)

def maximum(a,b,c,d):
    
  if a > b:
    if a > c:
      if a > d:
        return a
      else:
        return d
    else:
      if c > d:
        return c
      else:
        return d
  else:
    if b > c:
      if b > d:
        return b
      else:
        return d
    else:
      if c > d:
        return c
      else:
        return d

maximum(a,b,c,d)     