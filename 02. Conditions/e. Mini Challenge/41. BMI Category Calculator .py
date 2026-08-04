# A Program to Calculate BMI and Determine Category.

weight = float(input("\nEnter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
    
# Explanation:
# In this code snippet, we take the user's weight in kilograms and height in meters as input. We then calculate the Body Mass Index (BMI) using the formula: BMI = weight / (height^2). Based on the calculated BMI, we determine the category of the user using if-elif-else statements. The categories are Underweight, Normal Weight, Overweight, and Obese. This code helps in assessing the user's BMI and categorizing their weight status accordingly.