def btd():
    n = int(input("Enter any integer Decimal number:\n"))              #take decimal number as a input from user
    v = []                                                             #create empty list for further use
    m = n                                                              #this is for save the value of input number
    while n != 0:  
        bin = n % 2                                                    #first it will find remainder of the input
        v.append(bin)                                                  #the remainder will append into empty list
        n = n//2                                                       #then the number will divided by 2 upto bin = 1 
         
    bin = v[::-1]                                                      #binary number will be in reverse order in that list
                                                                       #so we have to revers it again to get perfect value
    binary = ''.join(str(i) for i in bin)                              #this is use to convert list into number                                     
    print("The binary conversion of {0} is {1}".format(m,binary))      #print the binary number

btd() 