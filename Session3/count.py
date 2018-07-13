
numb = int(input("Enter a number: "))

counting = True 
original_numb = numb

count = 0
while counting:
    numb = numb // 10
    count += 1    
    if numb == 0:
        counting = False
    
        
    # else:
    #     print (count)
    #     loop = False 
print("{0} has {1} digit(s)".format(original_numb, count))