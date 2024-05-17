total_letters = 0

for n in range(1, 1000 + 1):
    numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    words = ""
    
    if n == 1000:
        words = "onethousand"
    
    else:
        # Handling hundreds place
        if n >= 100:
            words += numbers[n // 100] + "hundred"
            n %= 100
            if n > 0:
                words += "and"
        
        # Handling tens and numbers place
        if n >= 20:
            words += tens[n // 10]
            n %= 10
        elif n >= 11:
            words += teens[n - 10]
            n = 0
        
        words += numbers[n]
    
    total_letters += len(words)

print(total_letters)
