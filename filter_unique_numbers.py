# 1. Ask user to input 10 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
num6 = int(input("Enter sixth number: "))
num7 = int(input("Enter seventh number: "))
num8 = int(input("Enter eighth number: "))
num9 = int(input("Enter ninth number: "))
num10 = int(input("Enter tenth number: "))

#2. Store the numbers in a list
numbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

unique_numbers = [""] * 10

for num in numbers:
    if num not in unique_numbers:
        for i in range(10):
            if unique_numbers[i] == "":
                unique_numbers[i] = num
                break
            
#3. Print the duplicate numbers
print("Numbers without duplicates: ")
for num in unique_numbers:
    if num != "":
        print(num)