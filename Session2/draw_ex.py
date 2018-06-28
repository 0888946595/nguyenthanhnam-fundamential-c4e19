# for i in range (7):
#     for j in range (7):
#      print ("* ", end="")
#     print () 

# for i in range (5):
#     for j in range (i+1):
#         print ("* ", end=" ")
#     print (      )

n=10    
for i in range (n):
    for j in range (n):
        if (j< n-i-1):
            print ("* ", end=" ")
        else:
            print ("* ", end="")    
    print ()