
number = int(input("Enter a number to see its multiplication table: "))


print(f"\nMultiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
