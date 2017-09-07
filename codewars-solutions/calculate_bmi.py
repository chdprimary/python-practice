# Write function bmi that calculates body mass index (bmi = weight / height ^ 2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    output = ""
    bmi = weight / pow(height, 2)
    if bmi <= 18.5:
        output = "Underweight"
    elif bmi <= 25.0:
        output = "Normal"
    elif bmi <= 30.0:
        output = "Overweight"
    elif bmi > 30.0:
        output = "Obese"
    return output