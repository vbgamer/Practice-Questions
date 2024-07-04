#Write a python program to enter a number and display its hexa and octa equlivalent and its sqaure root\
num = int(input("Enter a Number"))
print ("Hexa - Decimal of" + str(num)+ ":"+ str(hex(num)))
print ("Octal  of" + str(num)+ ":"+ str(oct(num)))
print ("Square Root of" + str(num)+ ":"+ str(num**0.5))
