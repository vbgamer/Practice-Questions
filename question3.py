#Write a Python program that takes two numbers as input from the user, swaps their values, and then prints the swapped values.
#Ensure your program handles the input of any valid numerical values. give simple code
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

num1, num2 = num2, num1

print("\nAfter swapping:")
print(f"First number: {num1}")
print(f"Second number: {num2}")
