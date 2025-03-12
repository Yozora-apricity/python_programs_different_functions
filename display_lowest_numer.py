# Store the lowest number
# Ask user for input
# If lowest is None or num is smaller, update lowest
# If input is not a valid number, break the loop
# Display the lowest number if any valid number was entered

def find_lowest_number():
    lowest = None

    while True:
        try:
            num = int(input("Enter a number (or any non-number to stop): "))

            if lowest is None or num < lowest:
                lowest = num

        except ValueError:
            break

    if lowest is not None:
        print(f"The lowest number entered was: {lowest}")
    else:
        print("No valid numbers were entered.")

find_lowest_number()
