first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
if second_number != 0:
    division_result = first_number / second_number
else:
    division_result = "Error: Division by zero"
    print("Sum:", sum_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)