import itertools

# Initialize a variable to track whether the number is evenly divisible by all numbers
isEvenlyDividedForAllNumbers = False

# Loop indefinitely over numbers starting from 1
for number in itertools.count(start=1):
    # Loop over numbers from 1 to 20
    for x in range(1, 21):
        # Print the current number being checked
        print("number:" + str(number))
        
        # Check if the current number is evenly divisible by the current value of x
        if number % x == 0:
            # If evenly divisible, set the flag to True
            isEvenlyDividedForAllNumbers = True
            
            # If all numbers from 1 to 20 evenly divide the current number, print the number and break the loop
            if x == 20 and isEvenlyDividedForAllNumbers:
                print("her şeye bölünebildim: " + str(number))
                break
        else:
            # If the current number is not evenly divisible by the current value of x, set the flag to False
            isEvenlyDividedForAllNumbers = False
            # Print the message indicating the number couldn't be divided by x
            print(str(number) + " sayısını " + str(x) + "'e bölemedim")
            # Break the loop over x to proceed to the next number
            break
        
    # If the number is found to be evenly divisible by all numbers from 1 to 20, break the loop
    if isEvenlyDividedForAllNumbers:
        break
