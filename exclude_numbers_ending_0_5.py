num = 0

#Loop through numbers from 0 to 100
while num < 100:
#Check if number is not divisible by 10 and 5
    if num % 10 != 0 and num % 5 != 0:
        print(num)
    num += 1