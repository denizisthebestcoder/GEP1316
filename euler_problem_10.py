# Initialize variables
limit = 2000000
sumOfPrimes = 0

# Create a list to store whether a number is prime or not
isPrime = [True] * limit
isPrime[0] = isPrime[1] = False

# Loop to sieve out non-prime numbers
for i in range(2, int(limit ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i * i, limit, i):
            isPrime[j] = False

# Loop to sum up prime numbers
for i in range(limit):
    if isPrime[i]:
        sumOfPrimes += i

# Print the result
print("The sum of all prime numbers below two million is:", sumOfPrimes)
