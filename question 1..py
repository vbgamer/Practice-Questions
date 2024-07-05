#Write a Python program to calculate Body Mass Index (BMI) based on user input for weight in kilograms and height in meters. Ensure your program validates input
#and provides meaningful feedback to the user. Use the BMI formula: BMI = weight (kg) / (height (m))^2.

def calculate_bmi(weight, height):
    return weight / (height ** 2)
def main():
    print("Welcome to the BMI Calculator!")

    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return
        bmi = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
