# Initialize variables to store the maximum palindrome and its factors
maxPalindrome = 0
factor1 = 0
factor2 = 0

# Iterate through all three-digit numbers for both factors
for i in range(100, 1000):
    for j in range(100, 1000):
        # Calculate the product
        product = i * j
        
        # Check if the product is a palindrome
        productStr = str(product)
        if productStr == productStr[::-1]:
            # If it's a palindrome and greater than the current maximum, update the maximum and factors
            if product > maxPalindrome:
                maxPalindrome = product
                factor1 = i
                factor2 = j

# Print the largest palindrome and its factors
print("Largest palindrome:", maxPalindrome)
print("Factors:", factor1, "x", factor2)
