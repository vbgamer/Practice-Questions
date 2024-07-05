#Write a Python program that accepts an array of numbers from the user and display the numbers in ascending order.
#Ensure your program handles any valid number of elements in the array.


numbers_input = input("Enter numbers separated by spaces: ")

numbers_list = numbers_input.split()

numbers = []
for number in numbers_list:
    numbers.append(float(number))

numbers.sort()

print("Numbers in ascending order:")
for number in numbers:
    print(number)
