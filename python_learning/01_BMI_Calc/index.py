weight = input("Please enter your weight :- ")
height = input("Please enter your height :- ")

if weight.isnumeric() or height.numeric():
    print("Your BMI is :- ", int(weight)//(float(height)**2))
else:
    print("Please enter a valid input..!")
