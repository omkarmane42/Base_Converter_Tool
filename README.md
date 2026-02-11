# 🔢 Base Converter Tool (Python)

A simple Python command-line application that converts numbers between different number systems:
- Binary (Base 2)
- Octal (Base 8)
- Decimal (Base 10)
- Hexadecimal (Base 16)

---

---

## 🚀 Features

- Convert numbers between base 2, 8, 10, and 16
- Continuous conversion until user types `exit`
- Error handling for invalid inputs
- Simple CLI interface

---

## 🛠️ Technologies Used

- Python 3
- Built-in functions:
  - `int()`
  - `format()`
  - `input()`
  - `try-except`

---

## 📜 Source Code

```python
# -----------------------------------------
# Base Converter Tool
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
---
#Output
```
===== Base Converter Tool =====

Supported Bases:
2  -> Binary
8  -> Octal
10 -> Decimal
16 -> Hexadecimal
Type 'exit' to stop

Enter Source Base: 2
Enter Target Base: 10
Enter Number: 1010

Converted Result: 10
```
