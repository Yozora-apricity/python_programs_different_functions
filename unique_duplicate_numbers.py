# 1. Start with an empty list called 'numbers' to keep track of what the user enters.
numbers = []

# 2. Use a loop to continuously ask the user for a number.
while True:
    try:
        num = int(input("Enter a number: "))
    
# 3. Check if the number is already in 'numbers'
#    - If yes, print "Duplicate"
#    - If no, print "Unique" and add it to 'numbers'
    if num in numbers:
        print("duplicate")
    else:
        print("unique")
        numbers = numbers + [num]

# 4. If the user enters an invalid input, exit the loop and end the program.
    except ValueError:
    print ("Invalid input. Exit Program.")
    break