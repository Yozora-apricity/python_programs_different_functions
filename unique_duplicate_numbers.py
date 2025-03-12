# 1. Start with an empty list called 'numbers' to keep track of what the user enters.
# 2. Use a loop to continuously ask the user for a number.
# 3. Check if the number is already in 'numbers'
#    - If yes, print "Duplicate"
#    - If no, print "Unique" and add it to 'numbers'
# 4. If the user enters an invalid input, exit the loop and end the program.

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers = numbers + [num]
    except ValueError:
        print("Invalid input. Exiting program.")
        break
