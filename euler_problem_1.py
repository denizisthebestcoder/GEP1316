
# Initialize a variable to store the sum of multiples of 3 or 5
sum = 0

# Iterate through numbers from 0 to 999 (exclusive), as we want multiples below 1000
for number in range(1000):
    # Check if the current number is divisible by 3 or 5 without remainder
    if number % 3 == 0 or number % 5 == 0:
        # If the number is divisible by 3 or 5, add it to the sum
        sum += number

# Print the total sum of multiples of 3 or 5 below 1000
print(sum)
