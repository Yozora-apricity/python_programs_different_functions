# Ask user to input a number
while True:
    try:
        user_number = int(input("Enter a number: "))
        numbers = numbers + [user_number]   
    except ValueError:
        break

# Sort the list number
numbers.sort(reverse=True)

# Display number
print("Sorted numbers (highest to lowest):", numbers)