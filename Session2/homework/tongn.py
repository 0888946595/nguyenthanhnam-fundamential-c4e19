numb = int(input("Hay nhap so ban muon"))
def factorial(numb):
    if numb == 0:
        return 1
    else:
        return numb*factorial(numb-1)

print (factorial(10))


        
