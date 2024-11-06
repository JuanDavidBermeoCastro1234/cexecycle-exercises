# Ask the user for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Make sure num1 is the smaller number and num2 is the larger one
if num1 > num2:
    num1, num2 = num2, num1  # Swap the values if needed

# Calculate the sum of the numbers between num1 and num2
sum_result = sum(range(num1 + 1, num2))

# Display the result
print(f"The sum of the numbers between {num1} and {num2} is: {sum_result}")
