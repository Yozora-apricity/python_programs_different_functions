# Ask user to input a number
# Sort the number
#Display number

while True:
try:
        
        num = int(input("Enter a number: "))
        numbers += [num]
        
except ValueError:
    break
    
numbers.sort()

print(numbers)