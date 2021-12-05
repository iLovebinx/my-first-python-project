import math

number1 = input ("mumber 1")
number2 = input ("number 2")
opperation = input (

    "1 : Add\n" 
    "2 : Subtract\n"
    "3 : Divide\n"
    "4 : Modulo\n"

)

def calculateAdd (num0, num1):
     return (int(num0) + int(num1))

def calculateSubtract (num0, num1):
     return (int(num0) - int(num1))

def calculateDivide (num0, num1):
     return (int(num0) / int(num1))

def calculateMod (num0, num1):
     return (int(num0) % int(num1))

result_add = (calculateAdd(number1, number2))
result_subtract = (calculateSubtract(number1, number2))
result_divide = (calculateDivide(number1, number2))
result_mod = (calculateMod(number1, number2))


if opperation == ("1"):
    print (number1, + "plus" + number2 + "is")
    print (result_add)

elif opperation == ("2"):
    print (number1, + "minus" + number2 + "is")
    print (result_subtract)

elif opperation == ("3"):
    print (number1, + "divide" + number2 + "is")
    print (result_divide)

elif opperation == ("4"):
    print (number1, + "mod" + number2 + "is")
    print (result_mod)

else:
    print ("invalid input")

print ("done")






















