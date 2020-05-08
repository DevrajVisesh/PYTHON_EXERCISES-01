#Program on Arithmatic Operation
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
print("Enter which operation would you like to perform?")
operation = input("Enter any of these char for specific operations +, -, *, /:")

result = 0
if operation == '+':
         result = num1 + num2
elif operation == "-":
         result += num1- num2 
else:
    print("Input character is not recognized") 
print(num1, operation, num2, ":", result) 

