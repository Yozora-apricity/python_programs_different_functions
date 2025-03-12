#Set up initial values
total = 0
count = 0
# Loop to get user input continuously
while True:
    try:
        num = int(input("Enter a number: "))
        total += num
        count += 1
    except ValueError:
        break
# Calculate and display the average
if count > 0:
    average = total / count
    print("Average of entered numbers:", average)
else:
    print("No valid numbers entered.")