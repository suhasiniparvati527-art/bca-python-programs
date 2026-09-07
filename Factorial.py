def factorial(n): 
 if n <= 0: 
 return "Invalid input! Factorial is not defined for negative numbers." 
 result = 1 
 for i in range(1, n + 1): # i=1 
 result *= i 
 return result 
 
number = int(input("Enter a positive number: ")) 
print("Factorial of", number, "is", factorial(number)) 