print("__________BMI CAlculator__________")

#Height 
height = float(input("Enter your height: "))
height_unit = input("Enter height unit (m/cm/ft/in): ").lower()
if height_unit == "m":
    height_m = height
elif height_unit == "cm":
    height_m = height/100
elif height_unit =="ft":
    height_m = height*0.3048
elif height_unit == "in":
    height_m = height * 0.0254
else:
    print("Invalid height unit!")

#Weight
weight = float(input("Enter your weight: "))
weight_unit = input("Enter weight unit (kg/g/lb): ").lower()
if weight_unit == "kg":
    weight_kg = weight
elif weight_unit == "g":
    weight_kg = weight/1000
elif weight_unit == "lb":
    weight_kg = weight*0.453592
else:
    print("Invalid weight unit!")

#BMI Calculation
bmi = weight_kg / (height_m**2)
    print("\nYour BMI is:", round(bmi,2))

#BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")
