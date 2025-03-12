# Initialize the highest number variable
highest = None

# Continuously ask for input until an invalid entry is given
while True:
    try:
        num = int(input("Enter a number: "))
        
        # Update the highest number if needed
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break

# Display the highest number entered
if highest is not None:
    print("The highest number entered was:", highest)
else:
    print("No valid numbers were entered.")
