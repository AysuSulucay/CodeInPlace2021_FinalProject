# the function where all conversions are gathered in one place
def allconversion(number):
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)
    print("Binary representation: ",binary)
    print("Octal representation: ",octal)
    print("Hexadecimal representation: ",hexadecimal)


print("\nConvert Decimal Number to Binary or Octal or Hexadecimal or All-in-one")

"""
Binary is a numeric system that only uses two digits '0' and '1'

Octal is a numeric system that uses eight digits (0-7)

Hexadecimal is a numeric system that uses the decimal numbers(base 10) 
and siz extra symbols(a,b,c,d,e,f).
"""


while True:
    try:
        decimal_number = int(input("Enter Decimal Number: "))
        
        if decimal_number != float:
            print("Decimal Number Entered Successfully!")
            break;
    except ValueError:
        # We want to from the user enter an integer value
        print("Please provide an integer value")

converted_number = 0
while True:
    try:
        convert_to = int(input("\nConvert into: [2] Binary, [8] Octal, [16] Hexadecimal, [1]All: \n Please enter the corresponding numeric value: "))
        # Want to user enter the numeric values of corresponding the convertion name
        if convert_to == 2:
            converted_number = bin(decimal_number)
            print("Converting Decimal to Binary: ",converted_number)
            break;
        elif convert_to == 8:
            converted_number = oct(decimal_number)
            print("Converting Decimal to Octal: ",converted_number)
            break;
        elif convert_to == 16:
            converted_number = hex(decimal_number)
            print("Converting Decimal to Hexadecimal: ",converted_number)
            break;
        elif convert_to == 1:
            converted_number = allconversion(decimal_number)
            break;
        else:
            print("Please choose your conversion type from the list")
    except:
        continue



    
