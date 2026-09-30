print ("__________ MINI CALCULATOR ________")
N1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
N2 = float(input("Enter second number: "))
if operator == "+":
  result = N1 + N2
elif operator == "-":
  result = N1 - N2
elif operator == "*":
  result = N1 * N2
elif operator == "/":
  result = N1/N2
else:
  result = "Invalid operator"
print("Result:", result)
