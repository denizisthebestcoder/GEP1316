# Initialize the count of prime numbers and the number to check for primality
primeCount = 1  # We start with 1 to account for 2 as the first prime
number = 3      # We start checking from 3 since 2 is the first prime

# Loop until we find the 10001st prime
while primeCount < 10001:
    isPrime = True  # Assume the number is prime initially
    
    # Check if the number is divisible by any odd number less than itself
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:  # If the number is divisible by the divisor
            isPrime = False  # Then it's not prime
            break  # No need to continue checking for other divisors
            
    if isPrime:  # If the number is prime
        primeCount += 1  # Increment the prime count
        prime = number  # Store the prime number
    number += 2  # Move to the next odd number for checking primality

# Print the 10001st prime number
print(prime)
