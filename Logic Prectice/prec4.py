# Find factorial of n number

num = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f"The factorial of {i} is {factorial}")