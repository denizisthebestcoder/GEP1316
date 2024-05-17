import itertools

isEvenlyDividedForAllNumbers = False


for number in itertools.count(start = 1):
    for x in range (1,21):
        print("number:" + str(number))
        
        if number % x == 0:
            isEvenlyDividedForAllNumbers = True
            
            if(x == 20 and isEvenlyDividedForAllNumbers):
                print("her şeye bölünebildim: " + str(number))
                break
        else:
            isEvenlyDividedForAllNumbers = False
            print(str(number) + " sayısını" + str(x) + "'e bölemedim")
            break
        
    if isEvenlyDividedForAllNumbers:
        break
        
   
           
