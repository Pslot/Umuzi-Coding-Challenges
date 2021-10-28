#function that converts temperature in Celsius to Fahrenheit
def c_to_f(C):
    return ((9/5)*C) + 32 #formlar to convert Celsius to Fahrenheit

#function that converts temperature in Fahrenheit to Celsius
def f_to_c(F):
    return (5/9)*(F-32) #formular to convert Fahrenheit to Celsius

temp = float(input("Enter a temperature "))
choice = input("Was that temperature in Fahrenheit or Celsius? (c/f?): ")
if choice=="c":
    print(temp,"Celsius is",c_to_f(temp),"Fahrenheit")
else:
    print(temp, "Fahrenheit equals", f_to_c(temp), "Celsius")