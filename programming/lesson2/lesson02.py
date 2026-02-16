# #print("hello wolrd")
# n = input ("Enter your name ")
# print(f"Hello, {n}")
#
# a = 5
# b = 2
# print (f"{a} * {b} = {a*b}")
#
# # lesson 02
# # Nested math Operations
# # Formatting print statements
# #Example calculator
#
#
# #result = 5 + 3 - 6 * 2
# #result2 = (4 + 3) * (5 - 4)
# #result3 = 3**2 + 2 + 2
# #print(result)
# #print(result2)
# #print(result3)
# pi = 3.14159265358979324
# print(f"{pi:.5f}" )
# print(f"{pi:.2f}" )
#
# print(f"{int(pi)}")

a = float(input("enter a number plz: "))

b = float(input("enter a second number plz: "))


def storefunction(price):
    aftertax = price * 1.1
    aftertaxanddiscount = aftertax *0.7
    return aftertaxanddiscount

def floordivide(numerator, divisor):
    quotient = numerator // divisor
    remainder = numerator % divisor
    return  quotient, remainder


operations_menu = """
== operations_menu ==
1. addition
2.subtraction
3.multiplication
4.Division
5.exponentiation
6. tax (+ 10%) and discount (-30%)
"""

print (operations_menu)



c = input("Operations? ")



if c == 1:
    print(f"{a} + {b} = {a + b}")
if c == 2:
    print(f"{a} - {b} = {a - b}")
if c == 3:
    print(f"{a} * {b} = {a * b}")
if c == 4:
    print(f"{a} / {b} = {a / b:.3f}")
if c == 5:
    print(f"{a} ^ {b} = {a ** b}")
if c == 6:
    a2 = storefunction(a)
    b2 = storefunction(b)
    print(f"tax / discount {a} = {a2:.2f}")
    print(f"tax / discount {b} = {b2:.2f}")
    print(f"total for both {a2 + b2:.2f}")
    price = 5.99
    aftertax = price * 1.1
    aftertaxanddiscount = aftertax *0.7









