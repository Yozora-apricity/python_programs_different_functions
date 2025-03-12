def most_frequent():
    # Store number frequencies  
    freq = {}  
    
    # Take user input  
    while True:
        try:
            num = int(input("Enter a number: "))
            
            # Count occurrences  
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        except ValueError:
            break
        
    # Find the most frequent number  
    most_common = None
    highest_count = 0

    for num in freq:
        if freq[num] > highest_count:
            highest_count = freq[num]
            most_common = num
            
    # Print the result  
    if most_common is not None:
        print("Most frequent number:", most_common)
    else:
        print("No numbers entered.")

most_frequent()