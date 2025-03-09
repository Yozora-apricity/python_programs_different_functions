# Program to print numbers from 0 to 100 except those ending in zero
for current_number in range(101):  # Loop from 0 to 100
    if current_number % 10 != 0:  # Check if the number does not end in zero
        print(current_number) # Print the number