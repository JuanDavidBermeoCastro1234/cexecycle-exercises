# Ask the user for the maximum power up to which to generate powers of 2
n = int(input("Enter the maximum power (n): "))

# Generate and display powers of 2 from 2^0 to 2^n
for i in range(n + 1):
    print(f"2^{i} = {2 ** i}")