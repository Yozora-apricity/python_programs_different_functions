#1. Ask a number from the user 10 times
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))
num6 = int(input("Enter a number: "))
num7 = int(input("Enter a number: "))
num8 = int(input("Enter a number: "))
num9 = int(input("Enter a number: "))
num10 = int(input("Enter a number: "))

#2. Count the number of even numbers
even_count = 0
for i in range(1, 11):
    if i % 2 == 0:
        even_count += 1

#3. Print the number of even numbers
print("The number of even numbers is", even_count)