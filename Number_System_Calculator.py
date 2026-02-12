#Number System Calculator


Decimal_Number = int( input("Enter a Decimal Number : "))

#convert into different number system 
Binary_number = bin(Decimal_Number)
Octal_number = oct(Decimal_Number)
Hexadecimal_number = hex(Decimal_Number)

# Show the result

print("\n-------Coversion Result--------")
print("Binary :",Binary_number)
print("Ocatal :",Octal_number)
print("Hexadecimal: ", Hexadecimal_number)



