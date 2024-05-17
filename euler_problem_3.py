# Initialize the number
number = 600851475143

# Start with the smallest prime number
factor = 2

# Keep dividing the number by the smallest prime factor until it cannot be divided further
while factor * factor <= number:
    # If the number is divisible by the current factor
    while number % factor == 0:
        # Divide the number by the factor
        number //= factor
    # Move to the next prime factor
    factor = factor + 1

# The remaining number after all divisions is the largest prime factor
largestPrimeFactor = number

# Print the largest prime factor
print(largestPrimeFactor)
