
# Initialize variables to store the Fibonacci sequence and the sum of even terms
fibSequence = [1, 2]  # Start with the first two terms of the sequence
evenSum = 2  # Since the second term is even, initialize the sum with its value

# Loop to generate Fibonacci sequence until the limit
while True:
    # Generate the next Fibonacci term by adding the previous two terms
    nextTerm = fibSequence[-1] + fibSequence[-2]
    
    # Check if the next term exceeds the limit, if so, break the loop
    if nextTerm > 4000000:
        break
    
    # Add the next term to the Fibonacci sequence
    fibSequence.append(nextTerm)
    
    # Check if the next term is even and add it to the sum if it is
    if nextTerm % 2 == 0:
        evenSum += nextTerm

result = evenSum

print(result)
