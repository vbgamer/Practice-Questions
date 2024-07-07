#Write a Python program that prompts the user to enter 10 numbers. The program should then filter and display the even and odd numbers separately.
#Ensure your program handles the input of any valid numerical values.
numbers = []
for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("\nEven numbers:")
for num in even_numbers:
    print(num)

print("\nOdd numbers:")
for num in odd_numbers:
    print(num)
