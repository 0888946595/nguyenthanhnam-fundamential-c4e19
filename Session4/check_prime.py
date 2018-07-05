numb = int(input("Enter a number: "))

a = 2
loop = True

while a < numb:
    if numb % a == 0 :
        loop = False
        break
        # print (" is a prime number")
    a +=1

if loop  == True:
    print ("{0} is a prime number".format(numb)) 
else:
    print ("{0} is not prime number".format(numb))
    
