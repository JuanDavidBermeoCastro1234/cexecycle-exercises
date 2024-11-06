n = int(input("Enter the number of terms (n): "))

pi_estimation = 0

for i in range(n):
    sign = (-1) ** i
    pi_estimation += sign / (2 * i + 1)

pi_estimation *= 4

print(f"The estimation of pi with {n} terms is: {pi_estimation}")
