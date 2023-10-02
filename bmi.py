height = float(input("enter your height: "))
weight = float(input("enter your weight: "))
bmi = weight/height*height
if bmi < 18.5:
    print(f"your bmi is {bmi}, youre underweight ")
elif bmi < 25:
    print(f"your bmi is {bmi}, youre normal")
elif bmi < 30: 
    print(f"your bmi is {bmi}, youre overweight")
elif bmi < 35:
    print(f"your bmi is {bmi}, youre obese")
else:
    print(f"your bmi is {bmi}, youre clinically obese")