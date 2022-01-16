# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(round(weight / (height ** 2)))
if bmi < 18.5:
    result = 'are underweight'
elif bmi < 25:
    result = 'have a normal weight'
elif bmi < 30:
    result = 'are slightly overweight'
elif bmi < 35:
    result = 'are obese'
else:
    result = 'clinically obese'
print(f'Your BMI is {bmi}, you {result}.')
