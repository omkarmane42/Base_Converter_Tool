# -----------------------------------------
# Base Converter Tool Program
# -----------------------------------------

print("===== Base Converter Tool =====")

while True:
    print("\nSupported Bases:")
    print("2  -> Binary")
    print("8  -> Octal")
    print("10 -> Decimal")
    print("16 -> Hexadecimal")
    print("Type 'exit' to stop")

    source_base = input("\nEnter Source Base: ")

    if source_base.lower() == "exit":
        print("Program Ended.")
        break

    target_base = input("Enter Target Base: ")

    number = input("Enter Number: ")

    try:
        # Convert to decimal first
        decimal_number = int(number, int(source_base))

        # Convert decimal to target base
        if target_base == "2":
            result = format(decimal_number, "b")
        elif target_base == "8":
            result = format(decimal_number, "o")
        elif target_base == "10":
            result = decimal_number
        elif target_base == "16":
            result = format(decimal_number, "X")
        else:
            result = "Unsupported Target Base"

        print("Converted Result:", result)

    except ValueError:
        print("Invalid number for given base. Try again.")
