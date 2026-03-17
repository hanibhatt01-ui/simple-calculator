# Simple Calculator Program (Expression Based)

print("---- Simple Calculator ----")

# Direct expression input
expression = input("Enter calculation (example: 1+2, 5*6, 10/2): ")

try:
    result = eval(expression)
    print("Result:", result)
except:
    print("Invalid input")